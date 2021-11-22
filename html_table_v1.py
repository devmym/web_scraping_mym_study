# 조건
# 1. 웹페이지 html 구조를 파악한다.
# 2. 반복문을 사용할 수 있는 구조인지 파악한다.
# 3. 동적/ 정적 구조 여부를 파악한다.
# 4. 웹의 데이터가 table형태인지 파악한다.

# 크롤링 가능 범위 GV70 21 관련 부품 4911개

# 필요라이브러리
import pandas as pd
import numpy as np
import csv

#필요 변수
# keyword = '엔진'

# f = open(keyword.csv, "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(f)


for i in range(1, 4):
    url = 'https://www.mobis.co.kr/customer/part-info/simple-search/price/index.do?pageIndex={}&inputType=krNm&srchType=normal&hkgb=H&vtyp=R&catSeq=584212&inText=-'.format(i)
    datas = pd.read_html(url, header= 0, encoding= 'utf-8')
    for data in datas:
        print(data)
        data.to_csv('test{}.csv'.format(i),',', encoding='utf-8-sig')
        

