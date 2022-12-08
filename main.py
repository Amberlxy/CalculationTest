'''
Author: Amber
Date: 2022-12-02 15:06:39
LastEditors: Amberlxy
LastEditTime: 2022-12-03 11:27:32
FilePath: /Code/CalculationTest/main.py
'''
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import config
import requests


if __name__ == '__main__':
    pytest.main(['-s', '-v', './testcase/case/'])