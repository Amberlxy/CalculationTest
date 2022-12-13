'''
Author: Amber
Date: 2022-12-03 10:25:14
LastEditors: Amberlxy
LastEditTime: 2022-12-03 11:26:32
FilePath: /Code/CalculationTest/config.py
'''

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
import os
import requests


def get_access_token():           # 通过验证码获取新token
    data1 = dict(username=username)
    r = requests.get(url=url_domain + url_code, params=data1)
    verification_code = input("请输入验证码：")
    data2 = {
        'username': username,
        'password': password,
        'captchaCode': verification_code}
    s = requests.post(url=url_domain + url_login, data=data2)
    access_token2 = s.json()['records']
    return access_token2


filename = 'token.txt'
if os.path.exists(filename) is False:               # 判断文件是否存在：若不存在，则获取token并存入文件；
    with open(filename, 'w+') as f:
        access_token = get_access_token()
        f.write(access_token)
else:
    file = open(filename, 'r')
    access_token_exit = file.read()
    file.close()
    headers = {"access-token": access_token_exit}
    print(access_token_exit)
    m = requests.get(url=url_domain + url_eventList, headers=headers)
    print(m.json())
    if m.json()['code'] == 6000:                    # token生效，直接应用
        access_token = access_token_exit
    else:
        access_token = get_access_token()           #token失效，重新获取
        file = open(filename, 'w+')
        file.write(access_token)
        file.close()


