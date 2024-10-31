"""Crear un menú de opciones en el main.py que permita
desarrollar las siguientes tareas llamando a funciones
modularizadas en otros archivos.
1- Cargar secuencialmente una lista de alumnos, cada alumno
debe ser un diccionario con cuatro claves: nombre, apellido, edad y
la clave curso que posea de valor una tupla con el curso.
2- Cargar secuencialmente una lista de cursos, cada curso debe
ser un diccionario con dos claves: una tupla que contenga año y
división, debe tener cargada como valor la cantidad de alumnos y
el preceptor a cargo.
3- Generar un set de preceptores para cada año
4- Obtener promedio de edad de un determinado curso.
5- Buscar qué preceptores se encuentran repetidos en dos años
distintos.
6- Buscar qué preceptores se encuentran solo en un determinado
año.
7- Mostrar nombre y apellido del alumno más jóven y más grande
del colegio."""


# 1. Cargar secuencialmente una lista de alumnos
alumnos = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 15, "curso": ("1º", "A")},
    {"nombre": "María", "apellido": "López", "edad": 14, "curso": ("1º", "B")},
    {"nombre": "Ana", "apellido": "García", "edad": 16, "curso": ("2º", "A")},
    {"nombre": "Luis", "apellido": "Martínez", "edad": 17, "curso": ("2º", "B")},
    {"nombre": "Elena", "apellido": "Gómez", "edad": 13, "curso": ("1º", "A")},
]

# 2. Cargar secuencialmente una lista de cursos
cursos = [
    {("1º", "A"): {"cantidad_alumnos": 2, "preceptor": "Sra. Rodríguez"}},
    {("1º", "B"): {"cantidad_alumnos": 1, "preceptor": "Sr. González"}},
    {("2º", "A"): {"cantidad_alumnos": 1, "preceptor": "Sra. Rodríguez"}},
    {("2º", "B"): {"cantidad_alumnos": 1, "preceptor": "Sra. Fernández"}},
]

# 3. Generar una lista de preceptores para cada año
preceptores_por_año = {}
for curso in cursos:
    for (año, div), datos in curso.items():
        if año not in preceptores_por_año:
            preceptores_por_año[año] = []
        if datos["preceptor"] not in preceptores_por_año[año]:
            preceptores_por_año[año].append(datos["preceptor"])

# 4. Obtener promedio de edad de un determinado curso
def promedio_edad(curso):
    alumnos_curso = [alumno["edad"] for alumno in alumnos if alumno["curso"] == curso]
    return sum(alumnos_curso) / len(alumnos_curso) if alumnos_curso else 0

# 5. Buscar qué preceptores se encuentran repetidos en dos años distintos
preceptores_repetidos = []
todos_preceptores = []
for año, preceptores in preceptores_por_año.items():
    for preceptor in preceptores:
        if preceptor in todos_preceptores and preceptor not in preceptores_repetidos:
            preceptores_repetidos.append(preceptor)
        else:
            todos_preceptores.append(preceptor)

# 6. Buscar qué preceptores se encuentran solo en un determinado año
preceptores_unicos = {}
for año, preceptores in preceptores_por_año.items():
    preceptores_unicos[año] = [preceptor for preceptor in preceptores if preceptor not in preceptores_repetidos]

# 7. Mostrar nombre y apellido del alumno más joven y más grande del colegio
alumno_mas_joven = min(alumnos, key=lambda alumno: alumno["edad"])
alumno_mas_grande = max(alumnos, key=lambda alumno: alumno["edad"])

# Resultados
print("Lista de preceptores por año:", preceptores_por_año)
print("Promedio de edad del curso 1º A:", promedio_edad(("1º", "A")))
print("Preceptores repetidos en distintos años:", preceptores_repetidos)
print("Preceptores únicos por año:", preceptores_unicos)
print("Alumno más joven:", alumno_mas_joven["nombre"], alumno_mas_joven["apellido"])
print("Alumno más grande:", alumno_mas_grande["nombre"], alumno_mas_grande["apellido"])