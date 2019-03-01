from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageobject.base import BasePage
import time

class Vote_Message(BasePage):
    # 重新登录,进入默认模板
    # 发表投票帖子
    def send_message(self,title):
        send = (By.ID, 'newspecial')
        send_vote=(By.CSS_SELECTOR,'form div .mbw li:nth-child(2) a')
        send_vote_title=(By.CSS_SELECTOR,'.cl .z .px')
        self.click(*send)
        time.sleep(2)
        self.change_window()
        time.sleep(2)
        self.click(*send_vote)  #发起投票
        self.change_window()
        self.sendkeys(title,*send_vote_title)
    def message_number(self,msg1,msg2,msg3):   #添加帖子
        join_message1 = (By.CSS_SELECTOR, '.mbm p:nth-child(1) input')
        join_message2 = (By.CSS_SELECTOR, '.mbm p:nth-child(2) input')
        join_message3 = (By.CSS_SELECTOR, '.mbm p:nth-child(3) input')
        self.sendkeys(msg1,*join_message1)
        self.sendkeys(msg2, *join_message2)
        self.sendkeys(msg3, *join_message3)
        send_vote=(By.CSS_SELECTOR,'.pnpost .pn span')
        self.click(*send_vote)
    # 进行投票
    def vote(self):
        sel_msg_vote=(By.CSS_SELECTOR,'.pcht table tr:nth-child(1) td input')    #选择你要投的帖子
        msg_vote_button=(By.CSS_SELECTOR,'.pcht table tr:nth-last-child(1) td button span')  #提交按钮
        self.click(*sel_msg_vote)
        self.click(*msg_vote_button)
    def takout_vote(self):

        # 取出投票的主题名称
        tkout_title = (By.CSS_SELECTOR, '.ts span')
        print("投票主题：",self.find_element(*tkout_title).text)
        # 取出投票各个选项的名称以及投票比例
        tkout_name = (By.CSS_SELECTOR, '.pcht .pvt label')
        print("选项名称：",self.find_element(*tkout_name).text)
        tkout_propt = (By.CSS_SELECTOR, '.pcht table tr:nth-child(2) td:nth-child(2)')
        print("投票比例：",self.find_element(*tkout_propt).text)
