# -*- coding: utf-8 -*-
# @Time    : 2024/3/16 14:37
# @Author  : heyuyang 
# @Project : TestProject 
# @File    : test_class_demo.py
# @Desc    :


class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1

