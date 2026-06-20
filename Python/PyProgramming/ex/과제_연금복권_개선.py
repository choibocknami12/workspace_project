import random

# 연금복권720+ 번호 생성기
# 구조: 1개의 '조'(1~5) + 6자리 번호(각 자리 0~9, 중복 허용)

GROUP_MIN, GROUP_MAX = 1, 5   # 조 범위
DIGIT_MIN, DIGIT_MAX = 0, 9   # 각 자리 숫자 범위
DIGIT_COUNT = 6               # 번호 자릿수


def generate_lotto():
    """연금복권 1장을 생성해 (조, 6자리숫자리스트) 튜플로 반환한다."""
    group = random.randint(GROUP_MIN, GROUP_MAX)
    # 각 자리는 서로 독립이며 중복이 가능하므로 not in 검사를 하지 않는다.
    numbers = [random.randint(DIGIT_MIN, DIGIT_MAX) for _ in range(DIGIT_COUNT)]
    return group, numbers


def format_lotto(group, numbers):
    """생성된 번호를 보기 좋은 문자열로 변환한다. 예) '3조 482917'"""
    digits = "".join(str(n) for n in numbers)
    return f"{group}조 {digits}"


def main(count=1):
    """count장 만큼 연금복권 번호를 출력한다."""
    for i in range(count):
        group, numbers = generate_lotto()
        print(f"[{i + 1}장] {format_lotto(group, numbers)}")


if __name__ == "__main__":
    main(5)   # 예시: 5장 생성
