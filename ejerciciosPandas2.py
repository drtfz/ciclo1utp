import pandas as pd

#Convertir un objeto Series con múltiples listas en un único objeto Series
print("Ejercicio 11")
serie = pd.Series([["Colombia", "Mexico", "Perú", "Argentina"], ["Bolivia", "Brazil", "Chile"], ["Ecuador"]])
print(serie)
sere = serie.apply(pd.Series) .stack() .reset_index(drop=True)
print(serie)


#Ordenar los valores de un objeto Series con el método sort_values.
print("Ejercico 12")
datos = pd.Series(["1.1", "2.3", "Python", "Java", "4", "3.5"])
print(datos)
datos = pd.Series(datos).sort_values()
print(datos)


#Agregar datos a un objeto Series existente
print("Ejercicio 13")
datos = datos.append(pd.Series(["HTML", "REACT"])).reset_index()
print(datos)
print()
