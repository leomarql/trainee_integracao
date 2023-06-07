# Os números de Fibonacci são representados pela sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... ]
# onde cada valor é calculado pela soma dos dois anteriores. 
# Faça um programa que gere e imprima os primeiros 10 valores desta sequência utilizando for ou while.

def fibonacci(n=10):
    total = [0,1]
    for numero in range (2,n):
        total.append(total[numero-1]+total[numero-2])
    soma = 0
    for numero in range (0,n):
        soma+=numero
    return soma
print (fibonacci())
        
        