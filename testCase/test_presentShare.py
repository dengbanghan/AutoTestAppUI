# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 14:22
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : test_presentShare.py
# @Software: PyCharm

from page.init import *
from page.startApp import startApp
from page.presentShare import presentShare
import unittest

class PresentShare(InitApp):
    def test_001(self):
        '''好生活App：进入分享赚钱页面'''
        startApp.inToAppNotLogin(self)
        presentShare.clickinShare(self)
