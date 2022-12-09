'''
Author: Amber
Date: 2022-12-03 11:32:04
LastEditors: Amberlxy
LastEditTime: 2022-12-03 15:00:23
FilePath: /CalculationTest/testcase/module/calculate.py
'''
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from config import *


def calculation(data, access_token):
    url_trigger = "/olap/api/event/trigger"
    headers = {"access-token": access_token}
    r = requests.post(url=url_domain + url_trigger, json=data, headers=headers)
    print(r.json())
    assert r.json()['code'] == 6000
    # print(r.status_code)

