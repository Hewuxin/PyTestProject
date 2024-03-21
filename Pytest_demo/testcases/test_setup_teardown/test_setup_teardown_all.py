# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 14:04
# @Author  : heyuyang 
# @Project : TestProject 
# @Module  : 
# @File    : test_setup_teardown_all.py

# 所有setup/teardown嵌套

import pytest
import requests


def setup_module():
    print(">>>>>准备module测试\n")


def teardown_module():
    print("结束module测试<<<<<")


def setup_function():
    print(">>>>>准备function测试\n")


def teardown_function():
    print("结束function测试<<<<<")


def test_post():
    assert 1 == 1


class TestSetupTeardown:

    def setup_class(self):
        print(">>>>>准备class测试\n")

    def teardown_class(self):
        print("结束class测试<<<<<")

    def setup_method(self):
        print(">>>>>准备method测试\n")

    def teardown_method(self):
        print("结束method测试<<<<<")

    def test_xray_availability(self):
        url = 'http://10.21.25.54:3000/'
        params = {
            'name': 'heyuyang',
            'password': 'heyuyang'
        }
        response = requests.get(url, params)
        assert response.status_code == 200
        print("请求的url是: ", response.url)

    def test_baidu_availability(self):
        url = 'https://www.baidu.com'

        response = requests.get(url)

        assert response.status_code == 200
        print("请求的url是:", response.url)


if __name__ == '__main__':
    pytest.main(["-vs"])
