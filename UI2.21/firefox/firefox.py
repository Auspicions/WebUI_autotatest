from selenium import webdriver
import os
import time
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://ww.baidu.com")
driver.implicitly_wait(5)
# dir = os.path.dirname(__file__)
# chrome_driver_path =dir +"\chromedriver.exe"
# driver=webdriver.Chrome(chrome_driver_path)
time.sleep(1)
driver.execute_script("window.alert('这是一个弹出框')")
time.sleep(5)
driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

# driver.get("https://mail.163.com/")
# assert "163" in driver.title
# driver.switch_to.frame("frame")
# time.sleep(10)


# from selenium import webdriver
# import os
# dir = os.path.dirname(__file__)
# geck_driver_path =dir +"\geckodriver.exe"
# driver=webdriver.Firefox(executable_path=geck_driver_path)
# driver.get("http://www.python.org")
# assert "Python" in driver.title
#
# from selenium import webdriver
# import os
# dir = os.path.dirname(__file__)
# ie_driver_path =dir +"\IEDriverServer.exe"
# driver=webdriver.Ie (ie_driver_path)
# driver.get("http://www.python.org")
# assert "Python" in driver.title