#Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una Serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%

import pandas as pd

inicio = int(input("Digite por favor el año de inicio de las ventas: "))
fin = int(input("Digite por favor el año final de las ventas: "))
ventas = {}

for i in range(inicio, fin+1):
    ventas[i]= float(input(f"digite las ventas del año {i} :"))
print()

ventas = pd.Series(ventas)
print("Las ventas por año son: ")
print(ventas)
print("Las ventas por año con descuento son: ")
print(ventas*0.9)
