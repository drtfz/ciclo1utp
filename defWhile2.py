def main ():
    print("Alcancía Dígital")

    objetivo = float(input("Cuanto desea ahorrar?: "))

    ahorrado = 0.0

    while objetivo > ahorrado :
        ahorrado += float(input("Cuanto deseas consignar al ahorro?: "))
    print(f"Has cumplido con tu objetivo {ahorrado} , le sobra {ahorrado - objetivo}")



if __name__ == "__main__":
    main()

