# Defina a função div que recebe como argumentos dois números naturais  m  e  n  e 
# devolve o resultado da divisão inteira de  m  por  n . 

# div(7,2)
# Esperado: 3

def Divisao(m, n):
    return m // n

m, n = map(int, input('valores de m e n: ').split())
print(Divisao(m, n))
