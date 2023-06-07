# Escreva uma função que receba um numero pelo entrada e retorna se aquele numero é primo ou não 
def eh_primo(valor):
    divisores= 0
    for divisor in range(1,valor+1):
        if(valor%divisor==0):
            divisores+=1
        else:
            continue
    primo = True if divisores <=2 else False
    return primo
numero = int(input())
print(eh_primo(numero))
