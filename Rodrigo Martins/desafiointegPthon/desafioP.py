def inicializacao():
    print("#####################################################")
    print("###################_MOVIES_##########################")
    print("#####################################################")
    
    print('\n1 - Inserir novo filme')
    print('2 - Ver filmes por gênero')
    print('3 - Buscar filme')
    print('0 - Sair')

##opcao1
def inserir_filme(generos):
    nome = input('Nome do filme: ').lower().strip()
    genero = input('Gênero do filme: ').lower().strip()
    data = input('Data de visualização: ').strip()
    nota = input('Nota: ').strip()
    
    arquivoGenero = genero + '.txt'
    
    filme = f'Filme: {nome}, visualizado: {data}, avaliação: {nota}\n'
    with open(arquivoGenero, 'a') as arquivo:
        arquivo.write(filme)
    
    if genero not in generos:
        generos.append(genero)
    
    return '\n\nFilme inserido com sucesso!\n\n'

##opcao2
def listar_filmes_por_genero(generos):
    print('Gêneros disponíveis:')
    for genero in generos:
        print(genero)
        
    generoEscolhido = input('\nQual gênero deseja buscar? ').lower().strip()
    arquivoGenero = generoEscolhido + '.txt'
        
    if generoEscolhido in generos:
        with open(arquivoGenero) as arquivo:
            for linha in arquivo:
                print(linha)
    else:
        print('Gênero não encontrado')
##opcao3
def buscar_filme(generos):
    filmeEscolhido = input('Nome do filme: ').lower().strip()
    
    for genero in generos:
        
        arquivoGenero = genero + '.txt'        

        with open(arquivoGenero,) as arquivo:
            for linha in arquivo:
                if filmeEscolhido in linha:
                    print(linha)
                    break
            else:
                continue
            break
    else:
        print("Filme não encontrado\n")
 ##main##       
generos = ['acao', 'aventura', 'comedia', 'drama', 'fantasia', 'terror']
opcao = 10 

while opcao != 0:  
    if opcao == 1:
        print(inserir_filme(generos))
    elif opcao == 2:
        listar_filmes_por_genero(generos)
    elif opcao == 3:
        buscar_filme(generos)
        
    inicializacao()
    opcao = int(input('Qual opção desejas? '))

