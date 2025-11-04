number = int(input('정수를 입력하세요: '))

# try 문
try:
    result = 10 / number
    print(f'결과: {result}')

# except 문
except:
    print('0으로 나눌 수 없습니다.')