#crea una tupla con los meses del año, pide números al usuario, si el número está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición, sino muestra un mensaje de error.

#el programa termina cuando el usuario introduce cero.

meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

salir = False
while(not salir):

    numero = int(input("Ingrese un número: "))

    if numero == 0:
        salir = True
    elif (numero>=1 and numero <= len(meses)):
        print(meses[numero-1])
    else:
        print("INgrese un número entre el 1 y ", len(meses))
