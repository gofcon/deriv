from playwright.sync_api import sync_playwright
import time
import os
import http.client
import requests

def run():

    conn = http.client.HTTPSConnection("seibro.or.kr")
    payload = "<reqParam action=\"searchBondDepthContentList\" task=\"ksd.safe.bip.cmuc.User.process.SearchPTask\"><SECN_KACD value=\"\"/><SECN_DTAIL_KACD value=\"110210\"/></reqParam>"
    headers = {
    'Referer': 'https://seibro.or.kr/websquare/control.jsp?w2xPath=/IPORTAL/user/bond/BIP_CNTS03005V.xml&menuNo=88',
    'Content-Type': 'application/xml',
    'Cookie': 'JSESSIONID=4u9CnwnpxVYKqFzXB6n7EKKaCT7oPmpRDyFwgYYzoh8X0373UQ_C!-1970389529; WMONID=G0YNukR-gCW'
    }
    conn.request("POST", "/websquare/engine/proworks/callServletService.jsp", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


    url = "https://seibro.or.kr/websquare/engine/proworks/callServletService.jsp"
    payload = "<reqParam action=\"searchBondList\" task=\"ksd.safe.bip.cmuc.User.process.SearchPTask\"/>"
    headers = {
    'Referer': 'https://seibro.or.kr/websquare/control.jsp?w2xPath=/IPORTAL/user/bond/BIP_CNTS03005V.xml&menuNo=88',
    'Content-Type': 'application/xml; charset="UTF-8"',
    'Accept': 'application/xml',
    'Cookie': 'JSESSIONID=rwhCulmQFSG986aEvOeuQS2hfuXaD5v7q5iishJgAxKkR4ugiuPN!-1970389529; WMONID=G0YNukR-gCW'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == "__main__":
    run()
