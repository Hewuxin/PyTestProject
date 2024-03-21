# -*- coding: utf-8 -*-
# @Time    : 2024/3/15 17:09
# @Author  : heyuyang 
# @Project : TestProject 
# @Module  : 
# @File    : test__fixture_function.py
import pytest
import requests


# 默认scope= function 哪个函数传入哪个函数使用
# autouse=True 所有函数都使用
@pytest.fixture(scope='function', autouse=True)
def before_login():
    print("....请求之前.....")


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


if __name__ == '__main__':
    pytest.main()
