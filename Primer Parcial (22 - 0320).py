# Sistema de notas
def capturar_notas():
    estudiantes = []

    while True:
        # Solicitar información del estudiante
        nombre = input("Ingrese el nombre del estudiante: ")
        matricula = input("Ingrese la matrícula del estudiante: ")
        notas = []

        # Capturar las 4 notas
        for i in range(4):
            nota = input(f"Ingrese la nota {i+1}: ")
            while True:
                if nota.isdigit():
                    nota = float(nota)
                    if nota >= 0:
                        notas.append(nota)
                        break
                    else:
                        print("La nota no puede ser negativa. Inténtelo de nuevo.")
                        nota = input(f"Ingrese la nota {i+1}: ")
                else:
                    print("La nota debe ser un número. Inténtelo de nuevo.")
                    nota = input(f"Ingrese la nota {i+1}: ")

        # Calcular el promedio
        promedio = sum(notas) / 4

        # Guardar la información del estudiante
        estudiante = {"nombre": nombre, "matricula": matricula, "promedio": promedio}
        estudiantes.append(estudiante)

        # Preguntar si se quiere capturar otro estudiante
        continuar = input("¿Desea capturar otro estudiante? (s/n): ")
        if continuar.lower() != 's':
            break

    # Imprimir los promedios de los estudiante
    print("\nPromedios de los estudiantes:")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Matrícula: {estudiante['matricula']}, Promedio: {estudiante['promedio']:.2f}")

# Ejecutar la función para capturar notas
capturar_notas()
