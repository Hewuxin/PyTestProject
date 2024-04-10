# -*- coding: utf-8 -*-
# @Time    : 2024/3/28 20:37
# @Author  : heyuyang 
# @Project : PyTestProject 
# @File    : test_Xray_login.py
# @Desc    : Xray首页退出登录、登录、跳转检测首页自动化
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_detect():
    """
    登录检测,登录成功后点击在线试用跳转到检测页面
    :return:
    """
    driver = webdriver.Chrome()
    driver.get("http://mataim.lntu.edu.cn/xray/")
    time.sleep(1)

    driver.maximize_window()

    time.sleep(2)

    hover = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//div[@class="icon-user"]/*[name()="i"]/*[name()="svg"]'))
    )
    #                                   //div[@class='icon-user']/*[@class='el-icon']/*[@viewBox='0 0 1024 1024']
    #                                   //div[@class='icon-user']//*[name()='svg']
    print(hover.text)
    print("aaaaaaa")
    # 实例化ActionChains类，调用鼠标操作，并使用perform()方法执行所有的鼠标动作
    ActionChains(driver).move_to_element(hover).perform()
    # 点击退出登录
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/div/ul/li[2]').click()
    time.sleep(1)

    # 点击切换颜色
    # 判断当前时间是否处于夜间，如果是，则点击切换到白天模式，否则点击切换到夜间模式
    if time.localtime().tm_hour >= 18 or time.localtime().tm_hour < 6:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[3]/div').click()
        time.sleep(1)

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div[1]/div[1]/button').click()

    # 输入用户名和密码
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/input').send_keys("1")
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[3]/input').send_keys("1")
    time.sleep(5)
    # 点击登录
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[3]/div/button').click()
    time.sleep(5)
    # 点击 在线试用
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[2]/div[1]/div/button').click()
    res = driver.find_element(By.XPATH,
                              '//*[@id="app"]/div/div[3]/section/main/div/div[1]/div/div/div[2]/div[1]/div/h4').text

    print("输出结果", res)
    assert res == "请您上传图片"
    time.sleep(10)
    driver.quit()

    """
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[2]/div[2]/input'))
    )
    username_input.send_keys("1")

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[2]/div[3]/input'))
    )
    password_input.send_keys("1")

    btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[3]/div/button/span'))
    )
    btn.click()

    time.sleep(10)
    driver.quit()
    """


def test_baidu():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.maximize_window()
    s_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="kw"]'))
    )
    s_input.send_keys("selenium")

    btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="su"]'))
    )
    btn.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="4"]/div/h3/a/div/div/p/span/span/em'))
    ).click()

    # 切换到新窗口
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])

    # 点击功能

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="J-lemma-main-wrapper"]/div[2]/div/div[1]/div/div[5]/div/div/ol/li[1]/span[2]/a'))
    ).click()

    item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="J-lemma-main-wrapper"]/div[2]/div/div[1]/div/div[6]/ul[1]/li[3]/div/span[3]'))
    )
    print(item.text)
    time.sleep(10)
    driver.quit()


def test_baidu_xuanting():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.maximize_window()
    # 鼠标悬停

    # 鼠标悬停到设置上，并找到设置的元素
    hover = driver.find_element(By.NAME, 'tj_settingicon')
    # 实例化ActionChains类，调用鼠标操作，并使用perform()方法执行所有的鼠标
    action = webdriver.ActionChains(driver)


if __name__ == '__main__':
    # test_baidu()
    test_login_detect()
