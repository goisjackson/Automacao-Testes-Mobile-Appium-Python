from appium import webdriver
from selenium.webdriver.common.by import By
from Scripts.Page_Objects.WebDriver_po import Driver
from Scripts.Page_Objects.Calculadora_po import CalculatorPage

# Criar uma instância da classe Driver
conectar = Driver()

# Criar uma instância da classe CalculatorPage
calculadora_page = CalculatorPage(conectar.driver)

# Exemplo: realizar uma soma simples (n + n)
calculadora_page.get_numbers(9).click()
calculadora_page.get_operators('com.android.calculator2:id/op_sub').click()
calculadora_page.get_numbers(3).click()
calculadora_page.get_equals().click()

# Obter o resultado
resultado = calculadora_page.find_element(By.ID, 'com.android.calculator2:id/result').text
print("Resultado da subtração: ", resultado)

conectar.driver.quit()
