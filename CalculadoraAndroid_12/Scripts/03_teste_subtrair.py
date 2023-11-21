from Scripts.PageObject.PO_calculadora import CalculadoraPage
from Scripts.PageObject.PO_webdriver import Driver

# Inicia o driver
conectar = Driver()

# Abre o aplicativo da calculadora
calculadora_page = CalculadoraPage(conectar.driver)

# Executa a subtração
try:
    calculadora_page.clicar_numero("1")
    calculadora_page.clicar_numero("0")
    calculadora_page.clicar_menos()
    calculadora_page.clicar_numero("7")
    calculadora_page.clicar_igual()

    # Obtém o resultado numérico
    resultado_numerico = calculadora_page.obter_resultado_numerico()

    # Imprime o resultado numérico
    print(f"Resultado da Subtração: {resultado_numerico}")

    # Verifico se o resultado é o esperado
    resultado_esperado = "3"
    assert resultado_numerico == resultado_esperado, f"Resultado inesperado: {resultado_numerico}"

    print('Teste Subtração - OK')

except Exception as e:
    print(f'Erro durante a execução do teste: {str(e)}')
    print('Teste Subtração - NOK')

finally:
    conectar.driver.quit()
