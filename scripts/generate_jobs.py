import os
import sys
import argparse
import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import DatabaseManager
from app.utils.macros import resolve_macros, explode_params
from scripts.log_setup import setup_logging

def generate_api_jobs(db: DatabaseManager, base_yymm: str):
    schedules = db.list_active_api_schedule_msts()
    if not schedules:
        return 0

    job_count = 0
    
    for sch in schedules:
        # 삭제 대신 기존 해당 스케줄로 생성되었던 Job 대상들을 모두 비활성화
        db.deactivate_api_jobs_by_schedule(sch.schedule_id)
        
        param_combinations = explode_params(sch.macro_params_json)
        
        for i, param_combo in enumerate(param_combinations):
            resolved = resolve_macros(param_combo)
            job_id = f"{sch.schedule_id}_{base_yymm}_{i:03d}"
            
            db.add_api_job_mst(
                job_id=job_id,
                api_id=sch.api_id,
                params=resolved,
                description=f"Generated from {sch.schedule_id}",
                is_active=True,
                save_mode=sch.save_mode,
                execution_cycle=sch.execution_cycle,
                schedule_id=sch.schedule_id,
                status="READY",
                base_yymm=base_yymm
            )
            job_count += 1
            
    return job_count

def generate_browser_jobs(db: DatabaseManager, base_yymm: str):
    schedules = db.list_active_browser_schedule_msts()
    if not schedules:
        return 0

    job_count = 0
    
    for sch in schedules:
        # 삭제 대신 기존 해당 스케줄로 생성되었던 Job 대상들을 모두 비활성화
        db.deactivate_browser_jobs_by_schedule(sch.schedule_id)
        
        param_combinations = explode_params(sch.macro_params_json)
        
        for i, param_combo in enumerate(param_combinations):
            resolved = resolve_macros(param_combo)
            job_id = f"{sch.schedule_id}_{base_yymm}_{i:03d}"
            
            db.add_browser_job_mst(
                job_id=job_id,
                browser_id=sch.browser_id,
                params=resolved,
                description=f"Generated from {sch.schedule_id}",
                is_active=True,
                save_mode=sch.save_mode,
                execution_cycle=sch.execution_cycle,
                schedule_id=sch.schedule_id,
                status="READY",
                base_yymm=base_yymm
            )
            job_count += 1
            
    return job_count

def main():
    parser = argparse.ArgumentParser(description="Generate execution jobs from scheduled macros.")
    parser.add_argument("--base_yymm", default=None, help="Base Year Month YYYYMM (default: current month)")
    args = parser.parse_args()
    
    setup_logging()
    db = DatabaseManager()
    
    # 기본값을 "이전 달(last month)"로 설정하여 매크로({last_month_start} 등)와 일치시킴
    default_base_yymm = (datetime.now() - relativedelta(months=1)).strftime("%Y%m")
    base_yymm = args.base_yymm or default_base_yymm
    
    logging.info("="*60)
    logging.info(f"Generating All Jobs from Active Schedules for base_yymm: {base_yymm}...")
    logging.info("="*60)
    
    api_count = generate_api_jobs(db, base_yymm)
    browser_count = generate_browser_jobs(db, base_yymm)
    
    logging.info(f"Job Generation Complete:")
    logging.info(f" - API Jobs Queued: {api_count}")
    logging.info(f" - Browser Jobs Queued: {browser_count}")
    logging.info("="*60)

if __name__ == "__main__":
    main()
