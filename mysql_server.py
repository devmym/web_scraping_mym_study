import MySQLdb 

conn = MySQLdb.connect( user="scraper", passwd="password", host="localhost", db="scraping") # charset="utf-8"

# 커서 생성 
cursor = conn.cursor() 

# 실행할 때마다 다른값이 나오지 않게 테이블을 제거해두기 
cursor.execute("DROP TABLE IF EXISTS module") 

# 테이블 생성하기 
cursor.execute("CREATE TABLE module (code text, kor text, eng text, price text)") 
i = 1 





# 커밋하기 
conn.commit() 
# 연결종료하기 
conn.close()