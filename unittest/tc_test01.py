# -*- coding: utf-8 -*-
import unittest
import os

"""
    测试用例
"""

__auther__ = 'Duome'

class TestCaseDemo(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(1, 1, '1 == 1')
    def test_true(self):
        self.assertTrue(1==1, '1==1')
