import pandas as pd

#Obtener las primeras n filas de un objeto DataFrame.
print("Ejercicio 1")
nombre = ["Ana", "Eric", "Felipe", "Felix", "Leidy", "Liliana", "María" ]
puntaje = [11.5, 20, 15.3, 18, 19.7, 17, 9.8]
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
# 1:15:27 10 de junio





