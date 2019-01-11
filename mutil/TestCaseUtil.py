# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:04
# @Author  : zouay
# @Email   : aiiyong.zou@outlook.com
# @File    : TestCaseUtil.py
# @Software: PyCharm
import re
import unittest
import os
from appium import webdriver

from mutil.helpers import EXECUTOR

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
class TestCaseUtil(unittest.TestCase):

    def setUp(self):
        #print("set up  is run")
        os.system('adb wait-for-device')
        devicelist=list(
            os.popen('adb devices').readlines())
        #print(devicelist)
        deviceId=re.findall(r'^\w*\b', devicelist[1])[0]
        #print(deviceId)
        #deviceId ='bf5fb4a2' #sys.argv[1]
        deviceAndroidVersion = list(
            os.popen(
                'adb -s %s shell getprop ro.build.version.release' %
                deviceId).readlines())
        deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
        #deviceVersion=7.1
        print(deviceId, deviceVersion)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = deviceVersion
        desired_caps['deviceName'] = deviceId
        # com.bullet.messenger/com.smartisan.flashim.main.activity.MainActivity
        desired_caps['appPackage'] ='com.bullet.messenger' #'com.smartisanos.notes'
        desired_caps['noReset'] = True
        desired_caps['appActivity'] ='com.smartisan.flashim.main.activity.MainActivity' #'com.smartisanos.notes.NotesActivity'
        desired_caps['automationName']='uiautomator2'
        desired_caps['app'] = PATH(
            '../apkfile/ADBKeyBoard.apk'
        )
        #desired_caps['resetKeyboard']=True
        #desired_caps['unicodeKeyboard']=True
        #self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        #os.popen('adb wait-for-device ')
        self.driver = webdriver.Remote(command_executor=EXECUTOR, desired_capabilities=desired_caps)
        self.driver.install_app(desired_caps['app'])
        os.system('adb shell ime set com.android.adbkeyboard/.AdbIME')
        # self.driver = WebDriver(
        #     'http://localhost', port=4723,desired_capabilities=desired_caps)
        #self.driver.launch_app()
        #sleep(3)
        #self.driver.implicitly_wait(5)


    def tearDown(self):
        #self.driver.close_app()
        #self.driver.quit()
        self.driver.back()
        print("tear down is run")

    def test_case(self):
        try:
            print('parent test case')
            self.caseExecute()

        except Exception as e:
            raise Exception("error throw", str(e))

    def caseExecute(self):
        print('parent case execute')
        pass
if __name__ == '__main__':
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestCaseUtil)
    #unittest.TextTestRunner(verbosity=1).run(suite)
    pass
