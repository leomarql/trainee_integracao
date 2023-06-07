# Defina a função soma_nat de forma recursiva que recebe como argumento um número natural  n  e devolve a soma de todos os números naturais até  n .

#Exemplo
# soma_nat(n=5):
    # return 5+4+3+2+1 = 15
def soma_nat(n):
    if n==0:
        return 0
    else:
        return n+soma_nat(n-1)
n = int(input())
print(soma_nat(n))