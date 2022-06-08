def convertir(sistema):

    def sistema_binario(numero):
        print(f"El número décimal {numero}, en binario es { bin(numero) }")

    def sistema_octal(numero):
        print(f"El número décimal {numero}, en octal  es { oct(numero) }")

    def sistema_hexadecimal(numero):
        print(f"El número décimal {numero}, en hexadecimal es { hex(numero) }")


    sistema_fun = {"bin":sistema_binario, "oct":sistema_octal, "hex":sistema_hexadecimal}
    return sistema_fun[sistema]

numeroConv = (int(input("Digite el número a convertir: ")))
convertir("bin")(numeroConv)
convertir("oct")(numeroConv)
convertir("hex")(numeroConv)
