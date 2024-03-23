import pytest
import allure
import requests

from testXray.common.send_requests import SendRequest
from testXray.common.yaml_utils import write_yaml, read_all_yaml, read_yaml


@allure.title("接口参数化测试")
class TestApi:
    @allure.title("登录、获取token功能")
    @pytest.mark.parametrize("login_yaml", read_all_yaml(
        "/Users/heyuyang/Study/PyProject/TestProject/testXray/testcases/test_login.yaml"))
    def test_login(self, login_yaml):
        name = login_yaml["name"]

        method = login_yaml["request"]["method"]
        url = login_yaml["request"]["url"]
        form_data = login_yaml["request"]["form_data"]
        validate = login_yaml["validate"]
        print(name)
        response = SendRequest().all_send_request(method=method, url=url, data=form_data)

        assert response.status_code == validate
        if response.status_code == 200:
            headers = {
                "Context-Type": "application/json",
                "Authorization": f"{response.json()['token_type']} {response.json()['access_token']}",
            }
            write_yaml({"headers": headers})

    @allure.title("获取单个学生信息功能")
    def test_get_student_info(self):
        url = "http://localhost:8000/student_info/1"

        headers = read_yaml("headers")
        response = SendRequest().all_send_request(method='get', url=url, headers=headers)

        assert response.status_code == 200
        assert response.json()['user'] == 'hyy'
        assert response.json()['student_info'] == [1, 'daxinzang', 'man', 25, 'py_daxinzang@163.com']

    @allure.title("获取学生列表功能")
    def test_get_student_list(self):
        url = "http://localhost:8000/student_list"

        headers = read_yaml("headers")
        response = SendRequest().all_send_request(method='get', url=url, headers=headers)

        assert response.status_code == 200
        assert response.json()['user'] == 'hyy'
        assert len(response.json()['student_list']) == 5
