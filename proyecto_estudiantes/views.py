from models import Estudiante
from shared.json_manager import GestorJSON

RUTA_ESTUDIANTES = "data/estudiantes.json"
gestor = GestorJSON(RUTA_ESTUDIANTES)

def obtener_estudiantes():
    datos = gestor.leer()
    estudiantes = []
    for dato in datos:
        estudiantes.append(
            Estudiante.desde_diccionario(dato)
        )
    return estudiantes

def guardar_estudiantes(estudiantes):
    datos = []

    for estudiante in estudiantes:
        datos.append(estudiante.a_diccionario())
    return gestor.guardar(datos)

def siguiente_id():
    estudiantes = obtener_estudiantes()
    if not estudiantes:
        return 1
    return max(estudiante.id for estudiante in estudiantes) + 1

def obtener_por_id(id_estudiante):
    estudiantes = obtener_estudiantes()
    for estudiante in estudiantes:
        if estudiante.id == id_estudiante:
            return estudiante
    return None

def crear_estudiante(nombre, apellido, email, carnet):
    estudiantes = obtener_estudiantes()
    for estudiante in estudiantes:
        if estudiante.carnet.lower() == carnet.lower():
            return False, "El carnet ya existe"
    nuevo_id = siguiente_id()
    nuevo_estudiante = Estudiante(
        nuevo_id,
        nombre,
        apellido,
        email,
        carnet
    )
    estudiantes.append(nuevo_estudiante)
    if guardar_estudiantes(estudiantes):
        return True, nuevo_estudiante
    return False, "No se pudo guardar el estudiante"

def listar_estudiantes():
    return obtener_estudiantes()

def buscar_estudiantes(texto):
    estudiantes = obtener_estudiantes()
    texto = texto.lower().strip()
    resultados = []
    for estudiante in estudiantes:
        if (
            texto in estudiante.nombre.lower()
            or texto in estudiante.apellido.lower()
            or texto in estudiante.email.lower()
            or texto in estudiante.carnet.lower()
        ):
            resultados.append(estudiante)
    return resultados

def actualizar_estudiante(
    id_estudiante,
    nombre,
    apellido,
    email,
    carnet
):
    estudiantes = obtener_estudiantes()
    estudiante_encontrado = None
    for estudiante in estudiantes:
        if estudiante.id == id_estudiante:
            estudiante_encontrado = estudiante
            break
    if estudiante_encontrado is None:
        return False, "No se encontró el estudiante"
    for estudiante in estudiantes:
        if (
            estudiante.id != id_estudiante
            and estudiante.carnet.lower() == carnet.lower()
        ):
            return False, "El carnet ya existe"
    estudiante_encontrado.nombre = nombre
    estudiante_encontrado.apellido = apellido
    estudiante_encontrado.email = email
    estudiante_encontrado.carnet = carnet
    if guardar_estudiantes(estudiantes):
        return True, estudiante_encontrado
    return False, "No se pudo actualizar el estudiante"

def eliminar_estudiante(id_estudiante):
    estudiantes = obtener_estudiantes()
    estudiante_encontrado = None
    for estudiante in estudiantes:

        if estudiante.id == id_estudiante:
            estudiante_encontrado = estudiante
            break
    if estudiante_encontrado is None:
        return False, "No se encontró el estudiante"
    estudiantes.remove(estudiante_encontrado)
    if guardar_estudiantes(estudiantes):
        return True, estudiante_encontrado
    return False, "No se pudo eliminar el estudiante"

def agregar_nota(id_estudiante, materia, nota):
    estudiante = obtener_por_id(id_estudiante)
    if estudiante is None:
        return False, "No se encontró el estudiante"
    if nota < 0 or nota > 20:
        return False, "La nota debe estar entre 0 y 20"
    materia = materia.strip()
    if not materia:
        return False, "La materia no puede estar vacía"
    estudiante.agregar_nota(materia, nota)
    estudiantes = obtener_estudiantes()
    for i in range(len(estudiantes)):
        if estudiantes[i].id == id_estudiante:
            estudiantes[i] = estudiante
            break
    if guardar_estudiantes(estudiantes):
        return True, estudiante
    return False, "No se pudo guardar la nota"

def obtener_promedio(id_estudiante):
    estudiante = obtener_por_id(id_estudiante)
    if estudiante is None:
        return False, "No se encontró el estudiante"
    return True, estudiante.obtener_promedio()

def materias_ofertadas():
    estudiantes = obtener_estudiantes()
    materias = set()
    for estudiante in estudiantes:
        materias.update(estudiante.materias)
    return materias

def estudiantes_en_comun(id_a, id_b):
    estudiante_a = obtener_por_id(id_a)
    estudiante_b = obtener_por_id(id_b)
    if estudiante_a is None:
        return False, "No existe el primer estudiante"
    if estudiante_b is None:
        return False, "No existe el segundo estudiante"
    materias = estudiante_a.materias_en_comun(estudiante_b)
    return True, materias