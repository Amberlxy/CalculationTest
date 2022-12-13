'''
Author: Amber
Date: 2022-12-02 15:06:39
LastEditors: Amberlxy
LastEditTime: 2022-12-03 11:27:32
FilePath: /Code/CalculationTest/main.py
'''
import time

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os


def generate_import():
    cmd = "allure generate ./reports/temp -o ./reports/html/ --clean"
    # subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/report/" + "index.html"
    # logger.info("报告地址:{}".format(report_path))
    cmd = "allure open -h 127.0.0.1 -p 8883 ./reports/report/"
    # subprocess.call(cmd, shell=True)
    # logger.info("打开测试报告")


if __name__ == '__main__':
    pytest.main(['-vs', './testcase/case/', '-q', '--alluredir', 'reports/temp', '--clean-alluredir'])
    time.sleep(2)
    os.system('allure generate reports/temp -o reports/report --clean')               # -o:output