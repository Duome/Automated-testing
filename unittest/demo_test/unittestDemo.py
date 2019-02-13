# -*- coding: utf-8 -*-
__Author__ = 'Duome'
import unittest
from moduleDemo import Calculator
"""
    一个testcase的实例就是一个测试用例，
    但是多个以test开头的方法，每一个方法，在load的时候会生成一个testcase实例
    一个完整的测试流程，包括准备环境搭建（setUP）执行测试代码（run）环境还原（tearDown）
    setup和teardown是每个实例前后都会运行
    “测试驱动开发”（TDD：Test-Driven Development）
"""

class ModuleTest(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.cal = Calculator(8, 4)

    def tearDown(self):
        # 不管写到哪里都是最后一个执行
        print("tearDown")
        pass

    def test_add(self):
        result = self.cal.add()
        print("add 12")
        self.assertEqual(result, 12)

    # def test_sub(self):
    #     result = self.cal.sub()
    #     print("sub 4")
    #     self.assertEqual(result, 4)
    #
    # def test_mul(self):
    #     result = self.cal.mul()
    #     print("mul 32")
    #     self.assertEqual(result, 32)
    #
    # def test_div(self):
    #     result = self.cal.div()
    #     print("div 2")
    #     self.assertEqual(result, 2)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            # 检测异常，如果没有发生异常则报错
            print('before raise can print')
            s.split(2)
            print('behind raise can not print,if not raise can print')

if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest('test_add'))
    suite.addTest(ModuleTest('test_sub'))
    suite.addTest(ModuleTest('test_mul'))
    suite.addTest(ModuleTest('test_div'))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

