import MySQLdb 
from bs4 import BeautifulSoup 
import requests



header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'} 
req = requests.get('https://www.mobis.co.kr/customer/part-info/simple-search/price/index.do?pageIndex=1&inputType=krNm&srchType=normal&hkgb=H&vtyp=P&catSeq=584402&inText=.', headers=header) # -> url로 바꾸고 포맷팅해서 페이지 변환
# 주간 차트를 크롤링 할 것임 
html = req.text 
parse = BeautifulSoup(html, 'html.parser') 

datas = parse.find("tbody").find_all("tr")

titles = datas.find_all('td'.text)
title = [] 

for t in titles: 
    title.append(t.find('a').text)
    items = [item for item in zip(title)] 
 

conn = MySQLdb.connect( user="scraper", passwd="password", host="localhost", db="scraping") # charset="utf-8"

# 커서 생성 
cursor = conn.cursor() 

# 실행할 때마다 다른값이 나오지 않게 테이블을 제거해두기 
cursor.execute("DROP TABLE IF EXISTS melon") 

# 테이블 생성하기 
cursor.execute("CREATE TABLE melon (`rank` int, title text, singer text)") 
i = 1 

# 데이터 저장하기 
for item in items: 
    cursor.execute( f"INSERT INTO melon VALUES({i},\"{item[0]}\",\"{item[1]}\")") 
    i += 1 
    
# 커밋하기 
conn.commit() 
# 연결종료하기 
conn.close()

