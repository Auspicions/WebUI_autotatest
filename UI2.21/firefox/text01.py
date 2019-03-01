from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

dir=os.path.dirname(__file__)
chrome_driver_path=dir +"\chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)
# try:
#     driver.get("http://www.baidu.com")
#     assert "百度" in driver.title
#     driver.switch_to.window(driver.current_window_handle)
#     eles=driver.find_elements_by_tag_name("a")
#     print('共找到a标签%d个' % len(eles))
#     for ele in eles:
#         print(ele.text)
# finally:
#     driver.quit()

try:
    driver.get("http://www.baidu.com")
    assert "百度" in driver.title

    driver.switch_to.window(driver.current_window_handle)
    about_list = driver.find_element_by_link_text("关于百度")
    print("打开关于百度")
    about_list.click()

    driver.implicitly_wait(10)
    driver.switch_to.window(driver.current_window_handle)
    classl=driver.find_element_by_link_text("联系我们")
    print("打开联系我们")
    emil_list=driver.find_elements_by_link_text("emil_content_text")
    print("找到所有的邮箱 ")
    for i in emil_list:
        str = i.text
        if "@" in str:
            print(str)

finally:
    driver.quit()
