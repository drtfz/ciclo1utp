class Persona:

    def __init__(self,nombre,edad):

        self.nombre = nombre
        self.edad = edad


    def __str__(self):
        return "{} Tiene {} años " .format(self.nombre,self.edad)



personas = [Persona("Juan",13),
            Persona("Melissa", 2),
            Persona("Maria", 21)]

menorEdad = filter(lambda Persona : Persona.edad < 18, personas)
for menor in menorEdad:
    print(menor)
