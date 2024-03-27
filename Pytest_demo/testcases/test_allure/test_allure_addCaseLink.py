# -*- coding: utf-8 -*-
# @Time    : 2024/3/27 10:27
# @Author  : heyuyang 
# @Project : PyTestProject 
# @File    : test_allure_addCaseLink.py
# @Desc    : add link to allure report

import allure
import pytest
import requests


@allure.title("测试添加链接")
@allure.link("https://www.baidu.com", name="这是一个链接")
@pytest.mark.parametrize("url", ["https://www.baidu.com", "https://www.sina.com.cn"])
def test_add_link(url):
    response = requests.get(url)
    assert response.status_code == 200


test_case_link = "https://www.baidu.com"


@allure.title("测试添加用例管理系统链接")
@allure.testcase(test_case_link, "case manager system")
def test_case_manager():
    pass


@allure.title("测试添加用例管理系统链接{test_case_link1}")
@allure.testcase("https://www.sina.com.cn", "case manager system")
@pytest.mark.parametrize("test_case_link1", ["https://www.baidu.com", "https://www.sina.com.cn"])
def test_case_manager_with_param(test_case_link1):
    pass


@allure.title("测试添加缺陷链接")
@allure.issue(test_case_link, "issue description")
def test_with_issue():
    with allure.step(f"Step 1:request url{test_case_link}"):
        response = requests.get(test_case_link)
    with allure.step(f"Step 2:assert status_code{response.status_code}"):
        assert response.status_code == 200


