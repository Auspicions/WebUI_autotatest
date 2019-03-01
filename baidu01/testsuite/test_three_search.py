import unittest
from selenium import webdriver
from testsuite.base_testcase import BaseTestCase
from pageobject.discuz_login import LoginPage
from framework.logger import Logger
from pageobject.discuz3_page import Login_MessageSearch3


logger=Logger(logger="BasePage").getlog()
class search_message(BaseTestCase):

    def test_search_message(self):
        # 实战三
        login_page = LoginPage(self.driver)
        search_page = Login_MessageSearch3(self.driver)

        login_page.login_page('admin', "admin")
        # 期望值是否正确
        re_haotest = search_page.message_search_page('haotest')
        try:
            print(re_haotest)
            self.assertEqual(re_haotest, "haotest", msg=re_haotest)
            logger.info('实际值与期望值一致')
            print("实际值与期望值一致")
        except:
            logger.error('实际值与期望值不一致')
            print("实际值与期望值不一致")

        login_page.end_login()
        # login_page.end_window()

if __name__=='__main__':
    unittest.main()