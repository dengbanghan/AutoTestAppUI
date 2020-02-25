# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 19:31
# @Author  : DengBanghan
# @Email   : dengbanghan@gmail.com
# @File    : appiumServer.py
# @Software: PyCharm

import socket
import subprocess
import os

class AppiumServer():

    def check_port(self, host, port):
        """检测端口是否被占用"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, int(port)))
            s.shutdown(2)
            print('port %s is uesd !' %port)
            return False
        except:
            print('port %s is available!' %port)
            return True

    def start_appium(self,host,port):
        """启动appium 服务"""
        erromessage=""
        appium_server_url=""
        bootstrap_port=str(port+1)

        try:
            if self.check_port(host,port):

                cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' --bootstrap-port ' + str(bootstrap_port)
                print(cmd)

                # p = subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                p = subprocess.Popen(cmd, shell=True, stdout=open('E:/logs.log','a'), stderr=subprocess.STDOUT)
                # p = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
                p.wait()

                appium_server_url = 'http://' + host + ':' + str(port) + '/wd/hub'
                print(appium_server_url)

        except Exception as msg:
            erromessage=str(msg)

        return appium_server_url,erromessage

    def stop_appium(self):
        """
        退出appium服务
        :return:
        """
        # PID = os.system('netstat -ano | findstr 4723')
        # return os.system('for /f "skip=1 tokens=2" %i in netstat -ano | findstr 4723 do echo %i')
        os.system('taskkill /f /im node.exe')


if __name__ == '__main__':
    s = AppiumServer()
    s.start_appium('127.0.0.1',4723)
    # s.start_appium('127.0.0.1',4725)
    # s.stop_appium()