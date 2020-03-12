# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 13:58
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : presentShare.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from base.basePage import *

class presentShare(WebDriver):

    # 从首页进入分享赚钱的入口
    inShare = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ImageView[1]")

    def clickinShare(self):
        self.findElement(*self.inShare).click()