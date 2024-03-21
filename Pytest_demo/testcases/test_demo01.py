# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 12:54
# @Author  : heyuyang 
# @Project : Pytest_demo
# @Module  : 
# @File    : test_demo01.py


def test_one():
    expect = 1
    actual = 1

    assert expect == actual


def test_two():
    expect = 1
    actual = 2

    assert expect == actual


def test_three():
    expect = "1"
    actual = 1

    assert expect == actual
