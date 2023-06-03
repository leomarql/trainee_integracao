# Criar uma função externa que irá aceitar dois parametros, a e b
# Crie uma função interna dentro da função externa que irá retornar a soma os parametros a e b 
# Na função externa, adicione 5 ao retorno da funcao interna e escreva na tela este valor

def Externa(a, b):
    def Interna(a, b):
        return (a+b)
    return (Interna(a,b)+5)

a, b = map(int, input().split())
print(Externa(a,b))


