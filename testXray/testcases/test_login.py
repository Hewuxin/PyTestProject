# -*- coding: utf-8 -*-
# @Time    : 2024/3/16 15:45
# @Author  : heyuyang 
# @Project : TestProject 
# @File    : test_login.py
# @Desc    :
import pytest
import allure


def read_yam():
    return ['何', '雨', '阳']


class TestUser:
    @allure.title("测试login")
    def test_login(self):
        print("login")

    def test_register(self):
        print("register: ")

    def test_logout(self):
        print("logout")
