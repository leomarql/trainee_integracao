# Uma empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. 
# Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido. 
# Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$ 50.000.00 (incluindo extremos) a comissão será de 9.5%. Em qualquer outro caso, a comissão será de 7%. 
# Escreva um programa que calcule a comissão de um vendedor baseado no valor de suas vendas.
def Comissao(valor_vendas, comissao):
    if valor_vendas > 50000.00:
        comissao = valor_vendas * 0.12 
    if valor_vendas >= 30000.00 or valor_vendas <= 50000.00:
        comissao = valor_vendas * 0.095
    if valor_vendas < 30000.00:
        comissao = valor_vendas * 0.07
    return comissao

valor_vendas = int(input("Entre  a number: "))
comissao = 0

print(f'valor da comissão: {Comissao(valor_vendas, comissao)}')
