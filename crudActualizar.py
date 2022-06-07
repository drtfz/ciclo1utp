
estudiantesActivos = {1001:["claudia siabato"], 1002:["cristian melo"], 1003:["diego mora"], 1004:["Olga Aldana"]}

print("Modificar Información")
idEstudiante = int(input("Digite el ID del estudiante: "))
estudiantesActivos[idEstudiante][0] = str(input("Digite el nuevo nombre: "))
print (f"EL estudiante: {estudiantesActivos[idEstudiante][0]}, ha sido modificado con éxito")
print("-----------------")

def imprimirListadoEstudiantes(estudiantes):
    for identificacion, nombre in estudiantes.items():
        print("El ID es: ", identificacion)
        print("El nombre es: ", nombre[0])
        print(" ------------ ")

imprimirListadoEstudiantes(estudiantesActivos)

