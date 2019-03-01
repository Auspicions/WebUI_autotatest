import unittest
from selenium import webdriver
from testsuite.base_testcase import BaseTestCase
from pageobject.discuz_login import LoginPage


class DiscuzSearch(BaseTestCase):

    def test_login_search(self):
        login_page = LoginPage(self.driver)
        login_page.login_page('admin',"admin")
        login_page.login_first_page()
        login_page.login_send_page('默认模板发帖标题','默认模板发帖内容，。。，。，。。，，。')
        login_page.login_reply_page('默认模板回帖！！！！！！！！！')
        login_page.end_login()

if __name__ == '__main__':
    unittest.main(verbosity=2)