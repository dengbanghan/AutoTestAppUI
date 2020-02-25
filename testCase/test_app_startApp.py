# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:39
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : test_app_startApp.py
# @Software: PyCharm

from page.init import *
from page.startApp import startApp
import unittest

class StartApp(InitApp):
    def test_001(self):
        '''好生活App：不进行手机号码登录直接进入App'''
        startApp.inToAppNotLogin(self)
        self.assertEqual(self.getHomePageCommonTitle(),"重磅推荐")

    def test_002(self):
        '''好生活App：进行手机号码登录后进入App'''
        startApp.inToAppLogin(self,phonenum = '17722527464',code = '1708')
        self.assertEqual(self.getHomePageCommonTitle(),"重磅推荐")

    def test_003(self):
        '''好生活App：进入App'''
        startApp.inToApp(self,phonenum = '17722527464',code = '1708')
        self.assertEqual(self.getHomePageCommonTitle(),"重磅推荐")

if __name__ == '__main__':
    unittest.main(verbosity=2)