

"""
# Ciclo 1 Fundamentos de programación

## Reto 1

Descripción del problema: Una entidad Bancaria o entidad financiera, requiere calcular el valor de los intereses ganados y el total final de dinero para diferentes clientes, de acuerdo, a una cantidad de dinero invertida en un CDT. Un CDT por su parte, es un producto financiero que ofrece la posibilidad de guardar dinero durante un tiempo determinado para recibir posteriormente sus intereses devengados, asimismo, ofrece rendimientos a una tasa fija, asegurando una rentabilidad libre de riesgo en un tiempo determinado que por lo general debe ser mayor a dos (2) meses. Si, este dinero se retira antes de este periodo se aplica una penalidad del 2%.  En ese sentido, el valor de los intereses ganados por un periodo de tiempo superior a dos meses se determina a través de la siguiente formula:

    valorIntereses = ( cantidad * porcentaje_interes * tiempo ) / 12

    Donde:

    cantidad = dinero ingresado en el CDT
    porcentaje_interes = 3% (0.03).
    tiempo = cantidad de tiempo

En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:
   
    valorTotal = valorIntereses + cantidad

Se debe determinar el valor total a retirar por el cliente que invirtió en el CDT al final del periodo. Por otra parte, para un periodo de tiempo inferior o igual a dos meses se debe aplicar la siguiente formula:

    valorPerder = cantidad * porcentaje_perder

    Donde:

    cantidad = dinero ingresado en el CDT
    porcentaje_perder = 0.02 (2%)

En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:

    valorTotal = cantidad - valorPerder
___
 """ 
#```python3

def CDT(usuario:str,capital:int,tiempo:int):
    if (0 < tiempo <= 2):
        valorTotal = capital - (0.02 * capital) 
    else:
        valorTotal =capital + (capital * 0.03 * tiempo)/12


    return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {} " .format(usuario,capital, tiempo, valorTotal)


user = input("Ingrese su usuario: ")
amount = int(input("Ingrese el monto: "))
time = int(input("Ingrese el tiempo (en meses): "))

if amount <= 0 or type(amount) != int:
    print ("Monto invalido, intente de nuevo.")
elif time<=0 or type(time)!= int:
    print("Monto invalido, intente de nuevo.")
else:
    print(CDT(user,amount,time))







#```
