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
import os,sys
sys.path.append("./")

import config


def test_calculation(datas):
    url_trigger = "/olap/api/event/trigger"
    headers = {"access-token" : config.access_token}
    r = requests.post(url = config.url_domain + url_trigger, json = datas,headers=headers)
    # print(r.json()['code'])
    assert r.json()['code'] == '6000'
    print(r.status_code)

print(test_calculation())
