from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
    def forward(self):
        self.driver.forward()
    def open_url(self,url):
        self.driver.get(url)
    def quit_browser(self):
        self.driver.quit()
    def close(self):
        self.driver.close()
        print("关闭")
    def send_keys(self):
        self.driver.send_keys()
    def clear(self):
        self.driver.clear()
    def click(self):
        self.driver.click()
    def find_element(self,*loc):    #显示等待找到页面元素
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        print("找到页面元素")
        return self.driver.find_element(*loc)
    # 窗口截屏的存放位置
    def get_window_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq=time.strftime('%Y%m%d%H%N',time.localtime(time.time()))
        screen_name=file_path +rq +'.png'
        self.driver.get_screenshort_as_file(screen_name)

