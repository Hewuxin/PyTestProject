# -*- coding: utf-8 -*-
# @Time    : 2024/3/26 21:20
# @Author  : heyuyang 
# @Project : PyTestProject 
# @File    : run.py
# @Desc    :


import os
import time
import pytest


if __name__ == '__main__':
    pytest.main(["-vs"])
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")