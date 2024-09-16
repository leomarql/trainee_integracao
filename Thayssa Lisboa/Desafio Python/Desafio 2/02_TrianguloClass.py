# Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de um triângulo, 
# e se forem verificar se é um triângulo equilátero, isóscele ou escaleno. 
# Se eles não formarem um triângulo, escrever uma mensagem.

def VerificaTriangulo(x, y, z):
    if (x + y) > z and (x + z) > y and (y + z) > x:
        if x == y or x == z or y == z:
            mensagem = 'Triângulo Isósceles!'
        if x == y and y == z:
            mensagem = 'Triângulo Equilátero!'
        if x != y and x != z and y != z:
            mensagem = 'Triângulo Escaleno!'
    else:
        mensagem = 'Os comprimentos informados não podem formar um triângulo!'
    return mensagem

x, y, z = map(int, input().split())
print(VerificaTriangulo(x, y, z))
