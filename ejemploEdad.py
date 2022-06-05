edad = int(input("Por favor ingrese su edad: "))

if edad > 0 and edad <= 90:
    print("Edad correcta")
    if edad >= 18:
        print("Usted es mayor de edad")
    else:
        print("Usted es menor de edad")

else:
    print("Edad ingresada incorrecta")
