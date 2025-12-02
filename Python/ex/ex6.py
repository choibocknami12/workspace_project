rgb = [233,5,'아']
red,green,blue = rgb
# print(f'빨강: {red}, 초록: {green}, 파랑: {blue}')

# for _ in range(5):
    # print("Hello, Data Analysis with Open Source!")


students = [
    (20251234, '김철수', '컴퓨터과학', 2, 3.8),
    (20265678, '이영희', '생활과학부', 3, 4.2),
    (20243456, '박민수', '사회복지학과', 1, 3.5)
]

# 이름 및 성적 만 출력
for birth, name, _, _, grade in  students :

    print(f'{birth, name}의 성적: {grade}')