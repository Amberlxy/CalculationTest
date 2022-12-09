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


def get_access_token():
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


file = 'token.txt'
fo = open(file, 'w+')
if os.path.getsize(file):
    fo.write(get_access_token())
else:
    access_token1 = fo.read()
    headers = {"access-token": access_token1}
    m = requests.get(url=url_domain + url_eventList)
    if m.json()['code'] == 6000:
        access_token = access_token1
    else:
        access_token = get_access_token()
fo.close()



# print(get_access_token())
