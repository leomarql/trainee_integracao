#   Faça um programa que leia uma frase pelo teclado e mostre:
#       - Quantas vezes aparece a letra 'A'
#       - Em que posição ela aparece a primeira vez
#       - Em que posição ela aparece a última vez

palavra = input("insira a palavra:")
primeira_vez = palavra.find('A')
contagem = 0
for letra in palavra:
    if(letra=='A'):
        contagem+=1
for numero in range(len(palavra)-1,-1,-1):
    if(palavra[numero]=='A'):
        print('A ultima ocorrencia se dá no indice {}'.format(numero))
        break
print('A primeira ocorrencia da letra "A" ocorre no indice {}'.format(primeira_vez))
print("A letra 'A' aparece {} vezes".format(contagem))
        