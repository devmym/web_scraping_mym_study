import MySQLdb 
from bs4 import BeautifulSoup 
import requests
import numpy as np


header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'} 
req = requests.get('https://www.mobis.co.kr/customer/part-info/simple-search/price/index.do?pageIndex=1&inputType=krNm&srchType=normal&hkgb=H&vtyp=P&catSeq=584402&inText=.', headers=header) # -> url로 바꾸고 포맷팅해서 페이지 변환
# 주간 차트를 크롤링 할 것임 
html = req.text 
parse = BeautifulSoup(html, 'html.parser') 

datas = parse.find("tbody").find_all("tr")

result = []

for data in datas:
    ds = data.find_all('td')
    for d in ds:
        text = d.text
        print(text)
        result.append(d.text)
        # print(type(text))

print(result)
print(np.shape(result))
# titles = datas.find_all('td'.text)

