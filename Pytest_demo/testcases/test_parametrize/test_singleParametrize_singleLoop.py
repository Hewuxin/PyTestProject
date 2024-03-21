# -*- coding: utf-8 -*-
# @Time    : 2024/3/15 17:42
# @Author  : heyuyang 
# @Project : TestProject
# @File    : test_singleParametrize_singleLoop.py
# @desc    :  single parametrize single loop practice

import pytest
import pymysql


def connect_database():
    # 连接数据库
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='PyTestProject',
        cursorclass=pymysql.cursors.DictCursor  # 指定游标类型为字典型，方便取得查询结果
    )
    return connection


def login_check(username):
    connection = connect_database()
    try:
        with connection.cursor() as cursor:
            # 执行查询

            sql = "SELECT * FROM user WHERE name = %s"
            cursor.execute(sql, (username,))

            # 获取查询结果
            result = cursor.fetchone()

            if result:
                print("User found:")
                print(result)
            else:
                print("User not found.")
    finally:
        # 关闭数据库连接
        connection.close()

    return result


@pytest.mark.parametrize("name", ["hyy"])
def test_user_exist(name):
    result = login_check(name)
    assert result is not None


if __name__ == '__main__':
    pytest.main(['-vs'])
