# Faça um programa que receba 5 números e retorne o maior e o menor numero, a soma e a média dos números.

lista = [1,77,87,-5, 10]
def maior_lista(lista):
    maior = lista[0]

    for numero in range(1,len(lista)):
         if(lista[numero]>maior):
             maior = lista[numero]
         else: continue
    return maior
def menor_lista(lista):
    menor = lista[0]

    for numero in range(1,len(lista)):
         if(lista[numero]<menor):
             menor = lista[numero]
         else: continue
    return menor
def media(lista):
    soma=0
    for numero in lista:
        soma+=numero
    media = soma/len(lista)
    return media
     
print('Maior:{}\n Menor:{}\n Media:{}'.format(maior_lista(lista),menor_lista(lista),media(lista)))
    