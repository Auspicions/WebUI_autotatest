# 2. 打开 www.yahoo.com 页面,进行页面判断，在搜索输入框中，输入seleniumhq 与回车键，进行搜索。
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# # import os
# driver = webdriver.Chrome("./chromedriver.exe")
# dir = os.path.dirname(__file__)
# chrome_driver_path =dir +"\chromedriver.exe"
# val=webdriver.Chrome(chrome_driver_path)
# driver.get("https://www.yahoo.com")
# assert "yahoo" in driver.title
# elen=driver.find_element_by_name("p")
# elen.send_keys("seleniumhq" + Keys.RETURN )
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
driver = webdriver.Chrome("./chromedriver.exe")
dir=os.path.dirname(__file__)
chrome_driver_path =dir +"\chromedriver.exe"
val =webdriver.Chrome(chrome_driver_path)
try:
    driver.get("http://www.baidu.com")
    assert "百度" in driver.title

    driver.switch_to.window(driver.current_window_handle)
    search=driver.find_element_by_id("kw")
    print("百度首页已打开")
    search.send_keys("java"+ Keys.RETURN)
    search.submit()
    driver.implicitly_wait(10)

    nums=driver.find_element_by_class_name("nums")
    print("---------",nums.text)
    driver.switch_to.window(driver.current_window_handle)
    wait_seconds=10
    driver.execute_script("window.alert(\"{}, {}秒后关闭\")".format(nums.text.replace("\n", "$"), wait_seconds))
    driver.execute_script("window")
    time.sleep(wait_seconds)
finally:
    driver.quit()



print()
