# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:40
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : allTest.py
# @Software: PyCharm

import unittest
import os
import HTMLTestRunner
import time

def allTests():
    '''获取所有需要执行的测试用例'''
    suite = unittest.defaultTestLoader.discover(
        start_dir = os.path.join(os.path.dirname(__file__ ),'testCase'),
        pattern = 'test_*.py',
        top_level_dir = None
    )
    return suite

def webTests():
    '''获取所有需要执行的测试用例'''
    suite = unittest.defaultTestLoader.discover(
        start_dir = os.path.join(os.path.dirname(__file__ ),'testCase'),
        pattern = 'test_web*.py',
        top_level_dir = None
    )
    return suite

def appTests():
    '''获取所有需要执行的测试用例'''
    suite = unittest.defaultTestLoader.discover(
        start_dir = os.path.join(os.path.dirname(__file__ ),'testCase'),
        pattern = 'test_app*.py',
        top_level_dir = None
    )
    return suite

def getNowTime():
    '''获取当前的时间'''
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

def run():
    fileName = os.path.join(os.path.dirname(__file__),'report',getNowTime()+'_sinaReport.html')
    fp = open(fileName,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = 'UI 自动化测试报告',
    description = 'UI 自动化测试报告详细信息')
    runner.run(appTests())

if __name__ == '__main__':
    run()