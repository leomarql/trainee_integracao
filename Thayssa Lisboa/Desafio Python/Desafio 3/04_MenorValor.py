# Escreva uma função que receba um numero pelo entrada e retorna se aquele numero é primo ou não 

def Primo(x):
    cont = 0
    for i in range(1, x+1):
        if (x % i) == 0:
            cont += 1
    if cont == 2:
        mensagem = 'primo!'
    else:
        mensagem = 'não é primo!'
    return mensagem

x = int(input('valor de x: '))
print(Primo(x)) 