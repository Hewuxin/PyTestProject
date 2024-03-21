# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 13:08
# @Author  : heyuyang 
# @Project : Pytest_demo
# @Module  : 
# @File    : test_requests_get.py
import requests


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
