# Uma empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. 
# Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido. 
# Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$ 50.000.00 (incluindo extremos) a comissão será de 9.5%. Em qualquer outro caso, a comissão será de 7%. 
# Escreva um programa que calcule a comissão de um vendedor baseado no valor de suas vendas.

valor_vendas = int(input("Entre  a number: "))


def calcular_comissao(valor_vendas):
    if(valor_vendas>50000):
        comissao = 0.12*valor_vendas
        return comissao
    elif(valor_vendas>=30000 and valor_vendas <=50000):
        comissao = 0.095*valor_vendas
        return comissao
    else:
        comissao = 0.07*valor_vendas
        return comissao
print(calcular_comissao(valor_vendas))
