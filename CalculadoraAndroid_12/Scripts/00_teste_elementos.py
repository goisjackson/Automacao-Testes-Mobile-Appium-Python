from selenium.webdriver.common.by import By
from Scripts.PageObject.PO_webdriver import Driver

conectar = Driver()


# numeros
num1 = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="1"]').click()
num2 = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="2"]').click()
num3 = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="3"]').click()
num4 = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="4"]').click()
num5 = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="5"]').click()
num6 = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="6"]').click()
num7 = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="7"]').click()
num8 = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="8"]').click()
num9 = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="9"]').click()
num0 = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="0"]').click()

# operadores
mais = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Mais"]').click()
menos = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Menos"]').click()
mult = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Multiplicação"]').click()
div = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Divisão"]').click()
porcentagem = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Porcentagem"]').click()

# Botões
ponto = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Ponto decimal"]').click()
igual = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Igual"]').click()
apagar = conectar.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_handle_btn_delete').click()
zerar = conectar.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Apagar"]').click()
