loteria = []

for i in range(6):
    loteria.append(int(input("Digite el número ganador: ")))

#loteria.sort()
loteria.reverse()
print("Los números ganadores de la lotería son: "+ str(loteria)+ " ")
