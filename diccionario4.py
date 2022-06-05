# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
# por pantalla la misma fecha en formato dd de <mes> de aaaa . Donde <mes> es el
# nombre del mes.


fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
dia = fecha[:2]
mes = fecha[3:5]
año = fecha[6:10]

meses = {"01":"Enero", "02":"Febrero", "03":"Marzo", "04":"Abril", "05":"Mayo",
        "06":"Junio", "07":"Julio", "08":"Agosto", "09":"Septiembre",
        "10":"Octubre", "11":"Noviembre","12":"Diciembre"}

print(dia," de ",meses[mes]," de ", año)


# Mismo ejercicio pero utilizando split()

fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
fecha = fecha.split("/")
print(fecha[0]," del mes " ,meses[ fecha[1] ], " del año ", fecha[2])
