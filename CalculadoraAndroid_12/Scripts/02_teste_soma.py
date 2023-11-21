from Scripts.PageObject.PO_calculadora import CalculadoraPage
from Scripts.PageObject.PO_webdriver import Driver

# Inicia o driver
conectar = Driver()

# Abre o aplicativo da calculadora
calculadora_page = CalculadoraPage(conectar.driver)

# Executa a soma
try:
    calculadora_page.clicar_numero("4")
    calculadora_page.clicar_mais()
    calculadora_page.clicar_numero("6")
    calculadora_page.clicar_igual()

    # Obtém o resultado numérico
    resultado_numerico = calculadora_page.obter_resultado_numerico()

    # Imprime o resultado numérico
    print(f"Resultado da Soma: {resultado_numerico}")

    # Verifico se o resultado é o esperado
    resultado_esperado = "10"
    assert resultado_numerico == resultado_esperado, f"Resultado inesperado: {resultado_numerico}"

    print('Teste Soma - OK')

except Exception as e:
    print(f'Erro durante a execução do teste: {str(e)}')
    print('Teste Soma - NOK')

finally:
    conectar.driver.quit()
