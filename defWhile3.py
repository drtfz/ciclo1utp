def main ():
    print("Confirme su contraseña: ")
    password1 = input("Digite su contraseña: ")
    password2 = input("Digite de nuevo su contraseña: ")

    while password1 != password2:
        print("Las contraseñas no coinciden. ")
        password1 = input("Digite su contraseña: ")
        password2 = input("Digite de nuevo su contraseña: ")

    print("Contraseña confirmada, ha sido guardada de manera exitosa.")

if __name__ == "__main__":
    main()

