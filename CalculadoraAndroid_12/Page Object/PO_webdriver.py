from appium import webdriver
from selenium.webdriver.common.by import By


class Driver:
    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "m31nnxx",
            "appPackage": "com.sec.android.app.popupcalculator",
            "appActivity": "com.sec.android.app.popupcalculator.Calculator",
            "udid": "RQ8N80DG4MF",
            "automationName": "uiautomator2"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    def calculadora_cientifica(self):
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_handle_btn_rotation').click()
