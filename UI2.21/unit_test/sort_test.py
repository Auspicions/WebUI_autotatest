import unittest
from ddt import ddt,data,unpack
from unit_test.sort import sort

@ddt
class SortTestCase(unittest.TestCase):
    def setup(self):
        print("dhjfkfl--------------")
    @data([0,0,0],[1,0,2],[1,1,10],[1,2,20])
    @unpack
    def test_sort(self,x,y,expect_value):
        result=sort(x,y)
        self.assertAlmostEqual(result,expect_value, msg=result)

    def tearDown(self):
        print("**************__________")
if __name__=='__main__':
    unittest.main(verbosity=2)