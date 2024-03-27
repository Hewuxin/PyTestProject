# -*- coding: utf-8 -*-
# @Time    : 2024/3/27 10:54
# @Author  : heyuyang 
# @Project : PyTestProject 
# @File    : test_allure_addCaseClass.py
# @Desc    : 可以为项目，以及项目下的不同模块对用例进行分类管理。

import allure
import pytest


@pytest.fixture(scope="session", autouse=True)
def user_authentication():
    """
    用户认证
    """
    yield
    print("用户认证完成")


@allure.epic("测试向用例报告中添加用例分类")
@allure.feature("测试用户注册、登录功能")
class TestAllureAddCaseClass:

    def test_login(self):
        """
        测试登录功能
        """
        assert True

    def test_register(self):
        """
        测试注册功能
        """
        assert True


@allure.epic("测试向用例报告中添加用例分类")
@allure.feature("测试用户信息管理功能")
class TestAllureAddCaseClass1:
    @allure.story("测试获取单个用户信息功能")
    def test_get_single_user_info(self):
        """
        测试获取单个用户信息功能
        """
        assert True

    @allure.story("测试获取所有用户信息功能")
    def test_get_all_user_info(self):
        """
        测试获取所有用户信息功能
        """
        assert True

    @allure.story("测试更新用户信息功能")
    def test_update_user_info(self):
        """
        测试更新用户信息功能
        """
        assert True

    @allure.story("测试删除用户功能")
    def test_delete_user(self):
        """
        测试删除用户功能
        """
        assert True


@allure.epic("需求1")
@allure.feature("测试用户添加、编辑、删除功能")
class TestAllureAddCaseClass2:

    def test_add_user(self):
        """
        测试添加用户功能
        """
        assert True

    def test_edit_user(self):
        """
        测试编辑用户功能
        """
        assert True

    def test_delete_user(self):
        """
        测试删除用户功能
        """
        assert True


@allure.epic("需求1")
@allure.feature("测试产品管理功能")
class TestAllureAddCaseClass3:
    @allure.story("测试添加产品功能")
    @allure.title("测试添加产品功能")
    def test_add_product(self):
        """
        测试添加产品功能
        """
        assert True
        print("添加成功")

    @allure.story("测试编辑产品功能")
    @allure.title("测试编辑产品功能")
    def test_edit_product(self):
        """
        测试编辑产品功能
        """
        assert True
        print("编辑成功")

    @allure.story("测试更新产品状态功能")
    @allure.title("测试更新产品状态功能")
    def test_update_product_status(self):
        """
        测试更新产品状态功能
        """
        assert True
        print("更新成功")

    @allure.story("测试删除产品功能")
    @allure.title("测试删除产品功能")
    def test_delete_product(self):
        """
        测试删除产品功能
        """
        assert True
        print("删除成功")
