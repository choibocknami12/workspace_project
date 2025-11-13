from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()

# 브라우저 창없이 실행.(쿠팡은 헤드리스하니까 안댐. 왜..?)
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

# 드라이버실행
driver = webdriver.Chrome(options=options)

# 사이트 접속
url = "https://www.coupang.com/"
driver.get(url)
time.sleep(10)

# 제목 추출
# 경로적는거 좀 어려움. class_name등등이 있으니 쉬운방법 써도될듯..?
titles = driver.find_elements(By.XPATH, '//li[@class= "gnb-menu-item"]/a/span')

# print(titles)
for title in titles:
	print(title.text)

driver.quit