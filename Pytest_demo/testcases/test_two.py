# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 13:02
# @Author  : heyuyang
# @Project : Pytest_demo
# @Module  :
# @File    : test_two.py
import string


def test_less():
    assert 1 < 2


def test_more():
    assert 1 > 0


def test_equal():
    assert 1 == 1


def test_unequal():
    assert 2 != 1


def test_less_or_equal():
    assert 1 <= 2


def test_in():
    assert 'a' in 'abc'


def test_not_in():
    assert 'a' not in 'bc'


def test_is():
    assert type(1) is int


def test_not_is():
    assert type(1) is not string
