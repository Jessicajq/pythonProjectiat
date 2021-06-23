# -*- coding:utf-8 -*-
'''
@Time :2021/5/31$
@Author : xiaojing
@File :testtime.py
'''
from datetime import datetime
now = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
print(now)