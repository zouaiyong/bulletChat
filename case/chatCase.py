# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 11:22
# @Author  : zouay
# @Email   : zouaiyong@tuandai.com
# @File    : chatCase.py
# @Software: PyCharm
import argparse
import json
import os
import re
import unittest
from time import sleep

import xlrd

import mutil.TestCaseUtil



class redPacketCase(mutil.TestCaseUtil.TestCaseUtil):
    def caseExecute(self):
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("子弹群")').click()
        for i in range(20):
            for i in range(5):
                message=self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.bullet.messenger:id/editTextMessage")')
                message.click()
                message.clear()
                #self.driver.set_value()
                adbcommond = 'adb shell am broadcast -a ADB_INPUT_TEXT --es msg {inputtext}'.format(inputtext='打卡领金币')
                os.system(adbcommond)
                self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().resourceId("com.bullet.messenger:id/buttonSendMessage")').click()

                self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().resourceId("com.bullet.messenger:id/emoji_button")').click()
                self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().resourceId("com.bullet.messenger:id/imgEmoji")').click()

                self.driver.find_element_by_android_uiautomator(
                    'new UiSelector().resourceId("com.bullet.messenger:id/buttonSendMessage")').click()
        sleep(10)

        #self.driver.back()


    def readexcel(self,path):
        alluser = []
        try:
            excel=xlrd.open_workbook(path)
            sheet=excel.sheet_by_index(0)
            coldict={}
            for col in range(0,sheet.ncols):
                value = sheet.cell(0, col).value.strip()
                value = re.sub(r'\s', '', value)
                coldict[value] = col

            for row in range(1, sheet.nrows):
                try:
                    user={}
                    user['phonenume']=sheet.cell(row,coldict.get('电话号码')).value.strip()
                    user['money']=sheet.cell(row,coldict.get('金额')).value.strip()
                    user['status']=sheet.cell(row,coldict.get('操作')).value.strip
                    user['row']=row
                    user['col']=coldict.get('操作')
                    if '已结算' not in user.get('status'):
                        alluser.append(user)
                except Exception as e:
                    print('excel 读取行内容失败，跳过此行，继续下一行')
                    continue
        except Exception as e:
            print('excel 文件读取异常,异常信息：',str(e))
        return alluser

    pass

if __name__ == '__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(redPacketCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
    pass