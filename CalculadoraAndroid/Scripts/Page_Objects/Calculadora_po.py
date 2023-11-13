from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def get_numbers(self, digit):
        digit_id = f'com.android.calculator2:id/digit_{digit}'
        return self.find_element(By.ID, digit_id)

    def get_operators(self, operator):
        operator_id = f'{operator}'
        return self.find_element(By.ID, operator_id)

    def get_equals(self):
        return self.find_element(By.ID, 'com.android.calculator2:id/eq')
