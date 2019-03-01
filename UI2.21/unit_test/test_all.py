import unittest
import HTMLTestRunner
import os
from unit_test.abc_test import AbcTestCase
from unit_test.sort_test import SortTestCase

# 设置报文文件保存路径
cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path, "report")
if not os.path.exists(report_path):os.mkdir(report_path)

# 构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(AbcTestCase))
suite.addTest(unittest.makeSuite(SortTestCase))

if __name__=='__main__':
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)