import MySQLdb 
from bs4 import BeautifulSoup 
import requests
import numpy as np


number = range(1,4)
prod = ['H', 'K']
sort = ['R', 'P', 'C']

for p in prod:
    for s in sort:
        for n in number:
            url = 'https://www.mobis.co.kr/customer/part-info/simple-search/price/index.do?pageIndex={}&inputType=krNm&srchType=normal&hkgb={}&vtyp={}&catSeq=584270&inText=.'.format(n, p, s)
            print(url)

            # header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'} 
            req = requests.get(url) # -> url로 바꾸고 포맷팅해서 페이지 변환
            
            # 자동차 부품 클롤링
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