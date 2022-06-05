def vel (tiempo:int, distancia:int):
    
    velocidad = distancia / tiempo
    return " La velocidad es : {} m/s " .format(velocidad)

tiempo= int(input("Digite el tiempo (segundos): "))
distancia = int(input("Digite la distancia (en metros): "))


print(vel(tiempo,distancia))
