number = range(1,11)
prod = ['H', 'K']
sort = ['R', 'P', 'C']

for p in prod:
    for s in sort:
        for n in number:
            url = 'https://www.mobis.co.kr/customer/part-info/simple-search/price/index.do?pageIndex={}&inputType=krNm&srchType=normal&hkgb={}&vtyp={}&catSeq=584402&inText=.'.format(n, p, s)
            print(url)
            

