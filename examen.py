""""
Una empresa se dedica al almacenamiento y posterior distribución de artículos de limpieza
en el interior del país. Para ello cuentan con 3 depósitos distribuidos en diferentes
provincias (PBA, Jujuy y Neuquén).
Los depósitos pueden almacenar 7 tipos diferentes de artículos: químicos, trapos, escobas,
cepillos, papel higiénico, jabón y pañuelos descartables.
La oficina central, recibe mensualmente una planilla de existencias donde se indican las
existencias de cada juguete para cada depósito.
Realizar un menú de opciones:
1. Obtener existencias: para ello deberá cargar en el main la existencia de cada artículo
en todos los depósitos. En una lista de cantidad, no uno por uno. Por lo que habrá una
matriz con 3 columnas o filas, provincia, tipo de artículo y cantidad.
2. Calcular por cada depósito la cantidad total de artículos almacenados entre todos los
tipos.
3. Obtener los nombres de los artículos que es necesario reponer en cada depósito.
Crear una función que devuelva todos los juguetes con menos de 3000 unidades.
4. Máxima cantidad de artículos almacenados de cada tipo. Devolver en qué provincia se
encuentran por si es necesario redistribuir.
5. Generar una función que permita corregir un error de carga mediante carga aleatoria o
distribuida de matrices.
6. Cantidad de depósitos que hayan almacenado más de 3.000.000 de unidades entre
los 7 artículos. Mostrar provincias.
7. Porcentaje de artículos de cada tipo sobre el total de artículos almacenados. Realizar
una función que muestre el porcentaje de cada uno.
8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor
usando bubble sort o selection sort. Justificar la elección del algoritmo. Para ello la
función deberá recibir una matriz de ventas, y una lista de precios.
9. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector
con los valores por unidad de artículo. Esto se debe hacer con una función que reciba
la lista de precios por parámetro para poder actualizarlos frente a la inflación.
"""

#1
# Definición de constantes
DEPOSITOS = ["PBA", "Jujuy", "Neuquén"]
ARTICULOS = ["químicos", "trapos", "escobas", "cepillos", "papel higiénico", "jabón", "pañuelos descartables"]
NUM_ARTICULOS = len(ARTICULOS)
NUM_DEPOSITOS = len(DEPOSITOS)

# Inicializar matriz de existencias
existencias = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]

# Función para cargar existencias
def cargar_existencias():
    print("Ingrese las existencias para cada depósito:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        # Cargar existencias de todos los artículos
        cantidades = list(map(int, input(f"Ingrese las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Asegurarse de que se ingresen 7 cantidades
        while len(cantidades) != NUM_ARTICULOS:
            print(f"Error: debe ingresar exactamente {NUM_ARTICULOS} cantidades.")
            cantidades = list(map(int, input(f"Ingrese nuevamente las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Almacenar en la matriz
        existencias[i] = cantidades

# Función para mostrar existencias
def mostrar_existencias():
    print("\nExistencias en los depósitos:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        for j in range(NUM_ARTICULOS):
            print(f"{ARTICULOS[j]}: {existencias[i][j]}")

# Menú principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Obtener existencias")
        print("2. Mostrar existencias")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_existencias()
        elif opcion == 2:
            mostrar_existencias()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#2
# Definición de constantes
DEPOSITOS = ["PBA", "Jujuy", "Neuquén"]
ARTICULOS = ["químicos", "trapos", "escobas", "cepillos", "papel higiénico", "jabón", "pañuelos descartables"]
NUM_ARTICULOS = len(ARTICULOS)
NUM_DEPOSITOS = len(DEPOSITOS)

# Inicializar matriz de existencias
existencias = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]

# Función para cargar existencias
def cargar_existencias():
    print("Ingrese las existencias para cada depósito:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        # Cargar existencias de todos los artículos
        cantidades = list(map(int, input(f"Ingrese las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Asegurarse de que se ingresen 7 cantidades
        while len(cantidades) != NUM_ARTICULOS:
            print(f"Error: debe ingresar exactamente {NUM_ARTICULOS} cantidades.")
            cantidades = list(map(int, input(f"Ingrese nuevamente las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Almacenar en la matriz
        existencias[i] = cantidades

# Función para mostrar existencias
def mostrar_existencias():
    print("\nExistencias en los depósitos:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        for j in range(NUM_ARTICULOS):
            print(f"{ARTICULOS[j]}: {existencias[i][j]}")

# Función para calcular total de artículos por depósito
def total_articulos_por_deposito():
    print("\nTotal de artículos almacenados por depósito:")
    for i in range(NUM_DEPOSITOS):
        total = sum(existencias[i])
        print(f"Total en {DEPOSITOS[i]}: {total}")

# Menú principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Obtener existencias")
        print("2. Mostrar existencias")
        print("3. Calcular total de artículos por depósito")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_existencias()
        elif opcion == 2:
            mostrar_existencias()
        elif opcion == 3:
            total_articulos_por_deposito()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#3
# Definición de constantes
DEPOSITOS = ["PBA", "Jujuy", "Neuquén"]
ARTICULOS = ["químicos", "trapos", "escobas", "cepillos", "papel higiénico", "jabón", "pañuelos descartables"]
NUM_ARTICULOS = len(ARTICULOS)
NUM_DEPOSITOS = len(DEPOSITOS)

# Inicializar matriz de existencias
existencias = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]

# Función para cargar existencias
def cargar_existencias():
    print("Ingrese las existencias para cada depósito:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        # Cargar existencias de todos los artículos
        cantidades = list(map(int, input(f"Ingrese las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Asegurarse de que se ingresen 7 cantidades
        while len(cantidades) != NUM_ARTICULOS:
            print(f"Error: debe ingresar exactamente {NUM_ARTICULOS} cantidades.")
            cantidades = list(map(int, input(f"Ingrese nuevamente las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Almacenar en la matriz
        existencias[i] = cantidades

# Función para mostrar existencias
def mostrar_existencias():
    print("\nExistencias en los depósitos:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        for j in range(NUM_ARTICULOS):
            print(f"{ARTICULOS[j]}: {existencias[i][j]}")

# Función para calcular total de artículos por depósito
def total_articulos_por_deposito():
    print("\nTotal de artículos almacenados por depósito:")
    for i in range(NUM_DEPOSITOS):
        total = sum(existencias[i])
        print(f"Total en {DEPOSITOS[i]}: {total}")

# Función para obtener artículos a reponer
def obtener_articulos_a_reponer():
    print("\nArtículos que necesitan ser repuestos en cada depósito:")
    for i in range(NUM_DEPOSITOS):
        a_reponer = [ARTICULOS[j] for j in range(NUM_ARTICULOS) if existencias[i][j] < 3000]
        if a_reponer:
            print(f"{DEPOSITOS[i]}: {', '.join(a_reponer)}")
        else:
            print(f"{DEPOSITOS[i]}: No necesita reponer artículos.")

# Menú principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Obtener existencias")
        print("2. Mostrar existencias")
        print("3. Calcular total de artículos por depósito")
        print("4. Obtener artículos a reponer")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_existencias()
        elif opcion == 2:
            mostrar_existencias()
        elif opcion == 3:
            total_articulos_por_deposito()
        elif opcion == 4:
            obtener_articulos_a_reponer()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#4
# Definición de constantes
DEPOSITOS = ["PBA", "Jujuy", "Neuquén"]
ARTICULOS = ["químicos", "trapos", "escobas", "cepillos", "papel higiénico", "jabón", "pañuelos descartables"]
NUM_ARTICULOS = len(ARTICULOS)
NUM_DEPOSITOS = len(DEPOSITOS)

# Inicializar matriz de existencias
existencias = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]

# Función para cargar existencias
def cargar_existencias():
    print("Ingrese las existencias para cada depósito:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        # Cargar existencias de todos los artículos
        cantidades = list(map(int, input(f"Ingrese las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Asegurarse de que se ingresen 7 cantidades
        while len(cantidades) != NUM_ARTICULOS:
            print(f"Error: debe ingresar exactamente {NUM_ARTICULOS} cantidades.")
            cantidades = list(map(int, input(f"Ingrese nuevamente las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Almacenar en la matriz
        existencias[i] = cantidades

# Función para mostrar existencias
def mostrar_existencias():
    print("\nExistencias en los depósitos:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        for j in range(NUM_ARTICULOS):
            print(f"{ARTICULOS[j]}: {existencias[i][j]}")

# Función para calcular total de artículos por depósito
def total_articulos_por_deposito():
    print("\nTotal de artículos almacenados por depósito:")
    for i in range(NUM_DEPOSITOS):
        total = sum(existencias[i])
        print(f"Total en {DEPOSITOS[i]}: {total}")

# Función para obtener artículos a reponer
def obtener_articulos_a_reponer():
    print("\nArtículos que necesitan ser repuestos en cada depósito:")
    for i in range(NUM_DEPOSITOS):
        a_reponer = [ARTICULOS[j] for j in range(NUM_ARTICULOS) if existencias[i][j] < 3000]
        if a_reponer:
            print(f"{DEPOSITOS[i]}: {', '.join(a_reponer)}")
        else:
            print(f"{DEPOSITOS[i]}: No necesita reponer artículos.")

# Función para obtener máxima cantidad de artículos almacenados de cada tipo
def maxima_cantidad_articulos():
    print("\nMáxima cantidad de artículos almacenados de cada tipo:")
    for j in range(NUM_ARTICULOS):
        max_cantidad = 0
        provincia = ""
        for i in range(NUM_DEPOSITOS):
            if existencias[i][j] > max_cantidad:
                max_cantidad = existencias[i][j]
                provincia = DEPOSITOS[i]
        print(f"{ARTICULOS[j]}: {max_cantidad} en {provincia}")

# Menú principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Obtener existencias")
        print("2. Mostrar existencias")
        print("3. Calcular total de artículos por depósito")
        print("4. Obtener artículos a reponer")
        print("5. Máxima cantidad de artículos almacenados de cada tipo")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_existencias()
        elif opcion == 2:
            mostrar_existencias()
        elif opcion == 3:
            total_articulos_por_deposito()
        elif opcion == 4:
            obtener_articulos_a_reponer()
        elif opcion == 5:
            maxima_cantidad_articulos()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#5
import random

# Definición de constantes
DEPOSITOS = ["PBA", "Jujuy", "Neuquén"]
ARTICULOS = ["químicos", "trapos", "escobas", "cepillos", "papel higiénico", "jabón", "pañuelos descartables"]
NUM_ARTICULOS = len(ARTICULOS)
NUM_DEPOSITOS = len(DEPOSITOS)

# Inicializar matriz de existencias
existencias = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]

# Función para cargar existencias
def cargar_existencias():
    print("Ingrese las existencias para cada depósito:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        # Cargar existencias de todos los artículos
        cantidades = list(map(int, input(f"Ingrese las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Asegurarse de que se ingresen 7 cantidades
        while len(cantidades) != NUM_ARTICULOS:
            print(f"Error: debe ingresar exactamente {NUM_ARTICULOS} cantidades.")
            cantidades = list(map(int, input(f"Ingrese nuevamente las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Almacenar en la matriz
        existencias[i] = cantidades

# Función para mostrar existencias
def mostrar_existencias():
    print("\nExistencias en los depósitos:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        for j in range(NUM_ARTICULOS):
            print(f"{ARTICULOS[j]}: {existencias[i][j]}")

# Función para calcular total de artículos por depósito
def total_articulos_por_deposito():
    print("\nTotal de artículos almacenados por depósito:")
    for i in range(NUM_DEPOSITOS):
        total = sum(existencias[i])
        print(f"Total en {DEPOSITOS[i]}: {total}")

# Función para obtener artículos a reponer
def obtener_articulos_a_reponer():
    print("\nArtículos que necesitan ser repuestos en cada depósito:")
    for i in range(NUM_DEPOSITOS):
        a_reponer = [ARTICULOS[j] for j in range(NUM_ARTICULOS) if existencias[i][j] < 3000]
        if a_reponer:
            print(f"{DEPOSITOS[i]}: {', '.join(a_reponer)}")
        else:
            print(f"{DEPOSITOS[i]}: No necesita reponer artículos.")

# Función para obtener máxima cantidad de artículos almacenados de cada tipo
def maxima_cantidad_articulos():
    print("\nMáxima cantidad de artículos almacenados de cada tipo:")
    for j in range(NUM_ARTICULOS):
        max_cantidad = 0
        provincia = ""
        for i in range(NUM_DEPOSITOS):
            if existencias[i][j] > max_cantidad:
                max_cantidad = existencias[i][j]
                provincia = DEPOSITOS[i]
        print(f"{ARTICULOS[j]}: {max_cantidad} en {provincia}")

# Función para corregir errores de carga con carga aleatoria
def corregir_errores_carga_aleatoria():
    print("\nCorrigiendo errores de carga con valores aleatorios...")
    for i in range(NUM_DEPOSITOS):
        for j in range(NUM_ARTICULOS):
            # Asignar una cantidad aleatoria entre 1000 y 5000
            existencias[i][j] = random.randint(1000, 5000)
    print("Carga corregida con valores aleatorios.")

# Menú principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Obtener existencias")
        print("2. Mostrar existencias")
        print("3. Calcular total de artículos por depósito")
        print("4. Obtener artículos a reponer")
        print("5. Máxima cantidad de artículos almacenados de cada tipo")
        print("6. Corregir errores de carga con carga aleatoria")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_existencias()
        elif opcion == 2:
            mostrar_existencias()
        elif opcion == 3:
            total_articulos_por_deposito()
        elif opcion == 4:
            obtener_articulos_a_reponer()
        elif opcion == 5:
            maxima_cantidad_articulos()
        elif opcion == 6:
            corregir_errores_carga_aleatoria()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#6
import random

# Definición de constantes
DEPOSITOS = ["PBA", "Jujuy", "Neuquén"]
ARTICULOS = ["químicos", "trapos", "escobas", "cepillos", "papel higiénico", "jabón", "pañuelos descartables"]
NUM_ARTICULOS = len(ARTICULOS)
NUM_DEPOSITOS = len(DEPOSITOS)

# Inicializar matriz de existencias
existencias = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]

# Función para cargar existencias
def cargar_existencias():
    print("Ingrese las existencias para cada depósito:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        # Cargar existencias de todos los artículos
        cantidades = list(map(int, input(f"Ingrese las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Asegurarse de que se ingresen 7 cantidades
        while len(cantidades) != NUM_ARTICULOS:
            print(f"Error: debe ingresar exactamente {NUM_ARTICULOS} cantidades.")
            cantidades = list(map(int, input(f"Ingrese nuevamente las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Almacenar en la matriz
        existencias[i] = cantidades

# Función para mostrar existencias
def mostrar_existencias():
    print("\nExistencias en los depósitos:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        for j in range(NUM_ARTICULOS):
            print(f"{ARTICULOS[j]}: {existencias[i][j]}")

# Función para calcular total de artículos por depósito
def total_articulos_por_deposito():
    print("\nTotal de artículos almacenados por depósito:")
    for i in range(NUM_DEPOSITOS):
        total = sum(existencias[i])
        print(f"Total en {DEPOSITOS[i]}: {total}")

# Función para obtener artículos a reponer
def obtener_articulos_a_reponer():
    print("\nArtículos que necesitan ser repuestos en cada depósito:")
    for i in range(NUM_DEPOSITOS):
        a_reponer = [ARTICULOS[j] for j in range(NUM_ARTICULOS) if existencias[i][j] < 3000]
        if a_reponer:
            print(f"{DEPOSITOS[i]}: {', '.join(a_reponer)}")
        else:
            print(f"{DEPOSITOS[i]}: No necesita reponer artículos.")

# Función para obtener máxima cantidad de artículos almacenados de cada tipo
def maxima_cantidad_articulos():
    print("\nMáxima cantidad de artículos almacenados de cada tipo:")
    for j in range(NUM_ARTICULOS):
        max_cantidad = 0
        provincia = ""
        for i in range(NUM_DEPOSITOS):
            if existencias[i][j] > max_cantidad:
                max_cantidad = existencias[i][j]
                provincia = DEPOSITOS[i]
        print(f"{ARTICULOS[j]}: {max_cantidad} en {provincia}")

# Función para corregir errores de carga con carga aleatoria
def corregir_errores_carga_aleatoria():
    print("\nCorrigiendo errores de carga con valores aleatorios...")
    for i in range(NUM_DEPOSITOS):
        for j in range(NUM_ARTICULOS):
            # Asignar una cantidad aleatoria entre 1000 y 5000
            existencias[i][j] = random.randint(1000, 5000)
    print("Carga corregida con valores aleatorios.")

# Función para contar depósitos que almacenaron más de 3.000.000 unidades
def contar_depositos_mas_de_3_millones():
    print("\nDepósitos que han almacenado más de 3.000.000 de unidades:")
    for i in range(NUM_DEPOSITOS):
        total = sum(existencias[i])
        if total > 3000000:
            print(f"{DEPOSITOS[i]}: Total de unidades almacenadas: {total}")

# Menú principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Obtener existencias")
        print("2. Mostrar existencias")
        print("3. Calcular total de artículos por depósito")
        print("4. Obtener artículos a reponer")
        print("5. Máxima cantidad de artículos almacenados de cada tipo")
        print("6. Corregir errores de carga con carga aleatoria")
        print("7. Contar depósitos con más de 3.000.000 unidades")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_existencias()
        elif opcion == 2:
            mostrar_existencias()
        elif opcion == 3:
            total_articulos_por_deposito()
        elif opcion == 4:
            obtener_articulos_a_reponer()
        elif opcion == 5:
            maxima_cantidad_articulos()
        elif opcion == 6:
            corregir_errores_carga_aleatoria()
        elif opcion == 7:
            contar_depositos_mas_de_3_millones()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#7
import random

# Definición de constantes
DEPOSITOS = ["PBA", "Jujuy", "Neuquén"]
ARTICULOS = ["químicos", "trapos", "escobas", "cepillos", "papel higiénico", "jabón", "pañuelos descartables"]
NUM_ARTICULOS = len(ARTICULOS)
NUM_DEPOSITOS = len(DEPOSITOS)

# Inicializar matriz de existencias
existencias = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]

# Función para cargar existencias
def cargar_existencias():
    print("Ingrese las existencias para cada depósito:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        # Cargar existencias de todos los artículos
        cantidades = list(map(int, input(f"Ingrese las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Asegurarse de que se ingresen 7 cantidades
        while len(cantidades) != NUM_ARTICULOS:
            print(f"Error: debe ingresar exactamente {NUM_ARTICULOS} cantidades.")
            cantidades = list(map(int, input(f"Ingrese nuevamente las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Almacenar en la matriz
        existencias[i] = cantidades

# Función para mostrar existencias
def mostrar_existencias():
    print("\nExistencias en los depósitos:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        for j in range(NUM_ARTICULOS):
            print(f"{ARTICULOS[j]}: {existencias[i][j]}")

# Función para calcular total de artículos por depósito
def total_articulos_por_deposito():
    print("\nTotal de artículos almacenados por depósito:")
    for i in range(NUM_DEPOSITOS):
        total = sum(existencias[i])
        print(f"Total en {DEPOSITOS[i]}: {total}")

# Función para obtener artículos a reponer
def obtener_articulos_a_reponer():
    print("\nArtículos que necesitan ser repuestos en cada depósito:")
    for i in range(NUM_DEPOSITOS):
        a_reponer = [ARTICULOS[j] for j in range(NUM_ARTICULOS) if existencias[i][j] < 3000]
        if a_reponer:
            print(f"{DEPOSITOS[i]}: {', '.join(a_reponer)}")
        else:
            print(f"{DEPOSITOS[i]}: No necesita reponer artículos.")

# Función para obtener máxima cantidad de artículos almacenados de cada tipo
def maxima_cantidad_articulos():
    print("\nMáxima cantidad de artículos almacenados de cada tipo:")
    for j in range(NUM_ARTICULOS):
        max_cantidad = 0
        provincia = ""
        for i in range(NUM_DEPOSITOS):
            if existencias[i][j] > max_cantidad:
                max_cantidad = existencias[i][j]
                provincia = DEPOSITOS[i]
        print(f"{ARTICULOS[j]}: {max_cantidad} en {provincia}")

# Función para corregir errores de carga con carga aleatoria
def corregir_errores_carga_aleatoria():
    print("\nCorrigiendo errores de carga con valores aleatorios...")
    for i in range(NUM_DEPOSITOS):
        for j in range(NUM_ARTICULOS):
            # Asignar una cantidad aleatoria entre 1000 y 5000
            existencias[i][j] = random.randint(1000, 5000)
    print("Carga corregida con valores aleatorios.")

# Función para contar depósitos que almacenaron más de 3.000.000 unidades
def contar_depositos_mas_de_3_millones():
    print("\nDepósitos que han almacenado más de 3.000.000 de unidades:")
    for i in range(NUM_DEPOSITOS):
        total = sum(existencias[i])
        if total > 3000000:
            print(f"{DEPOSITOS[i]}: Total de unidades almacenadas: {total}")

# Función para calcular y mostrar el porcentaje de artículos de cada tipo
def porcentaje_articulos_tipo():
    total_general = sum(sum(existencias[i]) for i in range(NUM_DEPOSITOS))
    
    if total_general == 0:
        print("\nNo hay artículos almacenados.")
        return

    print("\nPorcentaje de artículos de cada tipo sobre el total almacenado:")
    for j in range(NUM_ARTICULOS):
        total_articulo = sum(existencias[i][j] for i in range(NUM_DEPOSITOS))
        porcentaje = (total_articulo / total_general) * 100
        print(f"{ARTICULOS[j]}: {porcentaje:.2f}%")

# Menú principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Obtener existencias")
        print("2. Mostrar existencias")
        print("3. Calcular total de artículos por depósito")
        print("4. Obtener artículos a reponer")
        print("5. Máxima cantidad de artículos almacenados de cada tipo")
        print("6. Corregir errores de carga con carga aleatoria")
        print("7. Contar depósitos con más de 3.000.000 unidades")
        print("8. Porcentaje de artículos de cada tipo")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_existencias()
        elif opcion == 2:
            mostrar_existencias()
        elif opcion == 3:
            total_articulos_por_deposito()
        elif opcion == 4:
            obtener_articulos_a_reponer()
        elif opcion == 5:
            maxima_cantidad_articulos()
        elif opcion == 6:
            corregir_errores_carga_aleatoria()
        elif opcion == 7:
            contar_depositos_mas_de_3_millones()
        elif opcion == 8:
            porcentaje_articulos_tipo()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#8
import random

# Definición de constantes
DEPOSITOS = ["PBA", "Jujuy", "Neuquén"]
ARTICULOS = ["químicos", "trapos", "escobas", "cepillos", "papel higiénico", "jabón", "pañuelos descartables"]
NUM_ARTICULOS = len(ARTICULOS)
NUM_DEPOSITOS = len(DEPOSITOS)

# Inicializar matriz de existencias y ventas
existencias = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]
ventas = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]

# Lista de precios por artículo
precios = [100, 50, 75, 60, 30, 20, 10]  # Precios de los artículos

# Función para cargar existencias
def cargar_existencias():
    print("Ingrese las existencias para cada depósito:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        # Cargar existencias de todos los artículos
        cantidades = list(map(int, input(f"Ingrese las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Asegurarse de que se ingresen 7 cantidades
        while len(cantidades) != NUM_ARTICULOS:
            print(f"Error: debe ingresar exactamente {NUM_ARTICULOS} cantidades.")
            cantidades = list(map(int, input(f"Ingrese nuevamente las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Almacenar en la matriz
        existencias[i] = cantidades

# Función para cargar ventas (simuladas)
def cargar_ventas():
    for i in range(NUM_DEPOSITOS):
        for j in range(NUM_ARTICULOS):
            # Generar una venta aleatoria entre 100 y 1000 unidades
            ventas[i][j] = random.randint(100, 1000)

# Función para calcular recaudación por depósito
def calcular_recaudacion():
    recaudacion = []
    for i in range(NUM_DEPOSITOS):
        total_recaudacion = sum(ventas[i][j] * precios[j] for j in range(NUM_ARTICULOS))
        recaudacion.append((DEPOSITOS[i], total_recaudacion))
    return recaudacion

# Función para ordenar recaudación usando Bubble Sort
def bubble_sort(recaudacion):
    n = len(recaudacion)
    for i in range(n):
        for j in range(0, n-i-1):
            if recaudacion[j][1] < recaudacion[j+1][1]:  # Ordenar de mayor a menor
                recaudacion[j], recaudacion[j+1] = recaudacion[j+1], recaudacion[j]

# Función para generar el informe de recaudación
def informe_recaudacion():
    recaudacion = calcular_recaudacion()
    bubble_sort(recaudacion)
    
    print("\nInforme de Recaudación por Depósito (de mayor a menor):")
    for deposito, total in recaudacion:
        print(f"{deposito}: ${total:.2f}")

# Menú principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Obtener existencias")
        print("2. Mostrar existencias")
        print("3. Calcular total de artículos por depósito")
        print("4. Obtener artículos a reponer")
        print("5. Máxima cantidad de artículos almacenados de cada tipo")
        print("6. Corregir errores de carga con carga aleatoria")
        print("7. Contar depósitos con más de 3.000.000 unidades")
        print("8. Porcentaje de artículos de cada tipo")
        print("9. Generar informe de recaudación")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_existencias()
        elif opcion == 2:
            mostrar_existencias()
        elif opcion == 3:
            total_articulos_por_deposito()
        elif opcion == 4:
            obtener_articulos_a_reponer()
        elif opcion == 5:
            maxima_cantidad_articulos()
        elif opcion == 6:
            corregir_errores_carga_aleatoria()
        elif opcion == 7:
            contar_depositos_mas_de_3_millones()
        elif opcion == 8:
            porcentaje_articulos_tipo()
        elif opcion == 9:
            cargar_ventas()  # Cargar ventas antes de generar el informe
            informe_recaudacion()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

#9
import random

# Definición de constantes
DEPOSITOS = ["PBA", "Jujuy", "Neuquén"]
ARTICULOS = ["químicos", "trapos", "escobas", "cepillos", "papel higiénico", "jabón", "pañuelos descartables"]
NUM_ARTICULOS = len(ARTICULOS)
NUM_DEPOSITOS = len(DEPOSITOS)

# Inicializar matriz de existencias y ventas
existencias = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]
ventas = [[0] * NUM_ARTICULOS for _ in range(NUM_DEPOSITOS)]

# Lista de precios por artículo
precios = [100, 50, 75, 60, 30, 20, 10]  # Precios de los artículos

# Función para cargar existencias
def cargar_existencias():
    print("Ingrese las existencias para cada depósito:")
    for i in range(NUM_DEPOSITOS):
        print(f"\nDepósito: {DEPOSITOS[i]}")
        # Cargar existencias de todos los artículos
        cantidades = list(map(int, input(f"Ingrese las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Asegurarse de que se ingresen 7 cantidades
        while len(cantidades) != NUM_ARTICULOS:
            print(f"Error: debe ingresar exactamente {NUM_ARTICULOS} cantidades.")
            cantidades = list(map(int, input(f"Ingrese nuevamente las existencias de los artículos {ARTICULOS} separados por espacio: ").split()))
        # Almacenar en la matriz
        existencias[i] = cantidades

# Función para cargar ventas (simuladas)
def cargar_ventas():
    for i in range(NUM_DEPOSITOS):
        for j in range(NUM_ARTICULOS):
            # Generar una venta aleatoria entre 100 y 1000 unidades
            ventas[i][j] = random.randint(100, 1000)

# Función para calcular recaudación por depósito
def calcular_recaudacion(precios):
    recaudacion = []
    for i in range(NUM_DEPOSITOS):
        total_recaudacion = sum(ventas[i][j] * precios[j] for j in range(NUM_ARTICULOS))
        recaudacion.append((DEPOSITOS[i], total_recaudacion))
    return recaudacion

# Función para encontrar el depósito con mayor recaudación
def deposito_con_mayor_recaudacion(precios):
    recaudacion = calcular_recaudacion(precios)
    # Encontrar el depósito con la mayor recaudación
    deposito_maximo = max(recaudacion, key=lambda x: x[1])
    return deposito_maximo

# Función para ordenar recaudación usando Bubble Sort
def bubble_sort(recaudacion):
    n = len(recaudacion)
    for i in range(n):
        for j in range(0, n-i-1):
            if recaudacion[j][1] < recaudacion[j+1][1]:  # Ordenar de mayor a menor
                recaudacion[j], recaudacion[j+1] = recaudacion[j+1], recaudacion[j]

# Función para generar el informe de recaudación
def informe_recaudacion():
    recaudacion = calcular_recaudacion(precios)
    bubble_sort(recaudacion)
    
    print("\nInforme de Recaudación por Depósito (de mayor a menor):")
    for deposito, total in recaudacion:
        print(f"{deposito}: ${total:.2f}")

# Menú principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Obtener existencias")
        print("2. Mostrar existencias")
        print("3. Calcular total de artículos por depósito")
        print("4. Obtener artículos a reponer")
        print("5. Máxima cantidad de artículos almacenados de cada tipo")
        print("6. Corregir errores de carga con carga aleatoria")
        print("7. Contar depósitos con más de 3.000.000 unidades")
        print("8. Porcentaje de artículos de cada tipo")
        print("9. Generar informe de recaudación")
        print("10. Depósito con mayor recaudación")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_existencias()
        elif opcion == 2:
            mostrar_existencias()
        elif opcion == 3:
            total_articulos_por_deposito()
        elif opcion == 4:
            obtener_articulos_a_reponer()
        elif opcion == 5:
            maxima_cantidad_articulos()
        elif opcion == 6:
            corregir_errores_carga_aleatoria()
        elif opcion == 7:
            contar_depositos_mas_de_3_millones()
        elif opcion == 8:
            porcentaje_articulos_tipo()
        elif opcion == 9:
            cargar_ventas()  # Cargar ventas antes de generar el informe
            informe_recaudacion()
        elif opcion == 10:
            # Preguntar por los precios actualizados
            precios_actualizados = list(map(float, input("Ingrese los nuevos precios separados por espacio: ").split()))
            if len(precios_actualizados) != NUM_ARTICULOS:
                print(f"Error: debe ingresar exactamente {NUM_ARTICULOS} precios.")
            else:
                deposito_maximo = deposito_con_mayor_recaudacion(precios_actualizados)
                print(f"\nEl depósito con mayor recaudación es {deposito_maximo[0]} con un total de ${deposito_maximo[1]:.2f}.")
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()