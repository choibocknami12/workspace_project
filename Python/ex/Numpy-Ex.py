import pandas as pd
import numpy as np

data = {
    "name": ["김민수", "이지영", "박준호", "최서연", "정도윤"],
    'age': [25, 30, 28, 22, 35],
    'city': ['서울', '부산', '인천', '서울', '대전'],
    'score': [90, 85, 95, 80, np.nan]
}

df = pd.DataFrame(data)
print('1. 기본 describe():')
print(df.describe())

print('\n2. 모든 데이터 타입:')
print(df.describe(include='all'))
# print(df.describe(include=[np.number]))
# print(df.describe(include=['object']))