import unittest
from testsuite.base_testcase import BaseTestCase
from pageobject.baidu_homepage import HomePage
class BaiduSearch(BaseTestCase):
    def test_baidu_search(self):
        home_page=HomePage(self.driver)
        home_page.search('selenium')

if __name__=='__main__':
    unittest.main()
