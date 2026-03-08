---
description: How to deploy and manage systemd background schedulers
---

# Systemd Scheduler Guide

This workspace uses the Linux `systemd` daemon to handle exact interval-based and calendar-based background executions. Instead of managing crontabs manually, this system uses `.service` and `.timer` files pair architecture.

## 1. Deployment Instructions

All `.service` and `.timer` files are stored in the `scripts/` directory.

To register these with the operating system, you should copy or symlink them to `/etc/systemd/system/`:

```bash
# 1. 파일들을 systemd 디렉토리로 복사 (또는 심볼릭 링크)
sudo cp scripts/*.service /etc/systemd/system/
sudo cp scripts/*.timer /etc/systemd/system/

# 2. 데몬 리로드 (systemd에 새로운 파일을 인식시킴)
sudo systemctl daemon-reload

# 3. 타이머 활성화 및 시작 (서버 재부팅 시에도 자동 구동되게 설정)
sudo systemctl enable --now main-5min.timer
sudo systemctl enable --now main-1hour.timer
sudo systemctl enable --now main-daily.timer
sudo systemctl enable --now generate-jobs.timer
```

_(참고: `.service` 파일은 타이머가 호출하므로 직접 `enable` 할 필요가 없습니다)_

## 2. Managing and Monitoring Services

Systemd provides powerful tools to check the status and logs of your backend scrapers:

### Check Status

타이머가 정상적으로 다음 스케줄을 기다리고 있는지, 혹은 서비스가 현재 구동 중인지 확인할 때 사용합니다:

```bash
# 특정 주기의 타이머 상태 확인 (다음에 언제 실행되는지)
sudo systemctl status main-5min.timer
sudo systemctl status generate-jobs.timer

# 현재 봇이 크롤링을 수행중인지 상태 확인
sudo systemctl status main-5min.service
```

### View Logs

애플리케이션 내의 `logs/` 폴더 외에도 OS 레벨에서 관리하는 시스템 로그를 스트리밍할 수 있습니다. `journalctl`을 사용합니다:

```bash
# 5분 주기 작업의 시스템 로그 스트리밍 (실시간 모니터링: -f)
sudo journalctl -u main-5min.service -f

# 월간 배치 작업의 로그 스트리밍
sudo journalctl -u generate-jobs.service -f
```

### Manual Trigger

타이머 시간을 기다리지 않고 지금 즉시 강제로 배치를 한 바퀴 돌리고 싶을 때는 `.service`를 직접 시작해주면 됩니다:

```bash
# 즉시 5분 주기 큐의 대상들을 소환해 실행
sudo systemctl start main-5min.service

# 즉시 월간 배치 작업을 구동 (generate_jobs.py 강제 실행)
sudo systemctl start generate-jobs.service
```

## 3. Configuration Reference

- **`main-[cycle].service`**: `run_cycle.sh`를 통해 `main.py --cycle [cycle]` 모드로 시스템을 실행합니다.
- **`generate-jobs.service`**: `run_generate_jobs.sh`를 통해 `generate_jobs.py` (당월 타겟 자동 생성기)를 실행합니다.
- **`[name].timer`**: 각 주기나 캘린더 (예: 매월 1일)에 맞춰 위의 `.service`를 대신 실행해주는 알람 시계 역할을 합니다.
