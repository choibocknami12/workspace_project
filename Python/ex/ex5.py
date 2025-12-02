matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

test1_rows = matrix[:2]
# print(test1_rows)
test_columns = [row[:2] for row in matrix]
# print(test_columns)

# 리스트 슬라이싱
numbers = [10,20,30,40,50]
numbers[2:4] = [300,400]
# print(numbers)

# =====================================================================================

# 리스트 컴프리헨션
numbers2 = [i for i in range(5)]
# print(numbers2)

# 리스트 컴프리헨션 응용-값변경
# 1
numbers3 = [1,2,3,4,5]
squares = [num ** 2 for num in numbers3]
# print(squares)

# 2
numbers4 = [1, 2, 3, 4, 5]
squares = [ ]
# numbers의 모든 항목의 값을 제곱한 리스트
for num in numbers4:
  squares.append(num ** 2)

# print(squares)

# 리스트 컴프리헨션 응용-특정원소선택
# 1
numbers5 = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [num for num in numbers5 if num % 2 == 0]
# print(even_numbers)

# 2
numbers6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [ ]

# 짝수만 추출한 리스트
for num in numbers6:
    if num % 2 == 0:
        even_numbers.append(num)

# print(even_numbers)

# 리스트 컴프리헨션 응용-다중리스트 조합
# 1
list1 = ['사과','복숭아','바나나']
list2 = ['주스','잼','통조림']
pairs = [(fruit, product) for fruit in list1 for product in list2]
# print(pairs)

# 2
list1 = ['사과', '복숭아', '바나나']
list2 = ['주스', '잼', '통조림']
pairs = [ ]

# 두 리스트에 포함되 모든 원소를 조합한 투플의 리스트 생성
for fruit in list1:
    for product in list2:
        pairs.append((fruit, product))

# print(pairs)

# ===================================================================================

# 딕셔너리(키와 값이 한쌍으로 이루어진 자료형) 컴프리헨션
squares = {i: i ** 2 for i in range(5)}
# print(squares)
squares = {i: i * 2 for i in range(5)}
# print(squares)

city_population = {
    '서울': 957, '부산': 339, '인천': 294, '대구': 242, '광주': 145, '대전': 147,
    '울산': 114, '세종': 36, '수원': 115, '창원': 103, '고양': 105, '용인': 108, '성남': 94
}

# 인구 200만명 이상의 도시 리스트
large_cities = {city: pop for city, pop in city_population.items() if pop >= 200}
# print(large_cities)

# 인구 300만 이상 및 이름에 '산'이 포함된 도시 리스트
large_short_name_cities = {city: pop for city, pop in city_population.items() if pop >= 300 and '산' in city}
# print(large_short_name_cities)

# ====================================================================================

name = '아무개'
age = '25'
salary = 200
tax_rate = 0.2
basic_format = f'이름: {name}, 나이: {age}, 월급:{salary}원'
index_format = f'직원 {name}의 나이는 {age}세이고,{name}의 세후 월급은 {int(salary *(1 - tax_rate))}원입니다.'
keyword_format = f'직원정보: 이름: {name} 나이:{age}세 월급: {salary:,}원 세금:{tax_rate:.1%} 실수령액:{int(salary * (1 - tax_rate)):,}원'

print(basic_format)
print(index_format)
print(keyword_format)

# name = "최복남"
# age = 5
# print(f"이름: {name}, 나이: {age}")
# print("이름: {name}, 나이: {age}")