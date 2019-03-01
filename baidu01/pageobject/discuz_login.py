from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageobject.base import BasePage
import time

class LoginPage(BasePage):

    def login_page(self,username,password):        # 管理员登录
        login_page_username = (By.ID, 'ls_username')
        login_page_password = (By.ID, 'ls_password')
        login_page_button = (By.CSS_SELECTOR, ' .pn em')
        self.change_window()
        self.clear(*login_page_username)
        self.sendkeys(username, *login_page_username)
        self.clear(*login_page_password)
        self.sendkeys(password, *login_page_password)
        self.click(*login_page_button)
    def login_first_page(self):         # 进入默认板块
        first_page_moban=(By.CSS_SELECTOR,' .fl_tb h2 a')
        time.sleep(2)
        self.change_window()
        self.click(*first_page_moban)
    def login_send_page(self,mbft_title,mbft_body):         # 发帖
        send_page_title = (By.CSS_SELECTOR, '.px')
        send_page_messages=(By.CSS_SELECTOR,'.pt')
        send_page_submit=(By.CSS_SELECTOR,'.ptm .pn strong')
        time.sleep(2)
        self.sendkeys(mbft_title,*send_page_title)
        self.sendkeys(mbft_body, *send_page_messages)
        self.click(*send_page_submit)
    def login_reply_page(self,rpmsg):         # 回复帖子
        reply_page_message=(By.CSS_SELECTOR,'.area .pt')
        reply_page_submit=(By.CSS_SELECTOR,'.ptm .pn strong')
        time.sleep(2)
        self.sendkeys(rpmsg, *reply_page_message)
        self.click( *reply_page_submit)
    def end_login(self):        # 退出管理员
        closepage = (By.CSS_SELECTOR, '#um > p:nth-child(2) > a:nth-child(18)')
        time.sleep(2)
        self.change_window()
        self.click(*closepage)

    # 退出界面
    def end_window(self):
        self.driver.quite()








