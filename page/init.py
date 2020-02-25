# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:35
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : init.py
# @Software: PyCharm

import unittest
from utils.operationXml import *
from page.startApp import startApp
from appium import webdriver
from base.appiumServer import AppiumServer

class InitApp(unittest.TestCase,startApp):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = '192.168.181.102:5555'
        desired_caps['appPackage'] = 'com.pingan.lifecircle'
        desired_caps['appActivity'] = 'com.pingan.lifecircle.home.SplashActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        s = AppiumServer()
        s.start_appium('127.0.0.1', 4723)

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()