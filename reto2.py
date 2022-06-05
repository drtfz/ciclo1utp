

def cliente(informacion:dict)-> dict:  

    id_ = informacion["id_cliente"] 
    name = informacion["nombre"] 
    age = informacion["edad"] 
    ftime = informacion["primer_ingreso"]
    discount5 = 0.05
    discount7 = 0.07


    if age > 18:

        attr = "X-Treme"
        payment = 20000
        apt  = True

        if ftime == True:
            payment -= payment * discount5  

    elif 15 <= age <= 18:

        attr = "Carros chocones"
        payment = 5000
        apt  = True

        if ftime == True:
            payment -= payment * discount7  

    elif 7 <= age < 15:

        attr = "Sillas voladoras"
        payment = 10000
        apt  = True

        if ftime == True:
            payment -= payment * discount5  

    else:

        attr  = "N/A"
        payment = "N/A" 
        apt = False
    
    return {"nombre": name, "edad": age, "atraccion": attr, "apto": apt, "primer_ingreso": ftime, "total_boleta": payment }

informacion = {"id_cliente":1, "nombre":"Kathy", "edad":5,"primer_ingreso":False}

print(cliente(informacion))

