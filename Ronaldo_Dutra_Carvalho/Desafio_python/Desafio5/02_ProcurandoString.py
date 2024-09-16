#   Faça um funcão que leia o nome de uma pessoa
#   e diga se ela tem "Silva" no nome.

nome = input("insira seu nome: ")

retorno = nome.find('Silva')

if(retorno != -1):
    print ("Ela tem Silva no nome")
else:
    print("Não tem Silva")