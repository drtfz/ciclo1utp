asignaturas = ["matematicas", "fisica", "quimica", "historia", "lengua"]
aprobado = []

for asignatura in asignaturas :
    nota = float(input("Digite la nota de " + asignatura + ": "))
    if nota >= 3:
        aprobado.append(asignatura)
print("Los cursos aprobadas son: ", aprobado)

for asignatura in aprobado:
    asignaturas.remove(asignatura)
print("Los cursos a repetir son: "+ str(asignaturas))
