def circulo(radio:float):
    area = 3.1416 * (radio**2)
    return ("El área del circulo de acuerdo al radio es: {}") .format(area)

radio = float(input("Por favor ingrese el radio del circulo ( en cm ):  "))
print(circulo(radio))
 


