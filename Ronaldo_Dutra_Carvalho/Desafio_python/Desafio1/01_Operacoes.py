import math
# Construa um programa que receba como entrada três valores inteiros. Ao final imprima a soma, multiplicação e divisão deste itens.

a= int(input ("insira o primeiro numero:\n"))
b = int(input("insira o segundo numero:\n"))
c = int(input("insira o terceiro numero:\n"))
soma = a+b+c
produto = a*b*c
divisao = a/b/c

print("{},{},{}".format(soma,produto,divisao))

# Escreva um programa que leia um número e apresente a raiz quadrada deste número.

x = int(input("Entre  a number: "))

print("{}".format(math.sqrt(x)))


