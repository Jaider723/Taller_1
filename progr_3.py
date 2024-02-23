def get_promedio(notas):
    contador = 0
    for nota in notas:
        contador += nota
    return contador/len(notas)

def get_notas(asignatura):
    lista = []
    for i in range(1,5):
        nota = int(input(f"Ingrese la nota {i} de {asignatura}: "))
        lista.append(nota)
    return lista

asignaturas = ["matemáticas","física"]
notas_semestre = []

for asignatura in asignaturas:
    notas = get_notas(asignatura)
    promedio = get_promedio(notas)
    notas_semestre.append(promedio)
    print(f"Promedio de {asignatura}: {promedio}", end=" - ")
    if promedio < 3:
        print("asignatura perdida")
    else:
        print("asignatura ganada")

promedio_semestre = get_promedio(notas_semestre)
print(f"Promedio general: {promedio_semestre}",end=" - ")
if promedio_semestre < 3:
    print("Semestre perdido")
elif promedio_semestre < 4:
    print("Buen trabajo")
else:
    print("Felicidades, serás becado")
