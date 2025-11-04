def sum_all(*numbers):
      result = 0
      for number in numbers:
           result += number
      return result

print(sum_all(1, 2, 3)) # 6
print(sum_all(1, 2, 3, 4, 5, 6)) # 21


student_scores = [
    ('김철수', 85, 92, 78),
    ('이영희', 92, 88, 95),
    ('박지민', 75, 83, 90)
]

for number in student_scores:
    name = number[0]
    database = number[1]
    python = number[2]
    cloud = number[3]
    average = (database + python + cloud) / 3
    print(f'{name}의 평균 점수: {average:.1f}')