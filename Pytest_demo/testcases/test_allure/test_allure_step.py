# -*- coding: utf-8 -*-
# @Time    : 2024/3/26 22:36
# @Author  : heyuyang 
# @Project : PyTestProject 
# @File    : test_allure_step.py
# @Desc    : 在allure报告中添加用例步骤

import allure
import pytest


@allure.step
def simple_step1(step_param):
    """定义一个测试步骤step1"""
    print(f"步骤1：打开{step_param}页面")


@allure.step
def simple_step2(step_param1, step_param2=None):
    """定义一个测试步骤step2"""
    print(f"步骤2：传入参数：参数1：{step_param1},参数2：{step_param2}")


@allure.step
def simple_step3(step_param):
    """定义一个测试步骤step3"""
    print(f"步骤3：点击按钮{step_param}进行搜索")


@allure.title("测试参数化")
@pytest.mark.parametrize("param1", ["pytest", "allure"])
def test_parametrize_wth_id(param1):
    allure.dynamic.title(f"step 测试参数化：{param1}")
    simple_step1(param1)


# 执行顺序："True,value1", "False,value1", "True,value2", "False,value2" 可知
@pytest.mark.parametrize("param1", [True, False])
@pytest.mark.parametrize("param2", ["value1", "value2"])
def test_parametrize_with_two_params(param1, param2):
    """测试step传入两个参数"""
    simple_step2(param1, param2)


@allure.title("测试不止一个步骤")
@pytest.mark.parametrize("param2", ["pytest", "unittest"])
@pytest.mark.parametrize("param1,param3", [[1, 2]])
def test_parametrize_with_uneven_value_sets(param1, param2, param3):
    simple_step1(param3)
    simple_step2(param1, param2)


@allure.title("测试打开网页{param1}搜索关键字{param2}和{param3},最后点击按钮{param4}")
@pytest.mark.parametrize("param1", ["www.baidu.com", "www.google.com"])
@pytest.mark.parametrize(("param2", "param3"), [["pytest", "WebTesting"], ["pytest", "ApiTesting"],
                                                ["unittest", "WebTesting"], ["unittest", "ApiTesting"]])
@pytest.mark.parametrize("param4", ["btn1"])
def test_three_steps(param1, param2, param3, param4):
    simple_step1(param1)
    simple_step2(param2, param3)
    simple_step3(param4)


@allure.title("测试with allure.step添加测试步骤")
@pytest.mark.parametrize("param1", ["www.baidu.com", "www.google.com"])
@pytest.mark.parametrize(("param2", "param3"), [["pytest", "WebTesting"], ["pytest", "ApiTesting"],
                                                ["unittest", "WebTesting"], ["unittest", "ApiTesting"]])
@pytest.mark.parametrize("param4", ["btn1"])
def test_with_allure_steps(param1, param2, param3, param4):
    with allure.step(f"打开网页{param1}"):
        simple_step1(param1)
    with allure.step(f"搜索关键字{param2}和{param3}"):
        simple_step2(param2, param3)
    with allure.step(f"点击按钮{param4}"):
        simple_step3(param4)


def test_with_allure_step():
    param1 = "www.baidu.com"
    param2 = "pytest"
    param3 = "WebTesting"
    param4 = "btn1"
    with allure.step(f"打开网页{param1}"):
        assert 1 == 1
    with allure.step(f"搜索关键字{param2}和{param3}"):
        assert 1 == 1
    with allure.step(f"点击按钮{param4}"):
        assert 1 == 1


@allure.title("测试with allure.step添加测试步骤")
def test_with_allure_step2():
    param1 = "www.google.com"
    param2 = "unittest"
    param3 = "ApiTesting"
    param4 = "btn2"
    with allure.step(f"打开网页{param1}"):
        assert 1 == 1
        print(f"步骤1：打开{param1}页面")
    with allure.step(f"搜索关键字{param2}和{param3}"):
        assert 1 == 1
        print(f"步骤2：传入参数：参数1：{param2},参数2：{param3}")
    with allure.step(f"点击按钮{param4}"):
        assert 1 == 1
        print(f"步骤3：点击按钮{param4}进行搜索")