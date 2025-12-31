import requests
import json
#import xml.etree.ElementTree as ET
# from urllib.parse import urlencode

url = "http://openapi.seoul.go.kr:8088/sample/xml/SearchFAQClassListService/1/5/%20/%20/"
params = {
    "myKey" : "인증완료",
}

response = requests.get(url, params=params)
print(response.content)


if response.status_code == 200:
    print("-------요청성공------")

    # data = response.text
#     parsed = json.loads(response.text)
#     print(json.dumps(parsed, indent=4))

# else:
#     print("XXXX요청실패XXXX",response.status_code == 400)