import oracledb
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# 환경변수에서 접속 정보 읽기
USERNAME     = os.getenv("ORACLE_USER")
PASSWORD     = os.getenv("ORACLE_PASSWORD")
DSN          = os.getenv("ORACLE_DSN")
WALLET_DIR   = os.getenv("TNS_ADMIN")

# Oracle Cloud DB 접속
connection = oracledb.connect(
    user=USERNAME,
    password=PASSWORD,
    dsn=DSN,
    config_dir=WALLET_DIR,
    wallet_location=WALLET_DIR,
    wallet_password="dull6078!1"  # Wallet 비밀번호가 있으면 입력
)

print("Oracle Cloud DB 접속 성공!")
print(f"DB 버전: {connection.version}")

# 쿼리 실행 예시
cursor = connection.cursor()
cursor.execute("SELECT SYSDATE FROM DUAL")
row = cursor.fetchone()
print(f"현재 DB 시간: {row[0]}")

cursor.close()
connection.close()
print("접속 종료")