class Persona:

    def __init__(self,nombre,edad):

        self.__nombre = nombre
        self.__edad = edad


    def __str__(self):
        return "El nombre es: "+ self.__nombre + "y su edad es : "+ str(self.__edad)


