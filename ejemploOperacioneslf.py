num1 = float(input("Digite el valor 1: "))
num2 = float(input("Digite el valor 2: "))

operacion = input("Digite la operación mediante una letra S=suma, R=resta, M=multiplicación, D=división: ") .upper()


if operacion == "S":
    suma = num1 + num2
    print(f"La suma es igual a : {suma}")

elif operacion == "R":
    resta = num1 - num2
    print(f"La resta es igual a : {resta}")

elif operacion == "M":
    multiplicacion = num1 * num2
    print(f"La suma es igual a : {suma}")

elif operacion == "D":
    if(num2!=0):
        division = num1 / num2
        print(f"La división es igual a: {division}")
    else:
        print("No se puede dividir entre cero!")
else:
    print("Operación digitada no valida.")
