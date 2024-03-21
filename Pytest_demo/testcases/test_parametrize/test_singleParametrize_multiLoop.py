# -*- coding: utf-8 -*-
# @Time    : 2024/3/15 18:08
# @Author  : heyuyang 
# @Project : TestProject
# @File    : test_singleParametrize_multiLoop.py
# @Desc    : single params multiple loop practice
import pytest

from Pytest_demo.testcases.test_parametrize.test_singleParametrize_singleLoop import login_check


@pytest.mark.parametrize("name", ["hyy", "hwx", "heyuyang"])
def test_login(name):
    result = login_check(name)
    assert result is not None


if __name__ == '__main__':
    pytest.main(['-vs'])
