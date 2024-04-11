# -*- coding: utf-8 -*-
# @Time    : 2024/3/15 21:58
# @Author  : heyuyang 
# @Project : TestProject 
# @File    : conftest.py
# @Desc    :
import pytest

from PytestBasic.common.yaml_utils import clear_yaml


@pytest.fixture(scope="session", autouse=False)
def a_assert():
    print("在用例之前执行：select database for assert")
    yield "a"
    print("在用例之后执行：select database for assert")


@pytest.fixture(scope="session", autouse=True)
def exe_assert():
    print("clear yaml")
    clear_yaml()


@pytest.fixture(scope="function")
def login():
    print("执行登录")
