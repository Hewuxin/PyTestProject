# 爬虫代码
import allure
import requests


def test_xray_availability():
    # 设置代理访问
    proxy = {'https_proxy': 'http://127.0.0.1:33210',
             'http_proxy': 'http://127.0.0.1:33210',
             }
    # url = 'http://202.199.224.171'
    url1 = 'http://10.21.25.54:3000/'
    response = requests.get(url1, proxies=proxy)

    assert response.status_code == 200


@allure.title("测试百度")
def test_baidu_availability():
    # 创建一个Session对象
    session = requests.Session()

    # 设置代理
    # 设置代理访问

    url = 'https://www.baidu.com'

    # 使用代理进行请求
    response = session.get(url)
    assert response.status_code == 200
    # 打印使用的代理IP
