# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:36
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : startApp.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from base.basePage import *

class startApp(WebDriver):

    # 引导页图片显示区域
    guide_loc = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.ImageView")

    # 引导页的 跳过 按钮
    guide_skip = (By.ID,"com.pingan.lifecircle:id/tv_enter_without_login")

    # 引导页的 继续 按钮，滑动完引导页的图片才会出现
    guide_continue = (By.ID,"com.pingan.lifecircle:id/tv_enter_without_login")

    # 快速登录/注册 按钮
    login_quick = (By.ID,"com.pingan.lifecircle:id/quickLoginBtn")

    # 进入首页 按钮
    login_home = (By.ID,"com.pingan.lifecircle:id/secret_goto_main")

    # 温馨提示弹窗的 同意 按钮
    warm_tip_agreed = (By.ID,"com.pingan.lifecircle:id/alter_right_btn")

    # 温馨提示弹窗的 不同意 按钮
    warm_tip_disagreed = (By.ID,"com.pingan.lifecircle:id/alter_left_btn")

    # 温馨提示弹窗的 知道了 按钮
    warm_tip_know = (By.ID,"com.pingan.lifecircle:id/bt_sure")

    # 获取位置权限弹窗的 允许 按钮
    localtion_allow = (By.ID,"com.android.packageinstaller:id/permission_allow_button")

    # 手机号码输入框
    login_phone = (By.ID,"com.pingan.lifecircle:id/login_et_phone")

    # 发送验证码按钮
    login_getcode = (By.ID,"com.pingan.lifecircle:id/login_get_code")

    # 打点话获取验证码的提示
    login_call = (By.ID,"com.pingan.lifecircle:id/alter_left_btn")

    # 验证码输入框
    login_code = (By.ID,"com.pingan.lifecircle:id/login_et_code")

    # 用户协议勾选框
    login_checkbox = (By.ID,"com.pingan.lifecircle:id/protocol_checkbox")

    # 登录按钮
    login_commit = (By.ID,"com.pingan.lifecircle:id/login_commit")

    # 首页页面的重磅推荐模块标题
    home_peage_common_title = (By.ID,"com.pingan.lifecircle:id/tv_home_page_common_title")

    # 滑动启动页引导图
    def slideGuide(self):
        self.findElement(*self.guide_loc).set_Right_Left(self)

    # 启动页引导图，点击跳过按钮
    def clickSkip(self):
        self.findElement(*self.guide_skip).click()

    # 启动页引导图，点击跳过按钮
    def clickContinue(self):
        self.findElement(*self.guide_continue).click()

    # 点击快速注册/登录按钮
    def clickQuick(self):
        self.findElement(*self.login_quick).click()

    # 点击进入首页按钮
    def clickHome(self):
        self.findElement(*self.login_home).click()

    # 点击温馨提示的同意按钮
    def clickAgreed(self):
        self.findElement(*self.warm_tip_agreed).click()

    # 点击温馨提示的不同意按钮
    def clickDisagreed(self):
        self.findElement(*self.warm_tip_disagreed).click()

    # 点击温馨提示的不同意按钮
    def clickKnow(self):
        self.findElement(*self.warm_tip_know).click()

    # 获取拨打验证码的提示文案
    def textCall(self):
        return self.findElement(*self.login_call).text

    # 点击获取位置权限弹窗的允许按钮
    def clickAllow(self):
        if self.isElementExist(*self.localtion_allow):
            self.findElement(*self.localtion_allow).click()
            self.findElement(*self.localtion_allow).click()

    # 手机号码登录
    def login(self,phonenum,code):
        self.findElement(*self.login_phone).send_keys(phonenum)
        self.findElement(*self.login_getcode).click()
        # if self.isElementExist(*self.login_call):
        #     self.pressKeyCode(AndroidKeyCode.BACK)
        self.findElement(*self.login_code).send_keys(code)
        self.findElement(*self.login_checkbox).click()
        self.findElement(*self.login_commit).click()

    # 获取首页中的热销产品的文案
    def getHomePageCommonTitle(self):
        return self.findElement(*self.home_peage_common_title).text

    # 不登录直接进入App
    def inToAppNotLogin(self):
        self.clickSkip()
        self.clickHome()
        self.clickAllow()

    # 进入首页时进行手机号码登录
    def inToAppLogin(self,phonenum,code):
         self.clickSkip()
         self.clickQuick()
         if self.isElementExist(*self.warm_tip_agreed):
             self.clickAgreed()
             self.clickKnow()
             self.login(phonenum,code)
             self.clickAllow()
         else:
             self.login(phonenum,code)
             self.clickAllow()

    def inToApp(self,phonenum,code):
        if self.isElementExist(*self.guide_skip):
            self.inToAppLogin(phonenum,code)