from views import (
    crear_estudiante,
    listar_estudiantes,
    buscar_estudiantes,
    actualizar_estudiante,
    eliminar_estudiante,
    agregar_nota,
    obtener_promedio,
    materias_ofertadas,
    estudiantes_en_comun
)

def pausar():
    input("\nPresiona ENTER para continuar...")

def mostrar_estudiantes(estudiantes):

    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
        return

    print("\n" + "=" * 80)
    print("ESTUDIANTES")
    print("=" * 80)

    for estudiante in estudiantes:
        print(
            f"ID: {estudiante.id} | "
            f"Nombre: {estudiante.obtener_nombre_completo()} | "
            f"Email: {estudiante.email} | "
            f"Carnet: {estudiante.carnet} | "
            f"Promedio: {estudiante.obtener_promedio()}"
        )

    print("=" * 80)

def opcion_crear():

    print("\n--- CREAR ESTUDIANTE ---")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    carnet = input("Carnet: ")

    resultado, informacion = crear_estudiante(
        nombre,
        apellido,
        email,
        carnet
    )

    if resultado:
        print("\n✓ Estudiante creado correctamente.")
        print(informacion)
    else:
        print("\n✗ Error:", informacion)

    pausar()

def opcion_listar():

    estudiantes = listar_estudiantes()

    mostrar_estudiantes(estudiantes)

    pausar()

def opcion_buscar():

    print("\n--- BUSCAR ESTUDIANTE ---")

    texto = input(
        "Escribe nombre, apellido, email o carnet: "
    )

    resultados = buscar_estudiantes(texto)

    mostrar_estudiantes(resultados)

    pausar()
    
def opcion_actualizar():

    print("\n--- ACTUALIZAR ESTUDIANTE ---")

    try:
        id_estudiante = int(
            input("ID del estudiante: ")
        )
    except ValueError:
        print("El ID debe ser un número.")
        pausar()
        return

    estudiante = None

    for e in listar_estudiantes():
        if e.id == id_estudiante:
            estudiante = e
            break

    if estudiante is None:
        print("No existe ese estudiante.")
        pausar()
        return

    print("\nDatos actuales:")
    print("Nombre:", estudiante.nombre)
    print("Apellido:", estudiante.apellido)
    print("Email:", estudiante.email)
    print("Carnet:", estudiante.carnet)

    print("\nEscribe los nuevos datos.")

    nombre = input(
        f"Nombre [{estudiante.nombre}]: "
    )

    apellido = input(
        f"Apellido [{estudiante.apellido}]: "
    )

    email = input(
        f"Email [{estudiante.email}]: "
    )

    carnet = input(
        f"Carnet [{estudiante.carnet}]: "
    )

    if not nombre:
        nombre = estudiante.nombre

    if not apellido:
        apellido = estudiante.apellido

    if not email:
        email = estudiante.email

    if not carnet:
        carnet = estudiante.carnet

    resultado, informacion = actualizar_estudiante(
        id_estudiante,
        nombre,
        apellido,
        email,
        carnet
    )

    if resultado:
        print("\n✓ Estudiante actualizado.")
        print(informacion)
    else:
        print("\n✗ Error:", informacion)

    pausar()

def opcion_eliminar():

    print("\n--- ELIMINAR ESTUDIANTE ---")

    try:
        id_estudiante = int(
            input("ID del estudiante: ")
        )
    except ValueError:
        print("El ID debe ser un número.")
        pausar()
        return

    estudiante = None

    for e in listar_estudiantes():
        if e.id == id_estudiante:
            estudiante = e
            break

    if estudiante is None:
        print("No existe ese estudiante.")
        pausar()
        return

    print("\nVas a eliminar:")
    print(estudiante)

    confirmar = input(
        "¿Seguro que quieres eliminarlo? (si/no): "
    ).lower()

    if confirmar not in ("si", "sí", "s"):
        print("Operación cancelada.")
        pausar()
        return

    resultado, informacion = eliminar_estudiante(
        id_estudiante
    )

    if resultado:
        print("\n✓ Estudiante eliminado.")
        print(informacion)
    else:
        print("\n✗ Error:", informacion)

    pausar()

def opcion_agregar_nota():

    print("\n--- AGREGAR NOTA ---")

    try:
        id_estudiante = int(
            input("ID del estudiante: ")
        )

        nota = float(
            input("Nota (0 - 20): ")
        )

    except ValueError:
        print("El ID y la nota deben ser números.")
        pausar()
        return

    materia = input("Materia: ")

    resultado, informacion = agregar_nota(
        id_estudiante,
        materia,
        nota
    )

    if resultado:
        print("\n✓ Nota agregada correctamente.")
        print(informacion)
    else:
        print("\n✗ Error:", informacion)

    pausar()

def opcion_promedio():

    print("\n--- VER PROMEDIO ---")

    try:
        id_estudiante = int(
            input("ID del estudiante: ")
        )
    except ValueError:
        print("El ID debe ser un número.")
        pausar()
        return

    resultado, informacion = obtener_promedio(
        id_estudiante
    )

    if resultado:
        print(
            f"\nPromedio del estudiante: {informacion}"
        )
    else:
        print("\n✗ Error:", informacion)

    pausar()

def opcion_materias():

    print("\n--- MATERIAS OFERTADAS ---")

    materias = materias_ofertadas()

    if not materias:
        print("No hay materias registradas.")
    else:
        for materia in sorted(materias):
            print("-", materia)

    pausar()

def opcion_materias_comun():

    print("\n--- MATERIAS EN COMÚN ---")

    try:
        id_a = int(
            input("ID del primer estudiante: ")
        )

        id_b = int(
            input("ID del segundo estudiante: ")
        )

    except ValueError:
        print("Los IDs deben ser números.")
        pausar()
        return

    resultado, materias = estudiantes_en_comun(
        id_a,
        id_b
    )

    if not resultado:
        print("\n✗ Error:", materias)

    elif not materias:
        print(
            "\nLos estudiantes no tienen materias en común."
        )

    else:
        print("\nMaterias en común:")

        for materia in sorted(materias):
            print("-", materia)
            
    pausar()

def mostrar_menu():

    print("\n")
    print("=" * 50)
    print("       SISTEMA DE ESTUDIANTES")
    print("=" * 50)

    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Agregar nota")
    print("7. Ver promedio")
    print("8. Ver materias ofertadas")
    print("9. Ver materias en común")
    print("0. Salir")

    print("=" * 50)

def main():
    while True:
        mostrar_menu()

        opcion = input(
            "Selecciona una opción: "
        )

        if opcion == "1":
            opcion_crear()

        elif opcion == "2":
            opcion_listar()

        elif opcion == "3":
            opcion_buscar()

        elif opcion == "4":
            opcion_actualizar()

        elif opcion == "5":
            opcion_eliminar()

        elif opcion == "6":
            opcion_agregar_nota()

        elif opcion == "7":
            opcion_promedio()

        elif opcion == "8":
            opcion_materias()

        elif opcion == "9":
            opcion_materias_comun()

        elif opcion == "0":
            print("\nPrograma terminado.")
            break
        else:
            print("\nOpción no válida.")
            pausar()
            
if __name__ == "__main__":
    
    main()