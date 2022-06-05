num1 = int(input("Dígite el número 1: "))
num2 = int(input("Dígite el número 2: "))
num3 = int(input("Dígite el número 3: "))

if (num1 >= num2 and num1 >= num3):
    print(f"El número mayor es {num1}")

elif(num2 >= num3):
    print(f"El número mayor es {num2}")
else:
    print(f"El número mayor es {num3}")
