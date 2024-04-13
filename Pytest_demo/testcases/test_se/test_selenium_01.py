# -*- coding: utf-8 -*-
# @Time    : 2024/4/10 21:02
# @Author  : heyuyang 
# @Project : PyTestProject 
# @File    : test_selenium_01.py
# @Desc    :

import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="session", autouse=False)
def setup_web_driver():
    driver = webdriver.Chrome()
    driver.get("http://mataim.lntu.edu.cn/xray/")
    driver.maximize_window()

    yield driver

    driver.quit()


class TestSelenium01:

    def test_login(self, setup_web_driver):
        # driver = webdriver.Chrome()
        # driver.get("http://mataim.lntu.edu.cn/xray/")
        # driver.maximize_window()
        driver = setup_web_driver
        hover = driver.find_element(By.XPATH, '//div[@class="icon-user"]/*[name()="i"]/*[name()="svg"]')
        print(hover.text)
        # 实例化ActionChains类，调用鼠标操作，并使用perform()方法执行所有的鼠标动作
        ActionChains(driver).move_to_element(hover).perform()

        # 点击退出登录
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/div/ul/li[2]').click()
        time.sleep(1)

        # 输入用户名和密码
        driver.find_element(By.XPATH, '//*[@class="login-button"]').click()

        # 输入用户名
        driver.find_element(By.XPATH, '//*[@placeholder="请输入邮箱名"]').send_keys("1")
        # 输入密码
        driver.find_element(By.XPATH, '//*[@placeholder="请输入登录密码"]').send_keys("1")

        # 点击登录
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[3]/div/button').click()
        time.sleep(3)

    def test_get_link_text(self, setup_web_driver):
        # driver = webdriver.Chrome()
        # driver.get("http://mataim.lntu.edu.cn/xray/")
        # driver.maximize_window()

        driver = setup_web_driver
        link = driver.find_element(By.LINK_TEXT, 'LNTU-第四范式研究组')
        assert link.get_attribute("href") == "http://10.21.25.54:8888/#/"

    def test_get_partial_link_text(self, setup_web_driver):
        # driver = webdriver.Chrome()
        # driver.get("http://mataim.lntu.edu.cn/xray/")
        # driver.maximize_window()

        driver = setup_web_driver
        link = driver.find_element(By.PARTIAL_LINK_TEXT, 'LNTU')
        assert link.get_attribute("href") == "http://10.21.25.54:8888/#/"

    def test_get_element_by_xpath(self, setup_web_driver):
        # driver = webdriver.Chrome()
        # driver.get("http://mataim.lntu.edu.cn/xray/")
        # driver.maximize_window()

        driver = setup_web_driver
        element = driver.find_element(By.XPATH, '//*[@class="access-button"]')
        assert element.text == "在线试用"

    def test_get_element_by_tag(self, setup_web_driver):
        # driver = webdriver.Chrome()
        # driver.get("http://mataim.lntu.edu.cn/xray/")
        # driver.maximize_window()
        driver = setup_web_driver
        btns = driver.find_elements(By.TAG_NAME, 'button')
        assert len(btns) == 5

    def test_get_element_by_class_name(self, setup_web_driver):
        driver = setup_web_driver
        element = driver.find_element(By.CLASS_NAME, 'access-button')
        assert element.text == "在线试用"

if __name__ == '__main__':
    pytest.main(['-vs'])
