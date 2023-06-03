#   Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#   No final, mostre o conteúdo da estrutura na tela.
dic = {}
nome = input('nome: ')
media = float(input('média: '))

if media >= 60:
    situacao = 'aprovado'
    dic = {nome: situacao}
if media >= 40 and media < 60:
    situacao = 'exame especial'
    dic = {nome: situacao}
if media < 40:
    situacao = 'reprovado'
    dic = {nome: situacao} 

print(dic)

