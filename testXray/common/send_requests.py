import requests


class SendRequest:
    # 会话，会话对象能够自动的管理Cookie关联
    # session = requests.session()
    session = requests.Session()

    def all_send_request(self, method, url, **kwargs):
        print("--------------接口测试开始---------------")

        print("请求方式: %s" % method)
        print("请求地址: %s" % url)
        if kwargs:
            for key in kwargs.keys():
                print("请求参数:  ", key, "---", kwargs[key])

        response = SendRequest.session.request(method, url, **kwargs)

        print("------------- 接口测试结束---------------")
        print("status_code: %d" % response.status_code)
        return response
