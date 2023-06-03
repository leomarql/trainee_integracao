# Defina a função soma_nat de forma recursiva que recebe como argumento um número natural  n  e devolve a soma de todos os números naturais até  n .

#Exemplo
# soma_nat(n=5):
    # return 5+4+3+2+1 = 15

def Soma(n):
   soma = 0
   for i in range(n+1):
    soma += i
   return soma

n = int(input('valor de n: '))
print(Soma(n))
