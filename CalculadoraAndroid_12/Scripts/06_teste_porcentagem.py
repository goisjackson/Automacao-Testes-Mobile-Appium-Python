from Scripts.PageObject.PO_calculadora import CalculadoraPage
from Scripts.PageObject.PO_webdriver import Driver

# Inicia o driver
conectar = Driver()

# Abre o aplicativo da calculadora
calculadora_page = CalculadoraPage(conectar.driver)

# Executa a porcentagem
try:
    calculadora_page.clicar_numero("1")
    calculadora_page.clicar_numero("0")
    calculadora_page.clicar_numero("0")
    calculadora_page.clicar_menos()
    calculadora_page.clicar_numero("2")
    calculadora_page.clicar_numero("0")
    calculadora_page.clicar_porcentagem()
    calculadora_page.clicar_igual()

    # Obtém o resultado numérico
    resultado_numerico = calculadora_page.obter_resultado_numerico()

    # Imprime o resultado numérico
    print(f"Resultado do calculo: {resultado_numerico}")

    # Verifico se o resultado é o esperado
    resultado_esperado = "80"
    assert resultado_numerico == resultado_esperado, f"Resultado inesperado: {resultado_numerico}"

    print('Teste Porcentagem - OK')

except Exception as e:
    print(f'Erro durante a execução do teste: {str(e)}')
    print('Teste Porcentagem - NOK')

finally:
    conectar.driver.quit()
