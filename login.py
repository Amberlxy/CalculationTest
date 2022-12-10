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
    # print(access_token2)
    return access_token2


filename = 'token.txt'
if os.path.exists(filename) is False:
    with open(filename, 'w+') as f:
        access_token = get_access_token()
        f.write(access_token)
else:
    with open(filename, 'r+') as f:
        access_token_exit = f.read()
        headers = {"access-token": access_token_exit}
        print(access_token_exit)
        print(type(access_token_exit))
        m = requests.get(url=url_domain + url_eventList, headers=headers)
        print(m.json())
        if m.json()['code'] == 6000:
            access_token = access_token_exit
        else:
            access_token = get_access_token()
            f.write(access_token)
# print(access_token)
# print(type(access_token))
# with open(filename, 'r') as file:
#     print(file.read())
#     print(type(file.read()))
#     if file.read() == access_token:
#         print("相同")
#     else:
#         print('不同')


