
# for i in range(0, 5):
#     print("*" * (i+1))

import random

# num1 = ['1','2','3','4','5']

# print(random.choice(num1))


# num2 = ['1','2','3','4','5']

# print(random.randrange(5))

# numbers = []

# 총 6개의 숫자를 채울 때까지 반복 (range는 넉넉하게 잡거나 조건 활용)
# for i in range(100): # 중복이 나올 수 있으니 넉넉하게 반복
#     num = random.randint(0, 9)
    
    # [중요] if문으로 중복 검사
    # if num not in numbers:
    #     numbers.append(num)
    
    # 6개가 다 차면 for문을 강제로 종료(break)
#     if len(numbers) == 6:
#         break

# print(numbers)


for i in range(100):
    num = random.randint(0, 5)

print(f"{num}조")

numbers = []

for i in range(100): # 중복이 나올 수 있으니 넉넉하게 반복
    num = random.randint(0, 9)
        
    # [중요] if문으로 중복 검사
    if num not in numbers:
        numbers.append(num)
        
    # 6개가 다 차면 for문을 강제로 종료(break)
    if len(numbers) == 6:
        break
    
print(numbers)