# -*- coding: utf-8 -*-
# @Time    : 2024/3/15 18:14
# @Author  : heyuyang 
# @Project : TestProject 
# @File    : test_multiParametrize_multiLoop.py
# @Desc    : multi params multi loop practice

import pytest

from Pytest_demo.testcases.test_parametrize.test_singleParametrize_singleLoop import connect_database


@pytest.fixture(scope='module')
def db_connection():
    connection = connect_database()
    print("连接+1")
    yield connection

    # 关闭数据库连接
    connection.close()


@pytest.mark.parametrize("name", ["hyy", "hwx", "heyuyang"])
def test_user_exist(db_connection, name):
    with db_connection.cursor() as cursor:
        # 执行查询
        sql = "SELECT * FROM user WHERE name = %s"
        cursor.execute(sql, (name,))
        result = cursor.fetchone()
    assert result is not None


@pytest.mark.parametrize(("name", "password"), [("hyy", "123"), ("hwx", "123456")])
def test_login(db_connection, name, password):
    with db_connection.cursor() as cursor:
        # 执行查询
        sql = "SELECT * FROM user WHERE name = %s AND password = %s"
        cursor.execute(sql, (name, password))
        result = cursor.fetchone()
    assert result is not None


if __name__ == '__main__':
    pytest.main(['-vs'])
