import re

def test_patterns(text):
    # 1. ^a-zA-Z0-9가-힣\s  → 지정된 문자 외 제거
    pattern_clean = r'[^a-zA-Z0-9가-힣\s]'
    cleaned_text = re.sub(pattern_clean, '', text)

    # 2. '<[^>]*>' → HTML 태그 제거
    pattern_html = r'<[^>]*>'
    no_html_text = re.sub(pattern_html, '', text)

    print("원문:", text)
    print("① 문자 정제 결과:", cleaned_text)
    print("② HTML 태그 제거 결과:", no_html_text)


# 테스트할 텍스트
text = "Hello <b>월드</b>!! @@ 정규표현식 <div>테스트</div> 중입니다."

test_patterns(text)
