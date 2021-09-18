# -*- coding:utf-8 -*-
'''
@Time :2021/7/20$
@Author : xiaojing
@File :gunicorn.conf.py
'''
import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os

bind = "127.0.0.1:5000"
workers = 4
proc_name = 'gunicorn_project'
reload = True #当代码有修改时，自动重启workers。适用于开发环境。
worker_class = 'gevent' #使用gevent模式，还可以使用sync 模式，默认的是sync模式
loglevel = 'info' #日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'    #设置gunicorn访问日志格式，错误日志无法设置

accesslog = "/home/test/server/log/gunicorn_access.log"      #访问日志文件
errorlog = "/home/test/server/log/gunicorn_error.log"        #错误日志文件