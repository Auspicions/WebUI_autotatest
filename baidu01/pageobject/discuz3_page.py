from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageobject.base import BasePage
import time

class Login_MessageSearch3(BasePage):
    # 用户登录
    # 进行帖子搜索,搜索haotest帖子,进入搜索的帖子
    def message_search_page(self,search_inmessage):
        input_message_title=(By.CSS_SELECTOR,'.scbar_txt_td input')
        search_message_page = (By.CSS_SELECTOR, '.scbar_btn_td button')
        self.change_window()
        time.sleep(2)
        self.clear(*input_message_title)
        self.sendkeys(search_inmessage, *input_message_title)
        time.sleep(5)
        self.click(*search_message_page )
        # 验证帖子标题和期望的一致
        self.change_window()
        haotest_title=(By.CSS_SELECTOR,'.pbw .xs3 font')
        self.click(*haotest_title)
        time.sleep(2)
        self.change_window()
        find_haotest=(By.CSS_SELECTOR,'.ts span')
        time.sleep(10)
        print("haotest主题：", self.find_element(*find_haotest).text)
        re_haotest=self.find_element(*find_haotest).text
        return re_haotest
    # 用户退出
    # 退出界面