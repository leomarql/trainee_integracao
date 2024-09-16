# Faça um programa que receba 5 números e retorne o maior e o menor numero, a soma e a média dos números.
def Numeros(lista):
    maior = -999999999999999999
    menor = 9999999999999999999
    soma = 0
    for i in lista:
        soma += i
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    media = soma / 5
    return maior, menor, soma, media

lista = []
for j in range(5): 
    lista.append(int(input()))
print(Numeros(lista))

