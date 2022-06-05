nota = float(input("Por favor ingrese la nota"))

if (nota < 0 or nota > 5):
    print("La nota digitada tiene error")

elif (nota >=0 and nota < 3):
    print("Ha reprobado ")

else:
    print("Ha aprobado")
