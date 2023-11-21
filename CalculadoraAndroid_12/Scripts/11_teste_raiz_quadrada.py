from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Scripts.PageObject.PO_webdriver import Driver
from Scripts.PageObject.PO_calculadora import CalculadoraPage


# Instanciar a classe Driver
conectar = Driver()

# Instanciar a classe CalculadoraPage
calculadora_cientifica_page = CalculadoraPage(conectar.driver)

# Ir para a calculadora científica
calculadora_cientifica_page.clicar_calculadora_cientifica()

# Aguardar até que o botão de raiz esteja visível antes de clicar
WebDriverWait(conectar.driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_root_another_'
                                             'font_default'))
)

# Testar operações
try:
    calculadora_cientifica_page.clicar_raiz()
    calculadora_cientifica_page.clicar_numero('4')
    calculadora_cientifica_page.clicar_numero('9')
    calculadora_cientifica_page.clicar_igual()

    # Obtém o resultado numérico
    resultado_numerico = calculadora_cientifica_page.obter_resultado_numerico()

    # Imprime o resultado numérico
    print(f"Resultado da Raiz quadrada: {resultado_numerico}")

    # Verifico se o resultado é o esperado
    resultado_esperado = '7'
    assert resultado_numerico == resultado_esperado, f"Resultado inesperado: {resultado_numerico}"

    print('Teste Raiz quadrada - OK')

except Exception as e:
    print(f'Erro durante a execução do teste: {str(e)}')
    print('Teste Raiz quadrada - NOK')

finally:
    conectar.driver.quit()
