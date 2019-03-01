# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com")
elements = driver.find_elements_by_tag_name("a")

print('共找到a标签%d个'%len(elements))

for ele in elements:
    print(ele.text)

driver.quit()