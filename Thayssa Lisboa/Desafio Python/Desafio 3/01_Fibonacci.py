# Os números de Fibonacci são representados pela sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... ]
# onde cada valor é calculado pela soma dos dois anteriores. 
# Faça um programa que gere e imprima os primeiros 10 valores desta sequência utilizando for ou while.

pu = 0
u = 1
atual = 0
for i in range (1, 9):
    if i == 1:
        print(pu)
    if i == 2:
        print(u)
    atual = pu + u
    pu = u
    u = atual
    print(atual)