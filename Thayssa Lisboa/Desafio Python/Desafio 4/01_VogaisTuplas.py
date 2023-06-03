#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

frutas = ('banana', 'abacate', 'pera', 'uva', 'abacaxi')
vogais = []

for i in frutas:
    for j in i:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            vogais.append(j)
    print('vogais de', i) 
    for k in vogais:
        print(k)
    vogais.clear()