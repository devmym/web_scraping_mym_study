#필요라이브러리
import MySQLdb 
from bs4 import BeautifulSoup 
import requests
import numpy as np
from selenium import webdriver
import pandas as pd

#mysql 서버를 만든다.
conn = MySQLdb.connect( user="scraper", passwd="password", host="localhost", db="scraping") # charset="utf-8"

# 커서 생성 
cursor = conn.cursor() 

# 실행할 때마다 다른값이 나오지 않게 테이블을 제거해두기 
cursor.execute("DROP TABLE IF EXISTS car") 

# 테이블 생성하기 
cursor.execute("CREATE TABLE car (code text, kor text, eng text, price text)") 
i = 1 



# 요청사항 : 크롬드라이버 경로설정과 버전을 확인해주세요.
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.implicitly_wait(2)
driver.get("https://www.mobis.co.kr/customer/part-info/simple-search/price/index.do")

#로그기록
print(driver.title)
print(driver.current_url)

#필요설정
driver.find_element_by_xpath('//*[@id="frm_search"]/div/div/div[2]/ul/li[1]/div[2]/span[1]/a').click()
driver.find_element_by_xpath('//*[@id="frm_search"]/div/div/div[2]/ul/li[2]/div[2]/span[1]').click()
driver.find_element_by_xpath('//*[@id="frm_search"]/div/div/div[2]/ul/li[3]/div[2]/span[1]').click()
#차종선택 - 반복문을 통해 option[]인자를 변경
driver.find_element_by_xpath('//*[@id="catSeq"]/option[2]').click()

#키워드 입력
keyword = driver.find_element_by_xpath('//*[@id="frm_search"]/div/div/div[2]/ul/li[5]/div[2]/span/input')
keyword.send_keys('-')
driver.find_element_by_xpath('//*[@id="submit"]').click()


c_url = driver.current_url

print(c_url)


header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'} 
req = requests.get(c_url, headers=header) # -> url형태의 변수로 바꾸고 포맷팅해서 페이지 변환

# 자동차 부품 좌표 설정
html = req.text 
parse = BeautifulSoup(html, 'html.parser') 

datas = parse.find("tbody").find_all("tr")

#결과를 result 리스트에 저장
result = []

for data in datas:
    ds = data.find_all('td')
    for d in ds:
        text = d.text
        print(text)
        #차라리 이부분에서 바로바로 서버로 보낸다면 ? 
        cursor.execute('insert into module values(d)')
        i += 1


# 서버에 바로 저장 코드 추가

# 커밋하기 
conn.commit() 
# 연결종료하기 
conn.close()
