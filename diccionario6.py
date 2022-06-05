# Ejercicio 6
# Mustura S.A. es una empresa dedicada a la comercialización de dulces a nivel
# nacional. Después de una minuciosa evaluación, la empresa ha decidido
# asignarle la tarea de desarrollar un programa que permita gestionar las ventas
# de dulces. Se le pide ingresar la siguiente información: : Cantidad de dulces
# a comprar, el tipo de dulce (1,2 o 3) y muestre como salida, el tipo de dulce,
# el precio unitario, la cantidad y el monto de la venta, terniendo en cuenta la
# siguiente politica de descuento.



can = int(input("Cuantos dulces desea?: "))
tipo = int(input("Qué tipo de dulce? (1, 2, 3) :"))

dulceria = {"can":can,"tipo":tipo,"precio":0}

if dulceria["tipo"] == 1:
    dulceria["precio"] = 3
    monto = dulceria["can"] * dulceria["precio"]
    if dulceria["can"] <= 5:
        monto-= 0.5
    elif dulceria["can"] <= 10:
        descuento = monto * 0.07
        monto -= descuento #monto = monto - descuento

elif dulceria["tipo"] == 2:
    dulceria["precio"] = 4
    monto = dulceria["can"]* dulceria["precio"]
    if dulceria["can"] >7:
        monto-= 0.5
    elif dulceria["can"] <= 10:
        descuento = monto * 0.05
        monto -= descuento 

elif dulceria["tipo"] == 3:
    dulceria["precio"] = 5
    monto = dulceria["can"] * dulceria["precio"]
    if dulceria["can"] > 4:
        descuento = monto * 0.15
        monto -= descuento
else:
    print("Tipo de dulce no disponible ")

print("El tipo de dulce ",dulceria["tipo"]," tiene un costo unitario de "
        ,dulceria["precio"]," usted lleva ",dulceria["can"])
print(f"Con un total de ${monto} ")
