asignaturas = ["matematicas", "fisica", "quimica", "historia", "lengua"]
notas = []

for asignatura in asignaturas:
    nota = input(f"digita la nota de : {asignatura} : ")
    notas.append(nota)

print("Su registro ha sido exitoso ")

for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + "  Has obtenido la nota " + notas[i])


print("Estás son todas sus calificaciones.")
