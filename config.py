'''
Author: Amber
Date: 2022-12-03 10:25:14
LastEditors: Amberlxy
LastEditTime: 2022-12-03 11:26:32
FilePath: /Code/CalculationTest/config.py
'''

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 用户登录
username = "18091755660"
password = "18091755660_123"
url_code = "/uc/user/sendCaptchaCode"  # 获取验证码
url_login = "/uc/user/login"  # 登录

# 产品信息
productId = "1480807263997566978"
packageId = "1480808811246952449"
eventCode = "bwl4loevrshs"
access_token = "eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxODA5MTc1NTY2MDp4eHh4eHh4OjEzMjgyNDY5NjI4NTM1Mzk4NDI6MTQ0NzgwNDA0MTUyNjM1ODAxODoyOmFsbDphbGw6YWxsOmFsbCIsInVuaXF1ZVZhbHVlIjoiMTgwOTE3NTU2NjA6eHh4eHh4eDoxMzI4MjQ2OTYyODUzNTM5ODQyOjE0NDc4MDQwNDE1MjYzNTgwMTg6MjphbGw6YWxsOmFsbDphbGwiLCJleHAiOjE2NzA1MjkwMDd9.N1_KhVqs8BR382z4WOq8yNsDETdts2b5hsRcRWKg4-m0RMfdkDCO1fTSbQGZ03JcjqzmQ6oI7mi5vwMwmqhto86LOE2Xg12j3jr-Rj2Hq3cdeECkXZpSh6XNdxshTqN_wC40z7nr7ccNKgASabhwalvwXF2rpwTKERHIk-hCY3U"

# URL
url_domain = "http://holo-sh.tapque.com"  # 预发布
url_eventList = "/olap/consolidate/et/group/list"  # 某产品的事件列表
url_pubArgs = "/olap/consolidate/et/eventPublicArgs"  # 事件公参
url_Args = "/et/eventTracking/argList"  # 事件私参
url_userAttribute = "/olap/consolidate/et/userAttribute/allArgs"  # 用户属性

# def get_accesstoken():
#     data1 = {
#         username: username
#     }
#     r = requests.post(url=url_domain + url_code, json=data1)
#     print(r)
#     verification_code = input("请输入验证码：")
#     data2 = {
#         username: username,
#         password: password,
#         verification_code: verification_code
#     }
#     s = requests.post(url=url_domain + url_login, json=data2)
#     access_token = s.json()['records']
#     return access_token
#
#
# print(get_accesstoken())
