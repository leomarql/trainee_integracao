"""referencia: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files"""
# 1-Abra o arquivo do diretorio atual "foo.txt"
# Printe todo o conteudo do arquivo , então feche o arquivo
with open('foo.txt') as arquivo:
    for linha in arquivo:
        print(linha)

# 2- Crie um arquivo chamado "bar.txt" 
# Abra o arquivo e conte quanta vezes a palavra "sir" aparece 
# Escreva no arquivo que voce criou quantas palavras foram encontradas
# Feche o arquivo
c = 0
with open('foo.txt') as arq:
    for linha in arq:
        for palavra in linha.split():
            if 'sir' in palavra:
                c += 1

arq = open('bar.txt', 'w')
arq.write(str(c))
arq.close()
 
with open('bar.txt') as arquivo:
    for linha in arquivo:
        print(linha)
