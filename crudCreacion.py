
estudiantesActivos = {1001:["claudia siabato"], 1002:["cristian melo"], 1003:["diego mora"], 1004:["Olga Aldana"]}

def cargarEstudiantes(identificacion:int, nombre:str): #agrega nuevos elementos al diccionario
    estudiantesActivos[identificacion] = [nombre] 
    print("Información ingresada con éxito.")
    return estudiantesActivos

def imprimirListadoEstudiantes(estudiantes):
    for identificacion, nombre in estudiantes.items():
        print("El ID es: ", identificacion)
        print("El nombre es: ", nombre[0])
        print(" ------------ ")

print("Cargar estudiantes")

idEstudiante = int(input("Digite la identificación del estudiante: "))
nombreEstudiante = str(input("Digite el nombre del estudiante: "))
estudiantesActivos = cargarEstudiantes(idEstudiante,nombreEstudiante)

estudiantesActivos = cargarEstudiantes(idEstudiante, nombreEstudiante)
imprimirListadoEstudiantes(estudiantesActivos)


