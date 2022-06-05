estudiantesActivos = {1:["claudia siabato"], 2:["cristian melo"], 3:["diego mora"]}

def cargarEstudiantes(identificacion:int, nombre:str):
    estudiantesActivos[identificacion] = [nombre]  print("Los datos del estudiante han sido registrados con éxito.")
    return estudiantesActivos

def imprimirListadoEstudiantes(estudiantes):
    for identificacion, datos in estudiantes.items():
        print("El ID es: ", identificacion)
        print("El nombre es: ", datos[0])
        print(" ------------ ")

print("Cargar estudiantes")

idEstudiante = int(input("Digite la identificación del estudiante: "))
nombreEstudiante = str(input("Digite el nombre del estudiante: "))
estudiantesActivos = cargarEstudiantes(idEstudiante,nombreEstudiante)

estudiantesActivos = cargarEstudiantes(idEstudiante, nombreEstudiante)
imprimirListadoEstudiantes(estudiantesActivos)


