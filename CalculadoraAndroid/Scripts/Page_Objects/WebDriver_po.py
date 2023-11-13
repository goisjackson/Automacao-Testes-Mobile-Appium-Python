from appium import webdriver

class Driver:
    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "avd": "Pixel_2_-_6_RAM_API_28",
            "appPackage": "com.android.calculator2",
            "appActivity": "com.android.calculator2.Calculator",
            "automationName": "UiAutomator2",
# Adiciona esta capacidade para ignorar erros relacionados à política oculta da API
            "ignoreHiddenApiPolicyError": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
