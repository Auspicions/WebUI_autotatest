from selenium import webdriver
import os

dir =os.path.dirname(__file__)
chrome_driver_path=dir +"./chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)
driver.get("https://www.qiushibaike.com/text")
assert "糗事百科"in driver.title
driver.implicitly_wait(10)
driver.switch_to.window(driver.current_window_handle)

while True :
    author_css = driver.find_elements_by_css_selector(".author h2")
    content_css = driver.find_elements_by_css_selector(".content")
    xmun_css = driver.find_elements_by_css_selector(".number")
    for i in range(0, len(author_css)):
        print("作者：", author_css[i].text, "\n内容：", content_css[i].text, "\n有", xmun_css[i].text, "人觉得好笑")
        page = driver.find_element_by_css_selector(".next").text == "下一页"

    if page==".next":
        page.click()

    else:
        print("这是最后一页")
        driver.quit()
