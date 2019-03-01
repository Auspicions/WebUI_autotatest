from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.support.wait import WebDriverWait

dir=os.path.dirname(__file__)
chrome_driver_path=dir +"./chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)
driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")
driver.implicitly_wait(10)
main_window=driver.switch_to.window(driver.current_window_handle)

while True:
    open_page = driver.find_elements_by_css_selector(".position_link h3")
    for i in range(0,1):
        open_page[i].click()
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(5)
        compyname = driver.find_element_by_css_selector(".position-head .company")
        leixing = driver.find_element_by_css_selector(".job-name .name")
        money = driver.find_element_by_css_selector(".job_request .salary")
        print("公司名称：",compyname.text)
        print("工作类型：",leixing.text)
        print("薪资：",money.text)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    page_nums = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'pager_container:last-child')))
    page_num = page_nums.get_attribute("class")
    if "pager_next_disabled" in page_num:
        break
    else:
        page_nums.click()
        time.sleep(3)

