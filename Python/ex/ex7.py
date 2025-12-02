import pandas as pd
data = {
"이름": ["김철수", "이영희", "박민수", "최지훈"],
"학년": [1, 2, 3, 4],
"학점": [4.2, 3.8, 4.5, 3.9],
"학과": ["컴퓨터학", "경영학", "농학", "교육학"],
"동아리": ["프로그래밍", "독서", "로봇", "봉사"]
}
df = pd.DataFrame(data)
print("index:\n", df.index)
print("\ncolumns:\n", df.columns)
print("\nvalues:\n", df.values)
print("\nrows:\n", df.values.tolist()) 