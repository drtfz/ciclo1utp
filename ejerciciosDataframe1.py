import pandas as pd
import numpy as np

#Obtener las primeras n filas de un objeto DataFrame.
print("Ejercicio 1")
nombre = ["Ana", "Eric", "Felipe", "Felix", "Leidy", "Liliana", "María" ]
puntaje = [11.5, 20, 15.3, np.nan, 19.7, 17, np.nan]
intentos = [1,3,1,2,3,1,2,]
califico = ["si", "no", "si", "si", "no", "no", "si"]
indices = ["A", "B", "C", "D", "E", "F", "G"]
jugadores ={"nombre":nombre, "puntaje":puntaje, "intentos":intentos, "califico":califico}
df = pd.DataFrame(data=jugadores,index=indices)
print(df)
print(df.iloc[1:4])
print()


#Obtener las últimas n filas de un objeto DataFrame
print("Ejercicio 2")
print(df.iloc[-5:])
print()


#Seleccionar columnas de un objeto DataFrame
print("Ejercicio 4")
print(df[["nombre", "intentos"]])
print() 


#Obtener los ejes (atributos de filas y columnas) de un DataFrame
print("Ejercicio 5")
print(df.axes)
print()


#Seleccionar filas y columnas específicas de un DataFrame con iloc
print("Ejercicio 6")
print(df.iloc[[1,5], [0,3]])
print()


#Obtener la dimensión, el tamaño, y la forma de un objeto DataFrame
print("Ejercicio 7")
print(df.ndim)
print()
print(df.size)
print()
print(df.shape)
print()

#Obtener la cantidad de memoria ocupada por cada columna en un DataFrame
print("Ejercicio 8")
print(df.memory_usage())
print()


#Seleccionar las filas y columna a partir de sus nombres con loc.
print("Ejercicio 9")
print(df.loc[["C", "E"], ["intentos", "califico"]])
print()


#Comprobar si un objeto DataFrame está vacio con empty
print("Ejercicio 10")
print(df.empty)
vacio = pd.DataFrame([])
print(vacio.empty)
print()

#Seleccionar los registros que tienen un campo nulo (nan)
print("Ejercicio 11")
print(df[ df["puntaje"].isnull() ])
print()

#Crear un objeto DataFrame a partir de objetos Series
print("Ejercicio 12")
nombre = pd.Series(["Eric", "Henry", "Cavill", "Ramón", "Missy"])
edades = pd.Series([20,39,45,5,6])
personas = {"nombre":nombre, "edades":edades}
people = pd.DataFrame(data=personas)
print(people)
print()

#Cambiar el tipo de dato de una o más columnas con astype
print("Ejercicio 13")
tipos = pd.DataFrame({"x":[1,2,3,4], "y":[5,6,7,8]})
print(tipos.info())
print(tipos.astype({"x":"int32", "y":"float64"}).dtypes)









