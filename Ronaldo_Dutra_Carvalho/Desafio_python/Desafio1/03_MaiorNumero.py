# Escreva uma função para encontrar o maior entre 3 numeros
def Max(a,b,c):
    lista = [a,b,c]
    return max(lista)
numeros = list(map(int, input("Digite as variáveis separadas por espaço: ").split()))
print( Max(numeros[0],numeros[1],numeros[2]))