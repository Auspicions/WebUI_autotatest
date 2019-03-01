from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import os

driver=webdriver.Chrome("./chromedriver.exe")
driver.get("http://127.0.0.1/forum.php")
driver.implicitly_wait(5)
driver.switch_to.window(driver.current_window_handle)
username=driver.find_element_by_id("ls_username")
username.send_keys("admin")
password=driver.find_element_by_id("ls_password")
password.send_keys("admin")
login=driver.find_element_by_class_name(".pn  em")
login.submit()
print("登录")
driver.implicitly_wait(5)
driver.switch_to.window(driver.current_window_handle)
moban=driver.find_element_by_link_text("默认模板")
moban.click()
driver.switch_to.window(driver.current_window_handle)
subject=driver.find_element_by_css_selector(".px")
message=driver.find_element_by_css_selector(".pt")
submit=driver.find_element_by_css_selector(".pnpost .pnc strong")
submit.click()
driver.switch_to.window(driver.current_window_handle)

huifu=("form .pt")
