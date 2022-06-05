# Escribir un programa que guarde en un diccionario los precios de las frutas de
# la tabla, pregunte al usuario por una fruta, un número de kilos y los muestre
# por pantalla el precio de ese número de kilos de fruta. Si la fruta no esrá en
# el diccionario debe mostrar un mensaje informando de ello.

frutas = {"Fresa":2.5,"Mango":5,"Manzana":10.6, "Uva":3}
fruta = input("Que fruta quieres : ") .title() #para usar title() es necesario poner la primera letra en mayúscula.
if fruta in frutas:
    kilo = float(input("Cuantos kilos quieres cv?: "))
    print(kilo, "Kilos de ", fruta, "tienen un costo de $", frutas[fruta]*kilo)     
else:
    print(f"La fruta {fruta} no está disponible")


