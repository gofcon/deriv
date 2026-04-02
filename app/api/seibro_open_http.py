import logging
import requests
import urllib.parse
from typing import Dict, Any

from app.api.seibro_http import SeibroAPIResponse, SeibroAPIResponseError

class SeibroOpenHttpClient:
    """SEIBRO Open API 전용 HTTP 클라이언트
    GET 방식으로 호출하며, params을 'KEY:VALUE,KEY:VALUE' 형식의 텍스트로 직렬화하여 전달합니다.
    """
    
    def __init__(self, key: str, base_url: str, debug: bool = False):
        self.key = key
        self.base_url = base_url
        self.debug = debug

    def fetch(
        self,
        api_id: str,
        params: Dict[str, Any] = None,
        header_json: dict = None,
        additional_headers: Dict[str, str] = None,
        method: str = "GET",
        use_hash: bool = False
    ) -> SeibroAPIResponse:
        
        if not self.key:
            logging.error("SEIBRO_KEY is not configured.")
            return SeibroAPIResponseError(500, "SEIBRO_KEY is missing")

        if params is None:
            params = {}

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://seibro.or.kr/",
            "Accept": "application/xml, text/xml, */*"
        }
        if header_json:
            headers.update(header_json)
        if additional_headers:
            headers.update(additional_headers)

        # 직렬화: {"ISIN": "KR6268761881"} -> "ISIN:KR6268761881"
        param_list = []
        for k, v in params.items():
            if v is not None and str(v).strip():
                param_list.append(f"{k}:{v}")
        serialized_params = ",".join(param_list)

        # 쿼리 파라미터 빌드
        # apiId는 실제 호출하려는 Open API 식별자입니다 (GetBondStatInfo 등). 
        # api_def.api_name 값 등을 apiId 로 취급할 것이므로 여기선 api_id 파라미터로 받습니다.
        # 주의: 우리 DB의 api_id는 'seibro_getBondStatInfo' 같은 형태일 수 있으니, 
        # 실제 Seibro apiId는 파라미터에서 추출하거나 api_id 에서 추출하도록 약속합니다.
        # 이번 구현에서는 `main.py` 측에서 파싱된 `api_def.api_name`을 넘겨주기로 합니다 (예: getBondStatInfo)

        # 쿼리 파라미터 빌드 (주의: Seibro는 콜론(:) 인코딩 여부에 민감할 수 있으므로 수동으로 URL 조립)
        full_url = f"{self.base_url}?key={self.key}&apiId={api_id}&params={serialized_params}"

        try:
            if self.debug:
                logging.debug(f"[SeibroOpenHttpClient] GET {full_url}")

            response = requests.get(full_url, headers=headers)
            return SeibroAPIResponse(response)

        except requests.exceptions.RequestException as e:
            error_msg = f"[SeibroOpen HTTP Error] {self.base_url}: {str(e)}"
            logging.error(error_msg)
            return SeibroAPIResponseError(500, str(e))
