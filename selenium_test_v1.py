from selenium import webdriver
import pandas as pd


driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(2)
driver.get("https://www.mobis.co.kr/customer/part-info/simple-search/price/index.do")

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath('//*[@id="frm_search"]/div/div/div[2]/ul/li[1]/div[2]/span[1]/a').click()
driver.find_element_by_xpath('//*[@id="frm_search"]/div/div/div[2]/ul/li[2]/div[2]/span[1]').click()
driver.find_element_by_xpath('//*[@id="frm_search"]/div/div/div[2]/ul/li[3]/div[2]/span[1]').click()
driver.find_element_by_xpath('//*[@id="catSeq"]/option[2]').click()

keyword = driver.find_element_by_xpath('//*[@id="frm_search"]/div/div/div[2]/ul/li[5]/div[2]/span/input')
keyword.send_keys('-')
driver.find_element_by_xpath('//*[@id="submit"]').click()



