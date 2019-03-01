from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import os
import time
from selenium.webdriver.support.wait import WebDriverWait

logger=Logger(logger="BasePage").getlog()
class BasePage(object) :
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")
    def open_url(self,url):
        self.driver.get(url)
    def quit_browser(self):
        self.driver.quit()
    def close(self):
        self.driver.close()
        print("关闭")
    def find_element(self,*loc):
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located(loc))
        ele=self.driver.find_element(*loc)
        print("找到页面元素")
        return ele
    def change_window(self):
        window_list=self.driver.window_handles
        self.driver.switch_to.window(window_list[len(window_list)-1])

    def get_window_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq=time.strftime('%Y%m%d%H%N',time.localtime(time.time()))
        screen_name=file_path +rq +'.png'
        self.driver.get_screenshort_as_file(screen_name)

    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        # el.clear()
        el.send_keys(text)
        print("输入内容")
    def clear(self,*loc):
        el=self.find_element(*loc)
        el.clear()
        logger.info("Clear text in input box defore typing.")
    def click(self,*loc):
        el=self.find_element(*loc)
        el.click()
        logger.info("The element %s was clicked.")
    def enter_iframe(self):
        self.driver.switch_to.frame(0)

