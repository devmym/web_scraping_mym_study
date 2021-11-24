# 조건
# 1. 웹페이지 html 구조를 파악한다.
# 2. 반복문을 사용할 수 있는 구조인지 파악한다.
# 3. 동적/ 정적 구조 여부를 파악한다.
# 4. 웹의 데이터가 table형태인지 파악한다.

# 크롤링 가능 범위 GV70 21 관련 부품 4911개

# 필요라이브러리
import MySQLdb 
from bs4 import BeautifulSoup 
import requests
import numpy as np
from selenium import webdriver
import pandas as pd

#필요 변수
# keyword = '엔진'

# f = open(keyword.csv, "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(f)


#mysql 서버를 만든다.

conn = MySQLdb.connect( user="scraper", passwd="password", host="localhost", db="scraping") # charset="utf-8"

# 커서 생성 
cursor = conn.cursor() 

# 실행할 때마다 다른값이 나오지 않게 테이블을 제거해두기 
cursor.execute("DROP TABLE IF EXISTS car") 

# 테이블 생성하기 
cursor.execute("CREATE TABLE car (code text, kor text, eng text, price text)") 
i = 1 



for i in range(1, 4):
    c_url = 'https://www.mobis.co.kr/customer/part-info/simple-search/price/index.do?pageIndex={}&inputType=krNm&srchType=normal&hkgb=H&vtyp=R&catSeq=584212&inText=-'.format(i)
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

            cursor.execute('insert into module values(data)')
            i += 1

