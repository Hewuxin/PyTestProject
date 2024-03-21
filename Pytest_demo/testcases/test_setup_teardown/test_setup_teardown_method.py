# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 13:54
# @Author  : heyuyang 
# @Project : TestProject 
# @Module  : 
# @File    : test_setup_teardown_method.py
import pytest
import requests


# method setup/teardown

class TestSetupTeardown:

    def setup_method(self):
        print("准备method测试\n")

    def teardown_method(self):
        print("结束method测试")

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
