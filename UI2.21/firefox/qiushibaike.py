from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

dir=os.path.dirname(__file__)
chrome_driver_path =dir +"\chromedriver.exe"
driver =webdriver.Chrome(chrome_driver_path)

driver.get("https://www.qiushibaike.com/text/")
assert "糗事百科" in driver.title
driver.implicitly_wait(10)
driver.switch_to.window(driver.current_window_handle)

for a in range(0, 13):
    author_css = driver.find_elements_by_css_selector(".author h2")
    content_css = driver.find_elements_by_css_selector(".content")
    xmun_css = driver.find_elements_by_css_selector(".number")
    for i in range(0, len(author_css)):
        print("作者：",author_css[i].text, "\n内容：", content_css[i].text, "\n有", xmun_css[i].text, "人觉得好笑")
    if 0<=a<13:
        page_css = driver.find_element_by_css_selector(".next")
        page_css.click()
        print("下一页")
    else:
        driver.quit()