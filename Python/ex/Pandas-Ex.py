import pandas as pd

data = {
	"이름": ["홍길동", "김철수", "이영희"],
	"생일": ["1998/01/15_13:12:37", "1995/05/20_09:30:00", "1990/12/05_18:45:15"],
	"나이": [25, 28, 33],
	"직업": ["학생", "개발자", "디자이너"]
}

df = pd.DataFrame(data)
# DataFrame : 데이터를 표형태로 바꿔줌!
# print(df)

# describe 데이터프레임의 수치형 데이터에 대한 기초 통계 요약을 제공.
# 한마디로 데이터 요약에 사용.
# print(df.describe())

# to_datetime사용시 format 꼭 넣기..
# df['정규생일'] = pd.to_datetime(df['생일'], format='%Y/%m/%d_%H:%M:%S')
# print(df)

# 행순서 변경하기!
print(df.reindex([0,1,2]))

# 열순서 변경하기!
print(df.reindex(columns=['이름', '나이', '직업', '생일']))

# 이게 왜댐?
# 컬럼명이 파이썬 변수규칙을 지키면 df.column_name 형태로 접근이 가능.
# 공백x, 특문x, 숫자로시작x, pandas 내부속성과 같은 컬럼명x
print(df.이름)

# 원하는 데이터만 뽑아내기
print(df[["이름", "생일"]])

print(df["직업"][1])

# 조건 필터링도 가능
print(df['나이'] >= 27)

print((df['나이'] >= 27) & (df['나이'] <= 30))

# loc : 인덱스 기준으로 행과 열을 선택한다.
print(df.loc[0, "이름"])
