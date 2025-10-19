import requests
import json
import assigment3
import pandas as pd

## pandas : 데이터 분석 라이브러리. 행과 열로 이루어진 데이터 객체를 만들어 다룰수 있고, 
#           안정적으로 대용량의 데이터를 처리할 수 있다.

# print(assigment3.data)

# dataFrame = pandas.DataFrame(assigment3.data)
# print(dataFrame, "--------------변환성공------------")

data = assigment3.data["energyUseDataSummaryInfo"]
dataFrame = pd.DataFrame(data["row"])

# def : define > 함수(funciton)정의할 때 사용.
# def = 함수이름(매개변수):
def get_season(month):

    month = int(month)

    if month in [3,4,5]:
        return "봄"
    elif month in [6,7,8]:
        return "여름"
    elif month in [9,10,11]:
        return "가을"
    else:
        return "겨울"
    
dataFrame["SEASON"] = dataFrame["MON"].apply(get_season)
# dataFram.apply : 

print(dataFrame)
print("-----------변환성공-----------")

