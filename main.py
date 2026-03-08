import sys
import logging
import argparse
import json
from typing import Dict, Any, Optional

import pandas as pd

from app.api import kis_auth as ka
from app.database import DatabaseManager
from app.config import DB_PATH
from scripts.log_setup import setup_logging

setup_logging()


class APIManager:
    """API 관리 및 실행 클래스"""
    
    def __init__(self, db_path: str = None):
        self.db = DatabaseManager(db_path)
    
    def execute(self, job_id: str, skip_validation: bool = False) -> pd.DataFrame:
        """
        DB에 저장된 정보로 API 실행
        """
        
        # 2. 사용자 입력
        job_input = self.db.get_api_job_mst(job_id)
        if not job_input:
            raise ValueError(
                f"사용자 입력(Job) 없음: {job_id}\n"
            )
        
        api_id = job_input.api_id
        
        # 1. API 정의
        api_def = self.db.get_api_mst(api_id)
        if not api_def:
            raise ValueError(f"API 정의 없음: {api_id}")
        
        logging.info("="*60)
        logging.info(f"API 실행: {api_id} (Job: {job_id})")
        logging.info("="*60)
        logging.info(f"URL: {api_def.api_url}")
        logging.info(f"API_ID: {api_def.api_id}")
        
        raw_params = job_input.params_json if job_input else {}
        if isinstance(raw_params, str):
            import json
            raw_params = json.loads(raw_params) if raw_params else {}
        params = raw_params
        
        logging.info(f"파라미터: {json.dumps(params, ensure_ascii=False)}")
        
        # 3. 검증
        if not skip_validation:
            validation = self.db.validate_job_inputs(api_id, job_id)
            
            if not validation.is_valid:
                logging.error("검증 실패:")
                for error in validation.errors:
                    logging.error(f"  ✗ {error}")
                raise ValueError("파라미터 검증 실패")
            
            if validation.warnings:
                for warning in validation.warnings:
                    logging.warning(f"  ⚠ {warning}")
            
            params = validation.validated_params
            logging.info("✓ 검증 통과")
        
        # 4. API 호출
        logging.info("API 호출 중...")
        try:
            from kis_http import get_global_http_client
            client = get_global_http_client()
            
            res = client.fetch(
                api_url=api_def.api_url,
                api_id=api_def.api_id,
                header_json=api_def.header_json,
                params=params
            )
            
            if res.is_ok():
                body = res.get_body()
                
                # output이 리스트인지 딕셔너리인지 확인하여 DF 변환
                if hasattr(body, 'output1'): 
                     data = body.output1
                elif hasattr(body, 'output'):
                    data = body.output
                else:
                    data = body._asdict()

                # dict인 경우 리스트로 감싸기 (scalar dictionary handling)
                if isinstance(data, dict):
                    data = [data]
                
                # list가 아닌 경우 (namedtuple 등) list로 변환 시도
                if not isinstance(data, list):
                     if hasattr(data, '_asdict'):
                         data = [data._asdict()]
                     else:
                         try:
                             data = list(data)
                         except:
                             data = [data]

                data = pd.DataFrame(data)

                logging.info(f"✓ 성공: {len(data)}건")
                return data
            else:
                logging.error("✗ API 호출 실패")
                res.print_error(url=api_def.api_url)
                return pd.DataFrame()
        
        except Exception as e:
            logging.error(f"✗ 오류: {e}")
            raise

    def validate_all_active_inputs(self, cycle: str = None) -> bool:
        """
        활성화된 모든 입력의 파라미터 검증
        Returns:
            bool: 모든 입력이 유효하면 True, 하나라도 실패하면 False
        """
        active_inputs = self.db.list_active_api_job_msts(cycle=cycle)
        
        if not active_inputs:
            # API Job이 없더라도 브라우저 작업은 존재할 수 있으므로 True 반환
            return True
            
        logging.info("="*60)
        logging.info(f"파라미터 사전 검증 ({len(active_inputs)}개)")
        logging.info("="*60)
        
        all_valid = True
        
        for ui in active_inputs:
            validation = self.db.validate_job_inputs(ui.api_id, ui.job_id)
            
            if not validation.is_valid:
                all_valid = False
                logging.error(f"✗ [{ui.job_id}] 검증 실패:")
                for error in validation.errors:
                    logging.error(f"    - {error}")
            else:
                logging.info(f"✓ [{ui.job_id}] 검증 통과")
                
            if validation.warnings:
                for warning in validation.warnings:
                    logging.warning(f"    ⚠ {warning}")
        
        return all_valid

    def execute_active_programs(self, http_client, cycle: str = None) -> None:
        """활성화된 프로그램 실행"""
        active_inputs = self.db.list_active_api_job_msts(cycle=cycle)
        
        if not active_inputs:
            return

        # logging.info("\n" + "="*60)
        logging.info("="*60)
        logging.info(f"일괄 실행 시작 ({len(active_inputs)}개)")
        logging.info("="*60)
        
        success_count = 0
        fail_count = 0
        
        # API 호출 (주입된 http_client 사용)
        client = http_client

        for ui in active_inputs:
            # logging.info(f"\n▶ 실행: {ui.job_id}")
            logging.info(f"▶ 실행: {ui.job_id}")
            try:
                # 1. API 정의 조회
                api_def = self.db.get_api_mst(ui.api_id)
                if not api_def:
                    logging.error(f"  ✗ API 정의 없음: {ui.api_id}")
                    fail_count += 1
                    continue
                
                # 2. 파라미터 검증 및 기본값 적용
                validation = self.db.validate_job_inputs(ui.api_id, ui.job_id)
                if not validation.is_valid:
                    logging.error(f"  ✗ 파라미터 검증 실패")
                    fail_count += 1
                    continue
                
                # 검증된 파라미터 사용 (기본값 포함)
                validated_params = validation.validated_params
                
                # 3. API 호출
                # JobMst의 params_json은 generate_jobs.py에 의해 이미 매크로가 해석, 할당된 순수 파라미터 대상입니다.
                resolved_params = validated_params
                
                logging.info(f"  - 실행 파라미터: {resolved_params}")
                
                self.db.update_api_job_status(ui.job_id, "RUNNING")
                
                res = client.fetch(
                    api_url=api_def.api_url,
                    api_id=api_def.api_id,
                    header_json=api_def.header_json,
                    params=resolved_params
                )
                
                if res.is_ok():
                    # 데이터 프레임 변환
                    body = res.get_body()
                    if hasattr(body, 'output1'): 
                         data = body.output1
                    elif hasattr(body, 'output'):
                        data = body.output
                    else:
                        data = body._asdict()
                    
                    if isinstance(data, dict):
                        data = [data]
                    
                    data = pd.DataFrame(data)
                    print(data)

                    # Output 테이블에 저장
                    saved_count = self.db.insert_output_data(ui.api_id, ui.job_id, data)
                    logging.info(f"  ✓ 성공: {len(data)}건 (DB 저장: {saved_count}건)")
                    
                    self.db.update_api_job_status(ui.job_id, "SUCCESS")
                    success_count += 1
                else:
                    err_msg = f"API 호출 실패. Status code: {res.get_status_code()}"
                    logging.error(f"  ✗ {err_msg}")
                    self.db.update_api_job_status(ui.job_id, "FAIL", err_msg)
                    fail_count += 1
                    
            except Exception as e:
                logging.error(f"  ✗ 실행 중 오류: {e}")
                self.db.update_api_job_status(ui.job_id, "FAIL", str(e))
                fail_count += 1
        
        # logging.info("\n" + "="*80)
        logging.info("="*80)
        logging.info(f"실행 완료: 성공 {success_count}, 실패 {fail_count}")
        logging.info("="*80)

    def execute_active_browser_programs(self, cycle: str = None) -> None:
        """활성화된 브라우저 스크래핑 모델 실행"""
        try:
            from app.browser_scraper import BrowserScraper
        except ImportError:
            logging.error("app/browser_scraper.py 모듈을 찾을 수 없습니다.")
            return
            
        active_browser_jobs = self.db.list_active_browser_job_msts(cycle=cycle)
        
        if not active_browser_jobs:
            return
            
        logging.info("="*60)
        logging.info(f"브라우저 스크래핑 일괄 실행 시작 ({len(active_browser_jobs)}개)")
        logging.info("="*60)
        
        success_count = 0
        fail_count = 0
        
        scraper = BrowserScraper(self.db)
        
        for job in active_browser_jobs:
            logging.info(f"▶ 브라우저 스크래핑 템플릿: {job.job_id}")
            try:
                # JobMst에는 이미 분해(explode)되고 치환(resolve)된 단일 파라미터 대상이 영구적으로 들어있음
                resolved_params = job.params_json
                logging.info(f"  - 실행 파라미터: {resolved_params}")
                
                self.db.update_browser_job_status(job.job_id, "RUNNING")
                
                # 1. 브라우저 스크래핑 실행
                result_data = scraper.execute_job(job, resolved_params=resolved_params)
                
                if result_data:
                    # 2. 데이터 프레임 변환
                    is_scalar = True
                    for v in result_data.values():
                        if isinstance(v, list):
                            is_scalar = False
                            break
                    
                    if is_scalar:
                        df = pd.DataFrame([result_data])
                    else:
                        df = pd.DataFrame(result_data)
                    
                    logging.info(f"    추출된 데이터: {len(df)}건")
                    print(df.head())
                    
                    # 3. Output 테이블 저장 (browser_id를 기준으로 저장)
                    saved_count = self.db.insert_browser_output_data(job.browser_id, job.job_id, df)
                    logging.info(f"    ✓ 성공: {len(df)}건 (DB 저장: {saved_count}건)")
                    
                    self.db.update_browser_job_status(job.job_id, "SUCCESS")
                    success_count += 1
                else:
                    err_msg = "브라우저 스크래핑 결과 없음"
                    logging.error(f"    ✗ {err_msg}")
                    self.db.update_browser_job_status(job.job_id, "FAIL", err_msg)
                    fail_count += 1
                    
            except Exception as e:
                logging.error(f"  ✗ 브라우저 스크래핑 실행 중 오류: {e}")
                import traceback
                logging.error(traceback.format_exc())
                self.db.update_browser_job_status(job.job_id, "FAIL", str(e))
                fail_count += 1
                
        logging.info("="*80)
        logging.info(f"브라우저 스크래핑 완료: 성공 {success_count}, 실패 {fail_count}")
        logging.info("="*80)



def main():
    """메인 함수"""
    
    parser = argparse.ArgumentParser(
        description='DB 중심 KIS API 일괄 실행기',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
설명:
  DB에 'is_active=True'로 설정된 모든 프로그램을 실행합니다.
  실행 전 모든 활성 프로그램의 파라미터를 검증합니다.
  검증에 실패하는 프로그램이 하나라도 있으면 실행하지 않습니다.
        """
    )
    
    parser.add_argument("--db", default=DB_PATH, help="데이터베이스 경로 (기본값: data/kis_api.db)")
    parser.add_argument("--cycle", default=None, help="실행 주기 필터 (5min/1hour/daily)")
    
    args = parser.parse_args()
    
    # pandas 설정
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_rows', 50)
    
    try:
        # 0. 설정 로드
        from app.api.kis_config import KISConfig
        from app.api.kis_http import KISHttpClient
        
        config = KISConfig()
        
        manager = APIManager(args.db)
        
        # 1. 전체 사전 검증
        if not manager.validate_all_active_inputs(cycle=args.cycle):
            logging.error("\n[오류] 파라미터 검증에 실패하여 실행을 중단합니다.")
            sys.exit(1)
            
        logging.info("모든 파라미터 검증 완료. API 실행을 시작합니다.")
        
        # 2. 인증
        auth_manager = ka.KISAuthManager(config)
        try:
            auth_manager.authenticate()
        except Exception as e:
            logging.error(f"인증 실패: {e}")
            sys.exit(1)
            
        # 3. HTTP 클라이언트 생성
        http_client = KISHttpClient(config)
            
        # 4. API 실행 (HTTP 클라이언트 주입)
        manager.execute_active_programs(http_client, cycle=args.cycle)
        
        # 5. 브라우저 스크래핑 실행
        manager.execute_active_browser_programs(cycle=args.cycle)
    
    except Exception as e:
        import traceback
        logging.error(traceback.format_exc())
        logging.error(f"치명적 오류: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
