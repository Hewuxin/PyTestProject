# -*- coding: utf-8 -*-
# @Time    : 2024/4/10 15:35
# @Author  : heyuyang 
# @Project : PyTestProject 
# @File    : common_utils.py
# @Desc    : common utils

import yaml

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def read_all_yaml(yaml_path):
    with open(yaml_path, encoding='utf-8') as f:
        yaml_data = yaml.load(stream=f, Loader=yaml.FullLoader)
        return yaml_data


def send_mail(content, subject="小说更新提醒"):
    """
    发送微信消息
    :param subject:
    :param content:
    :return:
    """
    sender_email = "py_daxinzang@163.com"
    token_path = "./email_token.yaml"
    # 授权码
    sender_token = read_all_yaml(token_path)["163_token"]

    receiver_email = ["py-heyuyang@qq.com"]

    # 邮件内容
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = sender_email
    message['To'] = receiver_email[0]

    try:
        # 连接到SMTP服务器并发送邮件
        smtp_obj = smtplib.SMTP_SSL('smtp.163.com', 465)  # 连接到163的SMTP服务器
        smtp_obj.ehlo("smtp.163.com")
        smtp_obj.login(sender_email, sender_token)  # 登录邮箱
        smtp_obj.sendmail(sender_email, receiver_email, message.as_string())  # 发送邮件
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败:", e)
