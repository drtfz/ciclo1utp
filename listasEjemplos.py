nombres = ["ana", "brayan", "didian", "felix", "karen", "natalia", "junior"]
print(type(nombres))
print(nombres)

#conocer la dimensio de la lista

print(len(nombres))

#acceder a la información individual de la lista

print(nombres[4])
print(nombres[1])

#navegación inversa

print(nombres [ -5 ])
print(nombres[-7])

#imprimir un rango

print(nombres[0:6])
print(nombres[3:6])
print(nombres[0:4])

#cambiar elemento de una lista

nombres[1] = "sebastian"
print(nombres)

#revisar si existe un elemento en la lista

if "felix" in nombres:
    print("si está en la lista")
else:
    print("no está en la lista")

#agregar información al final de la lista

nombres.append("brayan")
print(nombres)

#agregar información en una posición específica

nombres.insert(3,"maría")
print(nombres)

#remover elementos de la lista por su valor

nombres.remove("sebastian")
print(nombres)

#remover el último elemento de una lista

nombres.pop()
print(nombres)

#remover elemento de la lista por posición

del nombres[0]
print(nombres)

del nombres[2:5]
print(nombres)

#limpiar los elementos de una lista

nombres.clear()
print(nombres)
