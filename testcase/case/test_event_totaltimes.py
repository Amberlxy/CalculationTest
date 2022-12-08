'''
Author: Amber
Date: 2022-12-03 11:29:13
LastEditors: Amberlxy
LastEditTime: 2022-12-03 15:00:53
FilePath: /CalculationTest/testcase/case/test_event_totaltimes.py
'''
import data as data

# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用pytest框架,测试文件必须以test_开头或者以_test结尾，断言使用基本的assert即可
# 类名必须以Test开头,并且不能带有 init 方法
from testcase.module.calculate import *


def test_01(data):
    data = {
        "productId": "1480807164923912194",
        "packageId": "",
        "dataSource": "ta",
        "events": [
            {
                "analysis": "TOTAL_TIMES",
                "eventName": "task_store_content__subscribe",
                "eventCode": "bwl4loevrshs",
                "eventType": "common",
                "eventNameDisplay": "订阅的总次数",
                "quota": "",
                "relation": "and",
                "initData": "[]",
                "type": "normal",
                "filts": [],
                "eventSplitIndexes": [],
                "fieldType": "",
                "attributeList": []
            }
        ],
        "eventView": {
            "startTime": "2022-11-25",
            "endTime": "2022-12-01",
            "timeParticleSize": "day",
            "firstDayOfWeek": 1,
            "relation": "and",
            "filts": [],
            "groupBy": [],
            "eventSplit": {},
            "initData": {
                "relationship": "and",
                "dataForm": []
            }
        },
        "statType": "event",
        "id": "f8df0158-5b1a-4b21-a548-3ae372e2a9b3"
    }


calculation(data)
