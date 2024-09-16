#   Faça um funcão que leia o nome de uma pessoa
#   e diga se ela tem "Silva" no nome.

def Busca(nome): 
    if 'Silva' in nome or 'silva' in nome:
        mensagem = 'tem Silva no nome!'
    else:
        mensagem = 'não tem Silva no nome!'
    return mensagem

nome = input('nome completo: ')
print(Busca(nome))
