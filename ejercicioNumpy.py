#Crear un vector con valores dentro del rango 10 a 49

import numpy as np

a =  np.arange(10,50)
print(a)

#Invertir el vector
print(a[::-1])
print()


#Crear una matriz 3x3 con valores de 0 a 8 
print(np.arange(0,9) .reshape(3,3))
print()

#Crear una matriz 4x5 
print(np.arange(0,20) .reshape(4,5))
print()


#Encontrar los índices que no son ceros del arreglo [1,2,4,2,0,1,0,0,0,12,4,5,6,7,8]
a= np.array([1,2,4,2,0,1,0,0,0,12,4,5,6,7,8])
print(np.argwhere(a==0))
print()

#Crear una matriz identidad de 6x6
print(np.identity(6))

#Crear una matriz con valores al azar con forma 3x3x3
r= np.random.random((3,3,3))
print(r)

#Encontrar los indices de los valores mínimos y máximos de la anterior matriz
print(r.argmax())
print(r.ravel ()[r.argmax()])
print(r.argmin())
print(r.ravel ()[r.argmin()])

#Crear una matriz de 10x10 con 1's en los bordes y 0 en el interior (con rangos de índices)
z = np.ones((10,10))
z[1:-1,1:-1]=0
print(z)
print()

#Crear una matriz de 5x5 con valores en los renglones que vayan de 0 a 4
print(np.tile(np.arange(0,5),5) .reshape(5,5))

#Crear dos arreglos al azar A y B, verificar si son iguales

a = np.random.random((3,3))
b = np.random.random((3,3))
print(a==b)






























