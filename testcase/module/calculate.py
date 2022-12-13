'''
Author: Amber
Date: 2022-12-03 11:32:04
LastEditors: Amberlxy
LastEditTime: 2022-12-03 15:00:23
FilePath: /CalculationTest/testcase/module/calculate.py
'''
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
from login import *
import requests


def calculation(data, access_token4):               # 将data传入「计算」接口，校验返回值code是否为6000
    url_trigger = "/olap/api/event/trigger"
    headers_cal = {"access-token": access_token4}
    r = requests.post(url=url_domain + url_trigger, json=data, headers=headers_cal)
    print(r.json())
    assert r.json()['code'] == 6000
    # print(r.status_code)

