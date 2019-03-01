import unittest
import os
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger='BrowserEngine').getlog()
class BrowserEngine(object):
    # 相对路径的获取方法
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_driver_path=dir +'/tools/chromedriver.exe'
    geck_driver_path=dir +"/tools/geckodriver.exe"
    ie_driver_path=dir +'/tools/IEDriverServer.exe'

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path,encoding='UTF-8')

        browser=config.get("browserType","browserName")
        logger.info("You had select %s browser." %browser)
        url=config.get("testServer","URL")
        logger.info("The test server url is:%s"%url)

        if browser=="Firefox":
            driver=webdriver.Firefox(executable_path=self.geck_driver_path)
            logger.info("开启火狐浏览器。")
        elif browser=="Chrome":
            driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("开启谷歌浏览器。")
        elif browser=="IE":
            driver=webdriver.Ie(self.ie_driver_path)
            logger.info("开启IE浏览器。")


        driver.get(url)
        logger.info("打开：%s" % url)
        driver.maximize_window()
        logger.info("窗口最大化")
        driver.implicitly_wait(10)
        logger.info("隐式等待10秒钟")
        self.driver = driver
        return driver
    def quit_browser(self):
        logger.info("关闭窗口")
        self.driver.quit()




