# Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de um triângulo, 
# e se forem verificar se é um triângulo equilátero, isóscele ou escaleno. 
# Se eles não formarem um triângulo, escrever uma mensagem.


def eh_triangulo(lados):
    maior_lado = max(lados)
    menor_lado_um = min(lados)
    lados.remove(menor_lado_um)
    menor_lado_dois = min(lados)
    if((menor_lado_um+menor_lado_dois)>=maior_lado):
        return True
    else:
        return False
def detecta_triangulo(lados):
    if(eh_triangulo(lados)):
        if(lados[0]==lados[1] and lados[1]==lados[2]):
            print("É equilátero")
        elif(lados[0]!= lados[1] and lados[1]!= lados[2] and lados[2]!= lados[0]):
            print("É escaleno")
        else:
            print("É isosceles")
lista_numeros = list(map(int,input("Insira os numeros:").split()))
detecta_triangulo(lista_numeros)
    
    
    