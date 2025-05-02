"""Guia de ejercicios
“Vectores bidimensionales”
1. Cargar una matriz con datos de personas
Crear una matriz de 4 filas y 3 columnas. Cada fila representa una persona y cada columna representa:
nombre, edad y ciudad. Pedir al usuario que cargue los datos y mostrarlos con formato de tabla.
2. Contar cuántas personas tienen más de 30 años
Con una matriz previamente cargada con nombre, edad y ciudad, recorrer la matriz y contar cuántas
personas tienen más de 30 años. Mostrar el total.
3. Buscar una persona por nombre
Solicitar al usuario un nombre y recorrer la matriz para buscar si existe. Si lo encuentra, mostrar todos los
datos de esa persona. Si no, indicar que no existe.
4. Calcular el promedio de edades
A partir de una matriz cargada con personas, calcular y mostrar el promedio de edades. Hacer una función
calcular_promedio(matriz) que lo haga.
5. Contar cuántas personas viven en una ciudad específica
Pedir al usuario que ingrese una ciudad. Contar cuántas personas de la matriz viven allí. Mostrar el
resultado.
6. Mostrar la persona con mayor edad
Recorrer la matriz y determinar cuál es la persona con mayor edad. Mostrar todos sus datos.
7. Cambiar ciudad a "Desconocida" si la edad es menor a 18
Crear una función que recorra la matriz de personas y, para cada persona cuya edad sea menor a 18
años, reemplace el valor de la ciudad por "Desconocida". Mostrar luego la matriz modificada.
8. Cargar una matriz numérica 3x3 y mostrar la suma total
Solicitar al usuario que ingrese valores enteros en una matriz 3x3 y luego calcular y mostrar la suma total
de todos los elementos.
9. Determinar cuántos valores pares hay en una matriz numérica
Con la matriz del ejercicio anterior, contar cuántos valores son pares. Mostrar el total.
10. Matriz de asistencia (V/F)
Crear una matriz de 5 filas (alumnos) por 3 columnas (clases). Cargar manualmente los valores con "V" o
"F" (asistió o no asistió). Mostrar cuántos alumnos asistieron a todas las clases."""

#1
personas = []

for i in range(4):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    ciudad = input(f"Ingrese la ciudad de {nombre}: ")
    personas.append([nombre, edad, ciudad])

print("\nDatos cargados:")
print(f"{'Nombre':<10}{'Edad':<5}{'Ciudad'}")
for persona in personas:
    print(f"{persona[0]:<10}{persona[1]:<5}{persona[2]}")

#2
contador = 0
for persona in personas:
    if persona[1] > 30:
        contador += 1

print(f"\nCantidad de personas mayores de 30 años: {contador}")

#3
buscar_nombre = input("Ingrese el nombre a buscar: ")
encontrado = False

for persona in personas:
    if persona[0].lower() == buscar_nombre.lower():
        print(f"Datos encontrados: Nombre: {persona[0]}, Edad: {persona[1]}, Ciudad: {persona[2]}")
        encontrado = True
        break

if not encontrado:
    print("Persona no encontrada.")

#4
def calcular_promedio(matriz):
    total_edades = sum(persona[1] for persona in matriz)
    promedio = total_edades / len(matriz)
    return promedio

promedio_edades = calcular_promedio(personas)
print(f"\nEl promedio de edades es: {promedio_edades:.2f}")

#5
buscar_ciudad = input("Ingrese la ciudad a buscar: ")
contador = 0

for persona in personas:
    if persona[2].lower() == buscar_ciudad.lower():
        contador += 1

print(f"Cantidad de personas que viven en {buscar_ciudad}: {contador}")

#6
mayor = personas[0]

for persona in personas:
    if persona[1] > mayor[1]:
        mayor = persona

print(f"\nLa persona de mayor edad es {mayor[0]} con {mayor[1]} años y vive en {mayor[2]}.")

#7
def reemplazar_ciudad(matriz):
    for persona in matriz:
        if persona[1] < 18:
            persona[2] = "Desconocida"

reemplazar_ciudad(personas)

print("\nMatriz modificada:")
for persona in personas:
    print(persona)

#8
matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Ingrese el valor en posición ({i+1},{j+1}): "))
        fila.append(valor)
    matriz.append(fila)

suma_total = sum(sum(fila) for fila in matriz)
print(f"\nLa suma total de los elementos es: {suma_total}")

#9
pares = 0

for fila in matriz:
    for valor in fila:
        if valor % 2 == 0:
            pares += 1

print(f"\nCantidad de valores pares en la matriz: {pares}")

#10
asistencias = []

print("Ingrese 'V' (verdadero) si asistió o 'F' (falso) si no asistió:")
for i in range(5):
    fila = []
    for j in range(3):
        valor = input(f"Asistencia del alumno {i+1} en clase {j+1}: ").upper()
        while valor not in ['V', 'F']:
            valor = input("Valor inválido. Ingrese 'V' o 'F': ").upper()
        fila.append(valor)
    asistencias.append(fila)

asistieron_todo = 0

for fila in asistencias:
    if all(valor == 'V' for valor in fila):
        asistieron_todo += 1

print(f"\nCantidad de alumnos que asistieron a todas las clases: {asistieron_todo}")
