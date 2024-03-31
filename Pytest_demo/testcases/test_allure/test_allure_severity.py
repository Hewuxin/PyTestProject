# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 10:18
# @Author  : heyuyang 
# @Project : PyTestProject 
# @File    : test_allure_severity.py
# @Desc    : 向allure 报告中添加用例优先级
import logging

import allure
import pytest

from Pytest_demo.testcases.test_allure.test_allure_step import simple_step1, simple_step2, simple_step3


@allure.epic("Functional severity测试")
@allure.story("需求1")
@allure.title("没有添加测试用例级别")
def test_allure_without_severity():
    """
    This test case will not have severity in allure report
    """
    print("没有添加用例级别")
    assert 1 == 1


@allure.epic("Functional severity测试")
@allure.story("需求2")
@allure.title("""添加测试用例级别为trivial""")
@allure.severity(allure.severity_level.TRIVIAL)
def test_allure_with_severity_trivial():
    """
    This test case will have severity as trivial in allure report
    """
    print("轻微缺陷，必输项无提示，或者提示不规范")
    assert 1 == 1


@allure.epic("Functional severity测试")
@allure.story("需求2")
@allure.title("""添加测试用例级别为minor""")
@allure.severity(allure.severity_level.MINOR)
def test_allure_with_severity_minor():
    """
    This test case will have severity as minor in allure report
    """
    print("次要缺陷，提示信息不够明确，或者界面错误与UI需求不符")
    assert 1 == 1


@allure.epic("Functional severity测试")
@allure.story("需求3")
@allure.title("""添加测试用例级别为normal""")
@allure.severity(allure.severity_level.NORMAL)
def test_allure_with_severity_normal():
    """
    This test case will have severity as normal in allure report
    """
    print("普通缺陷，数值计算错误")
    assert 1 == 1


@allure.epic("Functional severity测试")
@allure.story("需求4")
@allure.title("""添加测试用例级别为major""")
@allure.severity(allure.severity_level.CRITICAL)
def test_allure_with_severity_critical():
    """
    This test case will have severity as critical in allure report
    """
    print("临界缺陷，功能点缺失，或者系统崩溃")
    assert 1 == 1


@allure.epic("Functional severity测试")
@allure.story("需求5")
@allure.severity(allure.severity_level.BLOCKER)
def test_allure_with_severity_blocker():
    """
    This test case will have severity as blocker in allure report
    """
    print("严重缺陷，密码错误或者账号错误无法正常提醒，或者系统无法正常运行")
    assert 1 == 1


@allure.epic("Functional severity测试")
@allure.feature("核心功能")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("测试网页{param1}核心功能")
@pytest.mark.parametrize("param1", ["www.baidu.com", "www.google.com"])
@pytest.mark.parametrize(("param2", "param3"), [["pytest", "WebTesting"], ["pytest", "ApiTesting"],
                                                ["unittest", "WebTesting"], ["unittest", "ApiTesting"]])
@pytest.mark.parametrize("param4", ["btn1"])
def test_function_with_severity_blocker(param1, param2, param3, param4):
    """
    This test case will have severity as blocker in allure report
    :return:
    """
    logging.info("严重缺陷，密码错误或者账号错误无法正常提醒，或者系统无法正常运行")
    with allure.step(f"步骤1,打开网页{param1}"):
        simple_step1(param1)

    with allure.step(f"步骤2,输入参数{param2},{param3}"):
        simple_step2(param2, param3)
    with allure.step(f"步骤3,点击{param4}"):
        simple_step3(param4)


@allure.epic("Class级别 severity测试")
class TestAllureSeverity:
    @allure.feature("测试登录")
    @allure.title("测试登录功能")
    def test_login(self):
        """
        This test case will have severity as blocker in allure report
        """
        print("登录功能测试")
        assert 1 == 1

    @allure.feature("测试不添加用例级别")
    @allure.title("测试不添加用例级别")
    def test_allure_without_severity(self):
        """
        This test case will not have severity in allure report
        """
        print("没有添加用例级别")

    @allure.feature("测试添加用例级别")
    @allure.story("测试用例级别为trivial")
    @allure.title("测试用例级别为trivial")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_allure_with_severity_trivial(self):
        """
        This test case will have severity as trivial in allure report
        """
        print("轻微缺陷，必输项无提示，或者提示不规范")
        assert 1 == 1

    @allure.feature("测试添加用例级别")
    @allure.story("测试用例级别为minor")
    @allure.title("测试用例级别为minor")
    @allure.severity(allure.severity_level.MINOR)
    def test_allure_with_severity_minor(self):
        """
        This test case will have severity as minor in allure report
        """
        print("次要缺陷，提示信息不够明确，或者界面错误与UI需求不符")
        assert 1 == 1

    @allure.feature("测试添加用例级别")
    @allure.story("测试用例级别为normal")
    @allure.title("测试用例级别为normal")
    @allure.severity(allure.severity_level.NORMAL)
    def test_allure_with_severity_normal(self):
        """
        This test case will have severity as normal in allure report
        """
        print("普通缺陷，数值计算错误")
        assert 1 == 1

    @allure.feature("测试添加用例级别")
    @allure.story("测试用例级别为critical")
    @allure.title("测试用例级别为critical")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_allure_with_severity_critical(self):
        """
        This test case will have severity as critical in allure report
        """
        print("临界缺陷，功能点缺失，或者系统崩溃")
        assert 1 == 1

    @allure.feature("测试添加用例级别")
    @allure.story("测试用例级别为blocker")
    @allure.title("测试用例级别为blocker")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_allure_with_severity_blocker(self):
        """
        This test case will have severity as blocker in allure report
        """
        print("严重缺陷，密码错误或者账号错误无法正常提醒，或者系统无法正常运行")
        assert 1 == 1

    @allure.feature("测试核心功能流程")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("测试网页{param1}核心功能")
    @pytest.mark.parametrize("param1", ["www.apple.com"])
    @pytest.mark.parametrize(("param2", "param3"), [["airtest", "AppiumTesting"]])
    @pytest.mark.parametrize("param4", ["btn1"])
    def test_function_with_severity_blocker(self, param1, param2, param3, param4):
        """
        This test case will have severity as blocker in allure report
        :return:
        """
        logging.info("严重缺陷，密码错误或者账号错误无法正常提醒，或者系统无法正常运行")
        with allure.step(f"步骤1,打开网页{param1}"):
            simple_step1(param1)

        with allure.step(f"步骤2,输入参数{param2},{param3}"):
            simple_step2(param2, param3)
        with allure.step(f"步骤3,点击{param4}"):
            simple_step3(param4)

