# Programa persona dígite un caracter para saber si es una vocal

caracter = str(input("Digite un caracter: ")) .lower()

if len(caracter)>1:
    print("ERROR! Debe escribir un solo caracter. ")

elif (caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" ):

    print(f"El caracter {caracter} es una vocal. ")

else :

    print(f"El caracter {caracter} NO es una vocal. ")







    
