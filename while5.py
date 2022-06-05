import math 

numero = int(input("Digite un número: "))

while numero < 0:
    print("Debes ingresar un número positivo ")
    numero = int(input("Digite un número que sea positivo: "))

print(f"La raiz cuadrada es: {(math.sqrt(numero)): .4f } ") # .2f para dos cifras después del punto .4f para cuatro cifras.
