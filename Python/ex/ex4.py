import re

# re.sub(pattern, replace, text)
# test 중 pattern에 해당하는 부분을 replace로 대체한다.
def clean_text(text):

    text = "내 마음 대로 <div>test</div> 하기"
    
    if isinstance(text, str):
        text = re.sub(r'<[^>]*>','', text) #3
        text = re.sub(r'[^a-zA-Z0-9가-힣\s]','',text) #1
        # text = re.sub(r'<[^>]*>','', text) #2
        # ---------------------------------------------------------
        # 교재에선 1,2 순서로 해두었지만, 그렇게되면 html코드가 지워지지않음.
        # 3,1 순서로 진행해야 깨끗한 텍스트정제가 가능함.
        # 함수사용시 리턴값 잊지말자.

        return text
    else:
        return ''

print(clean_text(""))
# 호출에러 오답노트
# print(clean_text()) : TypeError. 함수에 1개의 인자를 가지고 있으니까 꼭 추가해줘야함
# print(clean_text(text)) : NameError. 함수안에서 print한게 아니라서 text에 대한 값이 없음.