import unittest
from functiontest.mymodule import mySum

'''
python 单元测试模块
'''

# 定义一个单元测试类，继承unittest.TestCase
class MyTest(unittest.TestCase):

    # 重写内置函数setUp，在测试开始时调用，以实现必要的功能
    def setUp(self):
        print("单元测试开始时调用")

    # 重写内置方法tearDown, 在测试结束时调用
    def tearDown(self):
        print("单元测试结束时调用")

    # 对应函数的单元测试方法， 在被测试函数名前加test_
    def test_mySum(self):

        # 进行等值断言，按照方法的预期结果给出预定结果，以及不符合预期结果的返回信息
        self.assertEqual(mySum(5, 4), 9, "加法函数mySum逻辑有误")


if __name__ == "__main__":

    # 执行测试
    unittest.main()

