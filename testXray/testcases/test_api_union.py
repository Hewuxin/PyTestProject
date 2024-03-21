import allure

from testXray.common.send_requests import SendRequest
from testXray.common.yaml_utils import write_yaml, read_yaml


@allure.title("统一封装")
class TestApi:
    @allure.title("登录功能")
    def test_login(self):
        url = "http://localhost:8000/login/"
        form_data = {
            "username": "hyy",
            "password": "123456",
        }

        response = SendRequest().all_send_request(method='post', url=url, data=form_data)

        assert response.status_code == 200
        assert response.json()["msg"] == "Login success!"

        headers = {
            "Context-Type": "application/json",
            "Authorization": f"{response.json()['token_type']} {response.json()['access_token']}",
        }
        write_yaml({"headers": headers})

    def test_get_student_info(self):
        url = "http://localhost:8000/student_info/1"

        headers = read_yaml("headers")
        response = SendRequest().all_send_request(method='get', url=url, headers=headers)

        assert response.status_code == 200
        assert response.json()['user'] == 'hyy'
        assert response.json()['student_info'] == [1, 'daxinzang', 'man', 25, 'py_daxinzang@163.com']

    def test_create_student(self):
        url = 'http://localhost:8000/new_student_info/'
        headers = read_yaml("headers")
        form_data = {
            'gender': 'man',
            'age': 18,
            'email': '2386474352@qq.com'

        }
        response = SendRequest().all_send_request(method='post', url=url, json=form_data, headers=headers)
        assert response.status_code == 400

    @allure.title("获取全部学生信息")
    def test_select_all_student(self):
        url = 'http://localhost:8000/student_info_list/'
        headers = read_yaml("headers")
        response = SendRequest().all_send_request(method='get', url=url, headers=headers)

        assert response.status_code == 200
        assert len(response.json()) == 2

    """
    # 文件上传
    def test_file_upload(self):
        url = "www.baidu.com/"
        params = {
            "access_token": TestApi.Access_token,
            # "access_token": read_yaml("access_token"),
        }
        with open("./segment/origin.jpeg") as file:
            form_data = {
                "media": file
            }

            response = SendRequest().all_send_request(method='post', url=url, params=params, files=form_data)
            assert response.status_code == 200
            assert response.json() == {"msg": "upload success!"}
    """
