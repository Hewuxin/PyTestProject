# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 13:39
# @Author  : heyuyang 
# @Project : Pytest_demo
# @Module  : 
# @File    : test_setup_teardown_module.py

import requests


# 模块级setup/teardown

def setup_module():
    print("准备测试")


def teardown_module():
    print("结束测试")


def test_xray_availability():
    url = 'http://10.21.25.54:3000/'
    params = {
        'name': 'heyuyang',
        'password': 'heyuyang'
    }
    response = requests.get(url, params)
    assert response.status_code == 200
    print("请求的url是: ", response.url)


def test_baidu_availability():
    url = 'https://www.baidu.com'

    response = requests.get(url)

    assert response.status_code == 200
    print("请求的url是:", response.url)
