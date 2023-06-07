

while(True):
    acao = input("Escolha sua acao:")
    
    genero = input("Escolha um genero")
    if(acao =="Inserir"):
        fout = open(genero+".txt","a") 
        nome_filme= input("Insira o nome do filme: ")
        fout.write(nome_filme+",")
        fout.close()
        
    if(acao =="Vizualizar_por_genero"):
         fout = open(genero+".txt","r")
         filmes = fout.read()
         print (filmes) 
    
