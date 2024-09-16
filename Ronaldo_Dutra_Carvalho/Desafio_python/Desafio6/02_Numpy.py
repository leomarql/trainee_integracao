
import numpy as np

#1- Crie uma matriz 1D com números de 0 a 9
arr1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr1)

#2- Crie uma matriz booleana numpy 3×3 com ‘True’
arr2 = np.array([[0,0,0],[0,0,0],[0,0,0]])
arr3 = arr2==0
print(arr3)

#3- Extraia todos os números ímpares de ‘arr’

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2 = np.array([])

for numero in arr:
    if(numero%2 == 0):
        arr2 = np.append(arr2,numero)
print (arr2)

#4- Substitua todos os números ímpares arr por -1
for numero in range(0,len(arr)):
    if(arr[numero]%2 != 0 ):
        arr[numero]= -1
print(arr)


#5- Substitua todos os números ímpares em arr com -1 sem alterar arr

arr = np.arange(10)
out = np.where(arr%2==0,arr,-1)
print(out)

#6- Converta uma matriz 1D para uma matriz 2D com 2 linhas:

arr = np.arange(10)
novo_arr = arr.reshape(2,-1)
print(novo_arr)

       
#6- Empilhe matrizes verticalmente:

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
nova_matriz = np.concatenate((a,b),axis = 1)
print(a)
print(b)
print (nova_matriz)


#6- Empilhe as matrizes horizontalmente:

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
nova_matriz = np.concatenate((a,b),axis = 0)
print(nova_matriz)