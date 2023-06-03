# Para esse exercicio usa as funções disponiveis da lista para a resolução

x = [1, 2, 3]
y = [8, 9, 10]

# Mude x para ficar x = [1, 2, 3, 4]
x.append(4)
print(x)

# Use y para mudar x e ter como resultado final x= [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Mude x para ficar x = [1, 2, 3, 4, 9, 10]
x.remove(8)
print(x)

# Mude x para ficar x = [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)

# Escreva o tamanho da lista x
print(len(x))

# Escreva todos os valores de x multiplicados por 1000
for i in x:
    print(i*1000) 