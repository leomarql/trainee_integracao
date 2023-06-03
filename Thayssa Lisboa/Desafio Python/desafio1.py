def Insere(generos, c):
    nome = (input('nome do filme: ')).lower()
    genero = input('gênero do filme: ').lower()
    data = input('data de visualização: ')
    nota = input('nota: ')
    g = genero + '.txt'
    filme = nome+', '+data+', '+nota+'\n'
    arq = open(g, 'a')
    arq.write(filme)
    arq.close()
    f = input('nome do filme: ').lower()
    for i in generos:
        j = i+'.txt' 
        with open(j) as arquivo:
            for linha in arquivo:
                if f in linha:
                    mensagem = 'filme inserido com sucesso!'
                else:
                    mensagem = 'ocorreu um erro, filme não inserido!'
    if genero in generos:
        c +=1
    else:
        generos.append(genero) 
    return mensagem  
 
def BuscaGenero(generos):
    t = len(generos)
    for i in generos:
        print(i)
    o = (input('\nqual gênero deseja buscar? ')).lower()
    g = o+'.txt'
    if o in generos:
        with open(g) as arquivo:
            for linha in arquivo:
                print(linha)
    else:
        print('insira um filme desse gênero para visualizar a lista!')
    return 

def BuscaFilme(generos):
    f = input('nome do filme: ').lower()
    for i in generos:
        j = i+'.txt'
        with open(j) as arquivo:
            for linha in arquivo:
                if f in linha:
                    print(linha)
    return 

print('\n1 - inserir novo filme \n2- ver filmes por gênero \n3- buscar filme \n0 - sair')
opcao = int(input('o que deseja fazer? '))
generos = ['acao', 'aventura', 'comedia', 'drama', 'fantasia', 'terror']
c = 0 # só pra não deixar o if vazio

while opcao != 0:
    if opcao == 1:
        print(Insere(generos, c))
    if opcao == 2:
        print(BuscaGenero(generos)) 
    if opcao == 3:
        print(BuscaFilme(generos))

    print('\n1 - inserir novo filme \n2- ver filmes por gênero \n3- buscar filme \n0 - sair')
    opcao = int(input('o que deseja fazer? '))