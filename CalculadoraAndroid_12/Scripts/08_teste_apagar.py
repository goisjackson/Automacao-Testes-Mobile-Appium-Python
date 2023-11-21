from Scripts.PageObject.PO_calculadora import CalculadoraPage
from Scripts.PageObject.PO_webdriver import Driver

# Inicia o driver
conectar = Driver()

# Abre o aplicativo da calculadora
calculadora_page = CalculadoraPage(conectar.driver)

# Executa calculo com decimal
try:
    calculadora_page.clicar_numero("1")
    calculadora_page.clicar_numero("0")
    calculadora_page.clicar_apagar()
    calculadora_page.clicar_apagar()
    print('Teste Apagar - OK')

except Exception as e:
    print(f'Erro durante a execução do teste: {str(e)}')
    print('Teste Apagar - NOK')

finally:
    conectar.driver.quit()
