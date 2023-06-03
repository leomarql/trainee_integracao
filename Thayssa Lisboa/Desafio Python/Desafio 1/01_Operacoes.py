# Construa um programa que receba como entrada três valores inteiros. Ao final imprima a soma, multiplicação e divisão deste itens.

a, b, c = map(int, input().split())
print('soma: ', a+b+c, 'multiplicacao: ', a*b*c, 'divisao:', a/b/c)

#Escreva um programa que leia um número e apresente a raiz quadrada deste número.
import math
x = int(input("Entre com um número: "))
r = math.sqrt(x)
print(f'raiz: {r:.2f}')