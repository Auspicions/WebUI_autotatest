from selenium import webdriver
import unittest
from framework.browser_engine import BrowserEngine

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser=BrowserEngine()
        self.driver=browser.open_browser()

        # self.driver=webdriver.Chrome("../text_baidu/tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
    def tearDown(self):
        self.driver.quit()
        # self.driver.quit()
