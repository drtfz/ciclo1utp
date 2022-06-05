#cajero automático saldo inicial $1000 - ingreso -retiro -mostrar - salir

saldo = 1000
while True:

    print("\t : menú")
    print("1. ingresar el dinero a la cuenta ")
    print("2. retirar dinero de la cuenta")
    print("3. mostrar dinero de la cueta")
    print("4. salir")

    opcion = int(input("Dígite la opción del menú: "))
    print() #este print() es un salto de linea

    if opcion == 1:
        dinero = float(input("Cuanto dinero desea ingresar : "))
        saldo += dinero # saldo = saldo + dinero
        print(f"Su nuevo saldo es: ${saldo}")

    elif opcion == 2:
        retiro = float(input("Cuanto dinero desea retirar: "))
        if retiro > saldo:
            print ("Fondos insuficientes")
        else:
            saldo -= retiro
        print(f"Su nuevo saldo es: ${saldo}")

    elif opcion == 3:
        print(f"Su saldo disponible es: ${saldo}")

    elif opcion == 4:
        print("No siendo mas... vaya con dios.")
        break

    else:
        print("Opción no válida")

