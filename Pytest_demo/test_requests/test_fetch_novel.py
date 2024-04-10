# -*- coding: utf-8 -*-
# @Time    : 2024/4/9 20:13
# @Author  : heyuyang 
# @Project : PyTestProject 
# @File    : test_fetch_novel.py
# @Desc    :

import logging

import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common_utils import send_mail


def test_fetch_content(driver, novel_content_url):
    """
    获取小说内容
    :param novel_content_url:
    :return:
    """
    driver.get(novel_content_url)
    title_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="bookname"]/h1'))
    )
    title = title_element.text

    content_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]'))
    )
    content = content_element.text
    # 去除广告
    content = title + "\n" + content.replace("\n", "").replace("天才一秒记住本站地址：[笔趣阁小说] 最快更新！无广告！", "")
    return content


def test_fetch_novel():
    """
    获取小说章节
    :return:
    """
    novel_index_url = "https://www.xswang.vip/book/61703/"
    logging.info("novel_index_url: %s ", novel_index_url)
    driver = webdriver.Chrome()
    driver.get(novel_index_url)
    # 获取更新时间
    update_time = driver.find_element(By.XPATH, '//*[@id="info"]/p[3]')
    # 获取今天日期
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    logging.info("Today time: %s", today)
    logging.info("last updated time: %s", update_time.text)

    # 判断今天是否更新,决定要不要获取内容
    if today == update_time.text.split(" ")[1]:
        logging.info("Start fetching novel content")
        catalog = driver.find_elements(By.XPATH, '//*[@id="list"]/dl//a')[-10:]
        logging.info(" fetched novel content numbers: %d", len(catalog))

        contents = [test_fetch_content(driver, content_url) for content_url in
                    [catalog[i].get_attribute("href") for i in range(len(catalog))]]

        with open(today + "novel.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(contents))
        logging.info("Novel content saved to file")
        # 发送邮件
        send_mail("\n".join(contents), "today" + str(len(catalog)) + "update")
    else:
        logging.info("No update today, skip fetching novel content")
        return


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info("Start fetching novel")
    test_fetch_novel()
    #
    # test_fetch_content()

