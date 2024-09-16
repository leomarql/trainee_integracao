import numpy as np

#1- Crie uma matriz 1D com números de 0 a 9
m = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(m)

#2- Crie uma matriz booleana numpy 3×3 com ‘True’
mb= np.full((3, 3), True, dtype=bool)
print(mb)

#3- Extraia todos os números ímpares de ‘arr’
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
t = len(arr)
ind = [] 
for i in range(t):
    if i % 2 != 0:
        ind.append(i)
arr = np.delete(arr, ind)
print(arr)

#4- Substitua todos os números ímpares arr por -1
for i in arr:
    if i % 2 != 0:
        arr[i] = -1
print(arr)

#5- Substitua todos os números ímpares em arr com -1 sem alterar arr
arr = np.arange(10)
out = np.where(arr%2==0, arr, -1)
print(out)

#6- Converta uma matriz 1D para uma matriz 2D com 2 linhas:
arr = np.arange(10)
arr1 = arr.reshape(2,5)
print(arr1)
       
#7- Empilhe matrizes verticalmente:
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
c = np.concatenate([a, b])
print(c)