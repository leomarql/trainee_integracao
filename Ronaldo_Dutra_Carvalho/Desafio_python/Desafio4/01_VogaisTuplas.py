#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

frutas = ('banana', 'abacate', 'pera', 'uva', 'abacaxi')
lista_vogais = ('a','e','i','o','u')

def retorna_vogais(palavra):
    vogais_palavra=[]
    for letra in palavra:
        for vogal in lista_vogais:
            if(letra==vogal and letra not in vogais_palavra):
                vogais_palavra.append(letra)
    return vogais_palavra
for palavras in frutas:
    print(retorna_vogais(palavras))