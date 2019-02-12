# -*- coding:utf-8 -*-
import unittest
import os
from HTMLTestRunner import HTMLTestRunner
"""
    
"""
case_path = os.path.join(os.getcwd())

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.discover(case_path, 'tc_*.py'))
    with open('Report.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Test Report',
                                description='generated by zsy',
                                verbosity=2)
        runner.run(suite)