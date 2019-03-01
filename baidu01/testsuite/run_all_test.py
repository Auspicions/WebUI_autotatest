import unittest
import HTMLTestRunner
import os
from selenium import webdriver
from testsuite.test_first_search import DiscuzSearch
from testsuite.test_second_search import Admin_Login_delmessage
from testsuite.test_three_search import search_message
from testsuite.test_four_search import Vote_message_page

# 设置报文文件保存路径
cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path, "test_report")
if not os.path.exists(report_path):os.mkdir(report_path)

#构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(DiscuzSearch))
suite.addTest(unittest.makeSuite(Admin_Login_delmessage))
suite.addTest(unittest.makeSuite(search_message))
suite.addTest(unittest.makeSuite(Vote_message_page))


if __name__=='__main__':
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告：",description="用例执行方法：")
    runner.run(suite)
