# Escribir un programa qu pregunte al usuario su nombre, edad, dirección y
# teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
# mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de
# teléfono es <telefono>. 

nombre = input("Por favor ingrese su nombre: ")
edad = input("Por favor ingrese su edad: ")
direccion = input("Por favor ingrese su dirección: ")
telefono = input("Por favor ingrese su teléfono : ")
persona = {"nombre":nombre, "edad":edad, "direccion":direccion,
        "telefono":telefono}
print(persona[ "nombre" ], "tiene", persona["edad"], "años, ","vive en ",
        persona["direccion"]," y su número de teléfono es ", persona["telefono"] )

