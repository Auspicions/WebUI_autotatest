import unittest
import os
from unit_test.abc_test import AbcTestCase
from unit_test.sort_test import SortTestCase

# 手动测试
# 构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(AbcTestCase))
suite.addTest(unittest.makeSuite(SortTestCase))

if __name__=='__main__':
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
