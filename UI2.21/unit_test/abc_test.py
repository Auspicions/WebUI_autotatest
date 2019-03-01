import unittest
from unit_test.abc import abc
from ddt import ddt,data,unpack

@ddt
class AbcTestCase(unittest.TestCase):
    def setup(self):
        print("开始方法测试 ")
    @data([-1,1],[1,1],[0,0])
    @unpack
    def test_abc(self, n, expect_value):
        result=abc(n)
        self.assertEqual(result,expect_value, msg=result)

    def tearDown(self):
        print("停止测试方法")
if __name__=='__main__':
    unittest.main(verbosity=2)
