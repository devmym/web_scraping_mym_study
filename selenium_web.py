from selenium import webdriver 
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver") 
driver.implicitly_wait(3)
driver.get("https://www.i-kapa.org/search?page=1") 

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath('//*[@id="detailTable"]/tbody/tr[9]').click()
driver.find_element_by_xpath('//*[@id="detailTable"]/tbody/tr[9]').click()


