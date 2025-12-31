import requests
import json

# 파라미터에 월별 변경하기
basic_url = "http://openapi.seoul.go.kr:8088/724d474575676c6736366745714841/json/energyUseDataSummaryInfo/1/5/{}/{}"

# 년도 설정 : range() > 끝 숫자는 범위에 포함되지 않음. 그래서 2015~2025로 설정.
years = range(2015, 2025)
# 월별 설정 : range() > 끝 숫자는 범위에 포함되지 않음. 그래서 1~13으로 설정.
months = range(1, 13) 

for year in years:
    for month in months:
        # f"문자열 {변수명 or 표현식}"
        formatted_month = f"{month:02d}"

        # str.format() : 문자열 {자리}, format(값)
        url = basic_url.format(year, formatted_month)

        # 요청 보내기
        response = requests.get(url)
        print(f"요청 URL: {response.url}")

    if response.status_code == 200:
            
            data = response.json()
            print(json.dumps(data, indent=4),"-------------출력성공-------------")
            # print(f"{year}-{formatted_month} 데이터 수신 완료")

    else:
            print(f"{year}-{formatted_month} 요청 실패: {response.status_code}")