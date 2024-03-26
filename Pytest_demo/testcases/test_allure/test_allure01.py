# -*- coding: utf-8 -*-
# @Time    : 2024/3/26 21:19
# @Author  : heyuyang 
# @Project : PyTestProject 
# @File    : test_allure01.py
# @Desc    :  allure testcase practice1,实现给测试报告添加用例标题


import allure
import pytest


@pytest.fixture(scope="session", autouse=True)
def init_allure():
    """
    初始化allure
    :return:
    """
    print("执行前置清理")
    yield "a"
    print("执行后置清理")


@allure.title("allure practice")
class TestApi:
    """
    测试API接口
    """

    @allure.title("登录功能")
    def test_login(self):
        assert 1 == 1
        print("登录功能测试通过")

    def test_get_student_info(self):
        assert 1 == 1
        print("获取学生信息测试通过")

    def test_create_student(self):
        assert 1 == 1
        print("创建学生测试通过")

    @allure.title("获取全部学生信息")
    def test_select_all_student(self):
        assert 1 == 1
        print("获取全部学生信息测试通过")


@allure.title("身份验证")
def test_authentication():
    assert 1 == 1
    print("身份验证成功")


def test_title():
    """
    直接使用@allure.title装饰器
    :return:
    """
    assert True


@allure.title("参数化用例标题:参数1:{p1},参数2:{p2}")
@pytest.mark.parametrize("p1,p2,p3", [(1, 2, 3), (3, 4, 7)])
def test_with_title(p1, p2, p3):
    tmp = p1 + p2
    assert tmp == p3


@allure.title("原始标题")
@pytest.mark.parametrize("p1", ["参数化标题1", "参数化标题2", "参数化标题3"])
def test_dynamic_title(p1):
    assert True
    print("原始标题")
    allure.dynamic.title(p1)
