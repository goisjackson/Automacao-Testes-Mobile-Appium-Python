from selenium.webdriver.common.by import By
import re


class CalculadoraPage:
    def __init__(self, driver):
        self.driver = driver

    # numeros
    def clicar_numero(self, numero):
        xpath = f'//android.widget.Button[@content-desc="{numero}"]'
        numero_elemento = self.driver.find_element(By.XPATH, xpath)
        numero_elemento.click()

    # Métodos para operadores
    def clicar_mais(self):
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Mais"]').click()

    def clicar_menos(self):
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Menos"]').click()

    def clicar_multiplicacao(self):
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Multiplicação"]').click()

    def clicar_divisao(self):
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Divisão"]').click()

    def clicar_porcentagem(self):
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Porcentagem"]').click()

    # Métodos para botões
    def clicar_ponto_decimal(self):
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Ponto decimal"]').click()

    def clicar_igual(self):
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Igual"]').click()

    def clicar_apagar(self):
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_handle_btn_delete').click()

    def clicar_zerar(self):
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Apagar"]').click()

    def obter_resultado_numerico(self):
        resultado_elemento = self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_edt_formula')
        resultado = resultado_elemento.text

        # Usando expressão regular para extrair números, pontos e vírgulas
        numeros = re.findall(r'[\d.,]+', resultado)

        # Concatenando os números encontrados
        resultado_numerico = ''.join(numeros)
        return resultado_numerico

    # calculadora cientifica
    def clicar_raiz(self):
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_root_another_'
                                        'font_default').click()

    def clicar_elevado2(self):
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_x_2').click()

    def clicar_elevadoy(self):
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_x_y').click()

    def clicar_pii(self):
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_pie').click()

    def clicar_calculadora_cientifica(self):
        self.driver.find_element(By.ID, 'com.sec.android.app.popupcalculator:id/calc_handle_btn_rotation').click()
