#Almacenar una lista de 5 elementos tuplas que guarden el nombre de un país y la cantidad de habitantes.
#Definir tres funciones, en la primera cargar la lista, en la segunda imiprimirla y en la tercera mostrar el nombre del país con mayor cantidade habitantes.

def cargarPaisesPoblacion():
    paises = []
    for x in range(5):
        nombre = input("Digite el nombre del país: ")
        cantidad = int(input("Digite la cantidad de habitantes: "))
        paises.append((nombre,cantidad))
    return paises 


def imprimir(paises):
    print("Paises y su población")
    for x in range(len(paises)):
        print(f"El país: {paises[x][0]}, tiene {paises[x][1]} habitantes")
    print("No hay mas paises.")
    print()


def paisMasPoblacion(paises):
    pos = 0
    for x in range(len(paises)):
        if paises [x][1] > paises[pos][1]:
            pos = x
    print(f"El pais con mayor cantidad de habitantes es: {paises[pos][0]}")


paises = cargarPaisesPoblacion()
imprimir(paises)
paisMasPoblacion(paises)
