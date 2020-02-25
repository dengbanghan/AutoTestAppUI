# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:38
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : toolBar.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from base.basePage import *

class toolBar(WebDriver):

    # 二维码按钮
    iv_scan = (By.ID,"com.pingan.lifecircle:id/iv_scan")

    # 定位显示文案
    city_text = (By.ID,"com.pingan.lifecircle:id/home_page_city")

    # 跳转进入定位选择的按钮
    city_change = (By.ID,"com.pingan.lifecircle:id/fragment_title_arrow")

    # 放大镜搜索按钮
    search_icon = (By.ID,"com.pingan.lifecircle:id/home_search_icon")

    # 搜索栏输入框
    search_txt = (By.ID,"com.pingan.lifecircle:id/home_page_search_hint_txt")

    # 语音客服按钮
    voice_call = (By.ID,"com.pingan.lifecircle:id/home_page_qa_icon")

    # 消息中心按钮
    iv_msg = (By.ID,"com.pingan.lifecircle:id/iv_msg")

    # 我的 页面的设置按钮
    setting_icon = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]")
