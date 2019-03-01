import unittest
from selenium import webdriver
from testsuite.base_testcase import BaseTestCase
from pageobject.discuz_login import LoginPage
from pageobject.discuz4_page import Vote_Message

class Vote_message_page(BaseTestCase):
    def test_vote_message(self):
    # 实战四
            login_page = LoginPage(self.driver)
            vote_message=Vote_Message(self.driver)


            login_page.login_page('admin', "admin")
            login_page.login_first_page()
            vote_message.send_message('发起投票的主题')
            vote_message.message_number('message1','message2','message3')
            vote_message.vote()
            vote_message.takout_vote()

if __name__=='__main__':
    unittest.main()