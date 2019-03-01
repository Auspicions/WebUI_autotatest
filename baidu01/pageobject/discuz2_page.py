from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageobject.base import BasePage
import time

class Login_AdminUsername2(BasePage):
    # 管理员用户登录
    # 进入默认板块
    # 选择要删除的帖子,并单击删除
    def del_message_page(self):
        sel_del_message=(By.CSS_SELECTOR,'form table tbody tr .o input')
        del_message = (By.CSS_SELECTOR, 'form div  p strong a')
        confirm_button=(By.CSS_SELECTOR, '.o .pn span')
        time.sleep(2)
        self.change_window()
        self.click(*sel_del_message)
        time.sleep(2)
        self.click(*del_message)
        time.sleep(2)
        self.click(*confirm_button)
    # 进入版块管理(管理中心 - -论坛)
        adminpage = (By.LINK_TEXT, '管理中心')
        self.click(*adminpage)
    def admin_page(self):
        # psw_page=(By.CSS_SELECTOR,'.loginform .txt')       # 重新登录
        # admin_submit=(By.CSS_SELECTOR,'.loginnofloat .btn')
        click_discuz = (By.ID, 'header_forum')     # 进入论坛

        self.change_window()
        time.sleep(5)
        # self.clear(*psw_page)
        # self.sendkeys(cx_psw,*psw_page)   # 重新登录
        # time.sleep(2)
        # self.click( *admin_submit)
        time.sleep(10)
        self.change_window()
        self.click(*click_discuz)
    # 创建新的版块
    def new_block_page(self,newblock):
        new_block=(By.CSS_SELECTOR,'.lastboard .addtr')  #添加新板块
        new_block_name=(By.NAME,'newforum[1][]')  #创建新的板块
        new_block_submit=(By.CSS_SELECTOR,'.fixsel .btn')     #提交
        time.sleep(5)
        self.change_window()
        self.enter_iframe()
        self.click(*new_block)
        time.sleep(5)
        time.sleep(2)
        self.clear(*new_block_name)
        self.sendkeys(newblock, *new_block_name)
        self.click(*new_block_submit)
        close_new_page = (By.CSS_SELECTOR, '.uinfo a')  # 关闭新的页面
        time.sleep(5)
        self.change_window()
        self.click(*close_new_page)
    # 管理员退出
    # 普通用户登录
    # 在新的版块下发帖
    def new_block_message(self):
        new_block = (By.CSS_SELECTOR, '.fl_tb  tr:nth-last-child(2) td h2 a')
        time.sleep(2)
        self.click(*new_block)
    # 发帖
    # 回复帖子