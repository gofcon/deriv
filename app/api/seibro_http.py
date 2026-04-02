import logging
import json
import xml.etree.ElementTree as ET
import requests
from typing import Dict, Any, Optional
from collections import namedtuple

class SeibroAPIResponse:
    """일반 API 응답 래퍼 클래스"""
    
    def __init__(self, response: requests.Response):
        self._response = response
        self._status_code = response.status_code
        self._body = self._parse_body()
    
    def _parse_body(self):
        text = self._response.text
        if not text:
            return None
            
        # [DEBUG] 원본 XML/JSON 확인을 위해 파일 저장
        try:
            with open("debug_seibro_response.xml", "w", encoding="utf-8") as f:
                f.write(text)
        except:
            pass

        try:
            # 1. JSON 체크
            json_data = self._response.json()
            if isinstance(json_data, list):
                json_data = {"data": json_data}
            BodyTuple = namedtuple("Body", json_data.keys())
            return BodyTuple(**json_data)
        except json.JSONDecodeError:
            try:
                # 2. XML 파싱 (Seibro 특화)
                root = ET.fromstring(text)
                
                # 유틸리티: 태그명 정규화 (네임스페이스 제거 + 소문자)
                def get_tag(node):
                    return (node.tag.split('}')[-1] if '}' in node.tag else node.tag).lower()

                # 유틸리티: XML 노드를 리스트/딕셔너리로 변환
                def node_to_dict(element):
                    res = {}
                    
                    # 1. 속성 수집
                    for k, v in element.attrib.items():
                        res[k.lower()] = v
                        
                    # 2. 자식 노드 순회
                    for child in element:
                        child_tag = get_tag(child)
                        child_val = node_to_dict(child)
                        
                        # 이미 속성에서 정의된 키라면 업데이트, 아니면 추가
                        if child_tag in res and isinstance(res[child_tag], dict) and isinstance(child_val, dict):
                            res[child_tag].update(child_val)
                        else:
                            res[child_tag] = child_val
                    
                    # 3. 리프 노드 처리 최적화
                    # 자식/속성이 없고 텍스트만 있는 경우
                    if not res and element.text:
                        return element.text.strip()
                    
                    # 속성이 'value' 하나만 있고 자식이 없는 경우 (Seibro 특화)
                    if len(element.attrib) == 1 and 'value' in element.attrib and not list(element):
                        return element.attrib['value']
                    
                    return res

                parsed_data = {}
                data_records = []

                # 모든 자식 노드 순회하며 메타데이터 수집 및 데이터 컨테이너 확인
                for child in root:
                    tag = get_tag(child)
                    
                    # 'data' 혹은 'outputX', 'vector', 'res' 태그가 있으면 그 내부의 'result'/'row'들을 수집
                    if tag in ('output', 'output1', 'output2', 'output3', 'data', 'res_data', 'vector', 'res'):
                        # 자식 노드들 중 'result' 또는 'row' 찾기 (표준 findall은 wildcard 미지원하므로 iter 사용)
                        results = []
                        for node in child.iter():
                            node_tag = get_tag(node)
                            if node_tag in ('result', 'row', 'item'):
                                results.append(node)
                        
                        if results:
                            for r in results:
                                data_records.append(node_to_dict(r))
                        else:
                            # 컨테이너 자체가 레코드인 경우 (단일 레코드 등)
                            node_val = node_to_dict(child)
                            if node_val:
                                data_records.append(node_val)
                    else:
                        # 일반 메타데이터 태그 (header, xdaresult 등)
                        parsed_data[tag] = node_to_dict(child)

                # 만약 위 루프에서 data_records를 하나도 못 찾았다면, 전체 트리에서 강제로 탐색 (Deep Search)
                if not data_records:
                    # 모든 하위 노드를 재귀적으로 탐색하여 result 또는 row 태그 수집
                    for node in root.iter():
                        tag = (node.tag.split('}')[-1] if '}' in node.tag else node.tag).lower()
                        if tag in ('result', 'row', 'item'):
                            # 이미 컨테이너 루프에서 수집되지 않은 경우에만 추가 (위 로직에서 수집 안되었으므로 전체 탐색)
                            data_records.append(node_to_dict(node))

                # 최종 데이터 할당
                if data_records:
                    parsed_data['data'] = data_records
                
                if not parsed_data:
                    parsed_data = {"raw_xml": text}
                    
                BodyTuple = namedtuple("Body", parsed_data.keys())
                return BodyTuple(**parsed_data)
                
            except ET.ParseError:
                return text


    def is_ok(self) -> bool:
        """HTTP 상태 코드로 성공 판단"""
        return 200 <= self._status_code < 300
        
    def get_body(self):
        return self._body

    def get_status_code(self):
        return self._status_code
        
    def get_error_message(self):
        return self._response.text

class SeibroAPIResponseError(SeibroAPIResponse):
    """에러를 래핑할 때 사용"""
    def __init__(self, status_code: int, error_text: str):
        self._status_code = status_code
        self.error_text = error_text
        self._body = None

    def is_ok(self) -> bool:
        return False
        
    def get_error_message(self):
        return self.error_text

class SeibroHttpClient:
    """Seibro 전용 HTTP 클라이언트 (세션 기반)"""
    
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.session = requests.Session()
        
    def fetch(
        self,
        api_url: str,
        api_id: str,
        header_json: dict = None,
        params: Dict[str, Any] = None,
        additional_headers: Dict[str, str] = None,
        method: str = "POST",
        use_hash: bool = False
    ):
        if params is None:
            params = {}
            
        # 기본 헤더 설정 (Postman 성공 사례 기반)
        default_referer = "https://seibro.or.kr/websquare/control.jsp?w2xPath=/IPORTAL/user/bond/BIP_CNTS03005V.xml&menuNo=88"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": default_referer,
            "Accept": "application/xml, text/xml, */*",
            "Content-Type": "application/xml"
        }
        
        if header_json:
            headers.update(header_json)
        if additional_headers:
            headers.update(additional_headers)
            
        try:
            # 세션 쿠키 확보를 위한 사전 방문 (Warm-up)
            # POST XML 요청 시에만 수행하거나, 모든 요청 전에 수행 가능
            referer_url = headers.get("Referer", default_referer)
            if self.debug:
                logging.debug(f"[Seibro Session Warm-up] Visiting {referer_url}")
            self.session.get(referer_url, headers={"User-Agent": headers["User-Agent"]})

            if method.upper() == "GET":
                response = self.session.get(api_url, params=params, headers=headers)
            elif method.upper() == "POST":
                content_type = headers.get('Content-Type', '').lower()
                
                if 'application/xml' in content_type:
                    # Parameter를 기반으로 XML Body 구축
                    action = params.get('ACTION', params.get('action', ''))
                    task = params.get('TASK', params.get('task', ''))
                    
                    # XML 선언부 없이 바로 본문 구성 (일부 레거시 서버 대응)
                    xml_body = f'<reqParam action="{action}" task="{task}">'
                    for k, v in params.items():
                        if k.upper() not in ("ACTION", "TASK"):
                            xml_body += f'<{k} value="{v}"/>'
                    xml_body += '</reqParam>'
                    
                    print("xml_body", xml_body)
                    if self.debug:
                        logging.debug(f"[Seibro POST XML] {xml_body}")
                        
                    # 세션 기반 POST (쿠키 자동 포함)
                    response = self.session.post(api_url, data=xml_body, headers=headers)
                    # print("response", response.text)
                elif 'application/json' in content_type:
                    response = self.session.post(api_url, json=params, headers=headers)
                else:
                    response = self.session.post(api_url, data=params, headers=headers)
            else:
                response = self.session.request(method.upper(), api_url, params=params, headers=headers)
                
            return SeibroAPIResponse(response)
            
        except requests.exceptions.RequestException as e:
            logging.error(f"[Seibro HTTP Error] {api_url}: {str(e)}")
            return SeibroAPIResponseError(500, str(e))
