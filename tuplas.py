frutas = ("naranja", "pera" , "uva" , "banana")
print(type(frutas))

#dimensión de la tuple

print(len(frutas))


#acceder a un elemento de la tupla
print(frutas[2])

#navegación inversa
print(frutas[-3])

#modificar una tupla
frutalist = list(frutas)
frutalist[0] = "guanabana"
frutas = tuple(frutalist)
print(frutas)

#iterar una tupla
for fruta in frutas:
    print(fruta,end=", " )

