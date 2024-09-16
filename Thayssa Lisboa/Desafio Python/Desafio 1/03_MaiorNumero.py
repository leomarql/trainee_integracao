# Escreva uma função para encontrar o maior entre 3 numeros

def Max(a,b,c):
    return max(a, b, c)

a, b, c = map(int, input().split())
print(Max(a,b,c))