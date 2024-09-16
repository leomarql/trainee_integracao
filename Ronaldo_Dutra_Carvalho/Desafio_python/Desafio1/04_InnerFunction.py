# Criar uma função externa que irá aceitar dois parametros, a e b
# Crie uma função interna dentro da função externa que irá retornar a soma os parametros a e b 
# Na função externa, adicione 5 ao retorno da funcao interna e escreva na tela este valor
def Soma5(a,b):
    def Soma_Numeros(a,b):
        return a+b
    return Soma_Numeros(a,b)+5
a = int(input("Insira o primeiro numero:"))
b = int(input("Insira o segundo numero:"))
print (Soma5(a,b))