#Escribir una función que reciba un diccionario con las notas de los alumnos en curso en un examen y devuelva una serie con la nota mínima, la máxima, la media y la desviación típica.
import pandas as pd

notas = {"Erik":0, "Andrew":0, "Jairo":0, "Eduard":0, "Karen":0}

for keys in notas:
    notas[keys] = float(input(f"Digite la nota del estudiante {keys}: "))

print(notas)

def estadisticasNotas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()],
            index = ["Nota mínima","Nota máxima", "Nota promedio", "Desviación estandar"])

    return estadisticas


print(estadisticasNotas(notas))

#11 06 22 50:08





