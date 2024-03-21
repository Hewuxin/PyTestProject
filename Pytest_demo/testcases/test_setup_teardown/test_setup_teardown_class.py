# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 13:48
# @Author  : heyuyang 
# @Project : TestProject 
# @Module  : 
# @File    : test_setup_teardown_class.py
import pytest
import requests


# 类级setup/teardown


class TestSetupTeardown:

    def setup_class(self):
        print("准备测试")

    def teardown_class(self):
        print("结束测试")

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
