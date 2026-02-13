# KIS Auth 모듈 리팩토링 가이드

## 개요
기존 kis_auth.py를 기능별로 4개 모듈로 분리하여 재구성했습니다.

## 새로운 구조

```
kis_auth.py (기존 - 800줄)
    ↓
    분리
    ↓
├── kis_config.py      (설정 및 환경 관리)
├── kis_auth_new.py    (인증 전용)
├── kis_http.py        (HTTP 요청/응답)
├── kis_websocket.py   (WebSocket 전용)
└── kis_api.py         (통합 모듈 - 하위 호환)
```

## 모듈별 역할

### 1. kis_config.py (설정 및 환경 관리)
**책임:**
- YAML 설정 파일 로드
- 환경 변수 관리 (실전/모의, 상품 코드)
- 계좌 정보 관리
- 기본 헤더 생성

**주요 클래스:**
- `KISConfig`: 설정 관리

**주요 함수:**
- `get_global_config()`: 전역 설정 인스턴스
- `getEnv()`: 설정 딕셔너리 반환 (하위 호환)
- `getTREnv()`: 거래 환경 반환 (하위 호환)
- `isPaperTrading()`: 모의투자 여부 (하위 호환)

### 2. kis_auth_new.py (인증 전용)
**책임:**
- 토큰 발급
- 토큰 저장/로드
- 토큰 만료 체크
- 자동 재인증

**주요 클래스:**
- `KISAuthManager`: 인증 관리

**주요 함수:**
- `auth(svr, product)`: 토큰 발급 (하위 호환)
- `reAuth(svr, product)`: 재인증 (하위 호환)
- `save_token()`: 토큰 저장 (하위 호환)
- `read_token()`: 토큰 로드 (하위 호환)

### 3. kis_http.py (HTTP 요청/응답)
**책임:**
- REST API 호출
- 응답 파싱 및 래핑
- Hash key 관리
- Rate limiting

**주요 클래스:**
- `KISHttpClient`: HTTP 클라이언트
- `APIResponse`: 응답 래퍼
- `APIResponseError`: 에러 응답

**주요 함수:**
- `_url_fetch()`: API 호출 (하위 호환)
- `smart_sleep()`: Rate limit 대기 (하위 호환)

### 4. kis_websocket.py (WebSocket 전용)
**책임:**
- WebSocket 인증
- 실시간 데이터 수신
- 암호화/복호화
- 구독 관리

**주요 클래스:**
- `KISWebSocket`: WebSocket 클라이언트
- `KISWebSocketAuth`: WebSocket 인증

**주요 함수:**
- `auth_ws()`: WebSocket 인증 (하위 호환)
- `aes_cbc_base64_dec()`: 복호화 (하위 호환)
- `add_open_map()`: 구독 추가 (하위 호환)
- `add_data_map()`: 데이터 매핑 (하위 호환)

### 5. kis_api.py (통합 모듈)
**책임:**
- 모든 모듈의 통합 인터페이스
- 하위 호환성 제공
- 편의 함수 제공

## 마이그레이션 방법

### 방법 1: 최소 변경 (추천)

기존 코드를 거의 수정하지 않고 사용할 수 있습니다.

**기존:**
```python
import kis_auth as ka

ka.auth()
result = ka._url_fetch(url, tr_id, "", params)
```

**변경:**
```python
import kis_api as ka  # kis_auth → kis_api만 변경

ka.auth()
result = ka._url_fetch(url, tr_id, "", params)
```

### 방법 2: 새로운 API 사용

객체 지향 스타일로 사용할 수 있습니다.

```python
from kis_api import KISAuthManager, KISHttpClient

# 인증
auth_manager = KISAuthManager()
token = auth_manager.authenticate(server="prod")

# HTTP 클라이언트
http_client = KISHttpClient(debug=True)
response = http_client.fetch(
    api_url="/uapi/...",
    tr_id="TRID001",
    params={"KEY": "VALUE"}
)

if response.is_ok():
    data = response.get_body()
```

### 방법 3: 편의 함수 사용

```python
from kis_api import initialize, get_client

# 초기화 (인증 + 클라이언트 설정)
initialize(server="prod", debug=True)

# 클라이언트 가져오기
client = get_client()
response = client.fetch(api_url="/uapi/...", tr_id="TRID001")
```

## 코드 비교

### 인증

**기존:**
```python
import kis_auth as ka
ka.auth()
```

**새로운 방식 1 (하위 호환):**
```python
import kis_api as ka
ka.auth()
```

**새로운 방식 2 (OOP):**
```python
from kis_api import KISAuthManager

auth_manager = KISAuthManager()
token = auth_manager.authenticate()
```

### API 호출

**기존:**
```python
import kis_auth as ka

ka.auth()
result = ka._url_fetch(
    api_url="/uapi/...",
    ptr_id="TRID001",
    tr_cont="",
    params={"KEY": "VALUE"}
)
```

**새로운 방식 1 (하위 호환):**
```python
import kis_api as ka

ka.auth()
result = ka._url_fetch(
    api_url="/uapi/...",
    ptr_id="TRID001",
    tr_cont="",
    params={"KEY": "VALUE"}
)
```

**새로운 방식 2 (OOP):**
```python
from kis_api import KISAuthManager, KISHttpClient

auth = KISAuthManager()
auth.authenticate()

client = KISHttpClient()
response = client.fetch(
    api_url="/uapi/...",
    tr_id="TRID001",
    params={"KEY": "VALUE"}
)
```

### WebSocket

**기존:**
```python
import kis_auth as ka

ka.auth_ws()
ws = ka.KISWebSocket("/websocket/path")
ws.start(on_result_callback)
```

**새로운 방식 1 (하위 호환):**
```python
import kis_api as ka

ka.auth_ws()
ws = ka.KISWebSocket("/websocket/path")
ws.start(on_result_callback)
```

**새로운 방식 2 (OOP):**
```python
from kis_api import KISWebSocketAuth, KISWebSocket

auth = KISWebSocketAuth()
auth.authenticate()

ws = KISWebSocket("/websocket/path")
ws.start(on_result_callback)
```

## 마이그레이션 체크리스트

### 단계 1: 파일 교체
- [ ] 기존 kis_auth.py 백업
- [ ] 새 모듈 5개 복사 (kis_config.py, kis_auth_new.py, kis_http.py, kis_websocket.py, kis_api.py)

### 단계 2: import 변경
- [ ] `import kis_auth as ka` → `import kis_api as ka`
- [ ] 다른 코드는 변경 불필요 (하위 호환)

### 단계 3: 테스트
- [ ] 인증 테스트 (`ka.auth()`)
- [ ] API 호출 테스트 (`ka._url_fetch()`)
- [ ] WebSocket 테스트 (사용 시)

### 단계 4: (선택) 새로운 API로 전환
- [ ] 객체 지향 스타일로 점진적 전환
- [ ] 에러 처리 개선
- [ ] 로깅 추가

## 장점

### 1. 모듈화
- 각 기능이 독립적인 파일로 분리
- 유지보수 용이
- 테스트 용이

### 2. 명확한 책임 분리
- 설정 → kis_config.py
- 인증 → kis_auth_new.py
- HTTP → kis_http.py
- WebSocket → kis_websocket.py

### 3. 하위 호환성
- 기존 코드를 거의 수정하지 않고 사용 가능
- `kis_auth` → `kis_api`만 변경

### 4. 확장성
- 새로운 기능 추가 시 적절한 모듈에만 추가
- 다른 모듈에 영향 최소화

### 5. 객체 지향
- 상태 관리 용이
- 멀티 계정 지원 가능
- 테스트 코드 작성 용이

## 문제 해결

### Q1: import 에러
```
ModuleNotFoundError: No module named 'kis_config'
```

**해결:** 모든 모듈 파일이 같은 디렉토리에 있는지 확인

### Q2: 기존 코드가 작동하지 않음
```
AttributeError: module 'kis_api' has no attribute '...'
```

**해결:** kis_api.py의 `__all__` 리스트에 해당 함수가 있는지 확인

### Q3: WebSocket 연결 실패
```
WebSocket 인증 실패
```

**해결:** `auth_ws()` 호출 확인 (`auth()`가 아님)

## 추가 개선 사항

### 1. 로깅 개선
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### 2. 설정 파일 경로 커스터마이징
```python
from kis_api import KISConfig

config = KISConfig(config_dir="/my/custom/path")
```

### 3. 멀티 계정 지원
```python
from kis_api import KISAuthManager, KISHttpClient

# 계정 1
auth1 = KISAuthManager(config_dir="/account1")
auth1.authenticate()
client1 = KISHttpClient()

# 계정 2
auth2 = KISAuthManager(config_dir="/account2")
auth2.authenticate()
client2 = KISHttpClient()
```

## 요약

1. **최소 변경**: `import kis_auth` → `import kis_api`
2. **기존 코드**: 대부분 그대로 동작 (하위 호환)
3. **새로운 기능**: 필요시 OOP 스타일 사용
4. **모듈화**: 각 기능이 독립적으로 분리됨

이제 깔끔하고 유지보수하기 쉬운 코드를 사용할 수 있습니다! 🎉
