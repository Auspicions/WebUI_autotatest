import unittest
from selenium import webdriver
from testsuite.base_testcase import BaseTestCase
from pageobject.discuz_login import LoginPage
from pageobject.discuz2_page import Login_AdminUsername2

class Admin_Login_delmessage(BaseTestCase):
    # 实战二
    def test_adminLogin_delmessage(self):

        login_page = LoginPage(self.driver)
        admin_page = Login_AdminUsername2(self.driver)

        login_page.login_page('admin', "admin")
        login_page.login_first_page()
        admin_page.del_message_page()
        admin_page.admin_page()
        # admin_page.admin_page('admin')

        admin_page.new_block_page('自动化测试')
        login_page.end_login()
        login_page.login_page('chen','chen')
        admin_page.new_block_message()
        login_page.login_send_page('普通用户发帖标题','普通用户发帖内容%……&**——————————————')
        login_page.login_reply_page('普通用户回帖。。。。。。')

if __name__=='__main__':
    unittest.main()