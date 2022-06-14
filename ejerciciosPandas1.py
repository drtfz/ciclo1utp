import pandas as pd

#Crear y visualizar un arreglo unidimensional como una estructura Series
#Ejercicio 2
datos = [1,2,3,4,5]
serie = pd.Series(datos)
print(type(datos))
print(type(serie))
print(serie)
print(serie.describe())

#Converir un objeto Series en una lista Python.
print("Ejercicio 3")
serie2 = pd.Series([5,7,8,9,10])
print()
lista = serie2.tolist()
print(lista)
print()

#Aplicar las operaciones aritméticas básicas sobre objetos Series
print("Ejercicio 4")
a = pd.Series([1,2,3,4,5])
b = pd.Series([6,7,8,9,10])
print(a+b)
print()
print(a-b)
print()
print(a*b)
print()
print(a/b)
print()
print(a**2)

#Usar operadores relacionales para comparar objetos Series
print("Ejercicio 5")
a = pd.Series([1,2,3,4,5])
b = pd.Series([6,7,8,9,10])
print(a<b)
print()
print(a>b)
print()
print(a==b)
print()
print(a!=b)
print()

#Convertir un diccionario Python en un objeto Series
print("Ejercicio 6")
dicc = {"a":10, "b":20, "c":30, "d":40}
seriedic = pd.Series(dicc)
print(seriedic)
print()

#Convertir un arreglo NumPy en un objetivo Series
print("Ejercicio 8")
import numpy as np
arreglo = np.array([2,5,8,7,6])
print(arreglo)
print()
seriearr = pd.Series(arreglo)
print(seriearr)

#Cambiar el tipo de datos de un objeto Series
print("Ejercicio 8")
cambiar = pd.Series(["100","200","python","300.15","400","500.22"])
print(cambiar)
print()
cambiar = pd.to_numeric(cambiar,errors="coerce")
print (cambiar)

#Obtener una columna de un objeto DataFrame como un objeto Series.
print("Ejercicio 9 ")
datos2 = {"A":[1,2,3,4,5], "B":[6,7,8,9,10], "C":[11,12,13,5,7]} 
df = pd.DataFrame(data=datos2)
print(df)
print()
columna = df.iloc[:,2]
print(columna)

#Extraer una fila de un DataFrame como un objeto Series.
print("Ejercicio 10")
print()
fila = df.iloc[2,:]
print(fila)

print()
rango = df.iloc[2,:2]
print(rango)

print()
print(df.iloc[3,1])

#video del 9 de Junio 
