"""
referencia: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# 1-Abra o arquivo do diretorio atual "foo.txt"
# Printe todo o conteudo do arquivo , então feche o arquivo
fout = open('foo.txt','r')
conteudo = fout.read()

# 2- Crie um arquivo chamado "bar.txt" 
fin = open('bar.txt','w') 
contador = conteudo.count('sir')
fout.close()
fin.write(str(contador))
fin.close
fin = open('bar.txt','r')
conteudo2 = fin.read()
print(conteudo2)
fin.close()

# Abra o arquivo e conte quanta vezes a palavra "sir" aparece 
# Escreva no arquivo que voce criou quantas palavras foram encontradas
# Feche o arquivo

