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
    calculadora_page.clicar_numero("0")
    calculadora_page.clicar_ponto_decimal()
    calculadora_page.clicar_numero("9")
    calculadora_page.clicar_multiplicacao()
    calculadora_page.clicar_numero("2")
    calculadora_page.clicar_numero("0")
    calculadora_page.clicar_ponto_decimal()
    calculadora_page.clicar_numero("5")
    calculadora_page.clicar_igual()

    # Obtém o resultado numérico
    resultado_numerico = calculadora_page.obter_resultado_numerico()

    # Imprime o resultado numérico
    print(f"Resultado do calculo: {resultado_numerico}")

    # Verifico se o resultado é o esperado
    resultado_esperado = "2.068.45"
    assert resultado_numerico == resultado_esperado, f"Resultado inesperado: {resultado_numerico}"

    print('Teste Ponto Decimal - OK')

except Exception as e:
    print(f'Erro durante a execução do teste: {str(e)}')
    print('Teste Ponto Decimal - NOK')

finally:
    conectar.driver.quit()
