# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 12:27
# @Author  : heyuyang 
# @Project : testXray
# @Module  : 
# @File    : run.py
import os
import time
import pytest


if __name__ == '__main__':
    pytest.main(["-vs"])
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")
