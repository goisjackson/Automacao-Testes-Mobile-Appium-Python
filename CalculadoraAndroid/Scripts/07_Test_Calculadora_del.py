from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from Scripts.Page_Objects.WebDriver_po import Driver
from Scripts.Page_Objects.Calculadora_po import CalculatorPage
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time

# Criar uma instância da classe Driver
conectar = Driver()

# Criar uma instância da classe CalculatorPage
calculadora_page = CalculatorPage(conectar.driver)

# Exemplo: realizar uma soma simples (n + n)
calculadora_page.get_numbers(1).click()
calculadora_page.get_dot().click()
calculadora_page.get_numbers(2).click()
calculadora_page.get_numbers(3).click()
calculadora_page.get_numbers(4).click()

# Botão DEL
del_button = calculadora_page.get_del_button()

# Pressionando DEL
TouchAction(conectar.driver).long_press(del_button).perform()

time.sleep(2)

conectar.driver.quit()


