import re

# re.sub(pattern, replace, text)
# test 중 pattern에 해당하는 부분을 replace로 대체한다.
def clean_text(text):

    text = "내 마음 대로 <div>test</div> 하기"
    
    if isinstance(text, str):
        text = re.sub(r'<[^>]*>','', text)
        text = re.sub(r'[^a-zA-Z0-9가-힣\s]','',text)
        # text = re.sub(r'<[^>]*>','', text)
        text = text.lower()

        return text
    else:
        return ''

# def clean_df(df):
#     if not df.empty:
#         df['정제된 제목'] = df['제목'].apply(clean_text)

print(clean_text(""))