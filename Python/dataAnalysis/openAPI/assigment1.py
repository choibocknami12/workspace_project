import requests
import json
#import xml.etree.ElementTree as ET
# from urllib.parse import urlencode

url = "http://openapi.seoul.go.kr:8088/724d474575676c6736366745714841/json/energyUseDataSummaryInfo/1/5/2015/01"
# params = {
#     "myKey" : "724d474575676c6736366745714841",
# }

response = requests.get(url)
# print(response.text)

if response.status_code == 200:
    print("-------요청성공------")

    # data = response.text
    data = json.loads(response.text)
    # json.loads(json_string) : json 문자열 > 파이썬 객체로 바꿈
    print(json.dumps(data, indent=4))
    # json.dumps(python_object, indent=4) : 파이썬 객체 > json 문자열로 바꿔줌.

else:
    print("XXXX요청실패XXXX",response.status_code == 400)