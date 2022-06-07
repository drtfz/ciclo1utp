def imprimirListadoEstudiantes(estudiantes):

    for identificacion, nombre in estudiantes.items():
        print("El ID es: ", identificacion)
        print("El nombre es: ", nombre[0])
        print(" ------------ ")

def eliminar(estudiante, activos):

    if eliminarEstudiante in estudiantesActivos:
        nombreEstudiante = estudiantesActivos[eliminarEstudiante][0]
        del estudiantesActivos[eliminarEstudiante]
        print(f"El estudiante { nombreEstudiante }, ha sido eliminado con éxito.\n \nLa lista actual es la siguiente:\n \n  ")
        imprimirListadoEstudiantes(estudiantesActivos)

    else:
        print("El estudiante no se encuentra.\n \nLa lista actual es la siguiente:\n \n ")
        imprimirListadoEstudiantes(estudiantesActivos)

estudiantesActivos = {1001:["claudia siabato"], 1002:["cristian melo"], 1003:["diego mora"], 1004:["Olga Aldana"]}

print("Eliminar Información")
eliminarEstudiante = int(input("Ingrese el ID del estudiante a eliminar: "))
eliminar(eliminarEstudiante, estudiantesActivos)


