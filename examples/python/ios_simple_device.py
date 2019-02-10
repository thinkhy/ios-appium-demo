# coding=UTF-8（
"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        # http://appium.io/slate/cn/master/?ruby#appium

#       debug
#        app = os.path.abspath('../../apps/HHH/build/Release-iphonesimulator/HHH.app')
#        self.driver = webdriver.Remote(
#                               command_executor='http://127.0.0.1:4723/wd/hub',
#                               desired_capabilities={
#                               'app': app,
#                               'platformName': 'iOS',
#                               'platformVersion': '10.2',
#                               'deviceName': 'iPhone 7',
##                               'automationName': 'XCUITest',
##                               'udid': 'bc7c227a4d06b6794a288459cc0255254d8e7e27',
#                               })

#        app = os.path.abspath('../../apps/HHH/build/Release-iphoneos/HHH.app')

        app = os.path.abspath('/Users/huangye/work/appium_ios_sample_code/apps/HHH/build/Release-iphoneos/HHH.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'iOS',
                'platformVersion': '11.4.1',
                'deviceName': 'qingqing的 iPhone',
                'automationName': 'XCUITest',
                'bundleId': 'com.pluralsight.HHH',
                'udid': 'eac6faafa72f80e17262f18030b548de97048405',
            })

#    def tearDown(self):
##        self.driver.quit()

    def test_scroll(self):
        self.driver.find_element_by_accessibility_id('button').click()

        sleep(1)
        try:
            sleep(1)
        except:
            pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
