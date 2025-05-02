""" Desafío: Gestionar el Equipo de Fútbol Argentino 󰳕
Historia:
Tu tarea es gestionar el equipo titular el próximo partido. El equipo tiene una matriz de jugadores
organizada en 11 filas (representando a los titulares del próximo partido) y 5 columnas (Nombre,
Apellido, posición en la que juega, cantidad de goles en el torneo). Necesitamos que puedas:
1. Cargar los datos de los jugadores en la matriz (nombre, edad, goles, etc).
2. Mostrar la matriz con la información de todos los jugadores.
3. Modificar un jugador: Cambiar la información de un jugador seleccionando su fila y
columna.
Objetivos del programa:
1. Menú con las siguientes opciones:
○ 1. Pedir datos para cargar la matriz: Ingresar los datos de los jugadores (nombre,
edad, goles) para cada celda de la matriz.
○ 2. Mostrar matriz: Ver la matriz con la información de todos los jugadores.
○ 3. Modificar matriz: Mostrar la matriz, pedir la fila y columna a modificar, y luego
ingresar el nuevo dato.
○ 4. Salir: Finalizar el programa.
Requisitos técnicos:
● Usar matrices (arrays bidimensionales).
● Usar ciclos para recorrer la matriz.
● Usar funciones y separarlas en un archivo aparte, importando desde el main.
● Implementar un menú con opciones para interactuar con el usuario.
● Para la modificación, mostrar la matriz y pedir al usuario que ingrese la fila y columna a
modificar, luego el nuevo dato."""

# equipo_futbol.py

def cargar_matriz():
    matriz = []
    for i in range(11):
        jugador = []
        print(f"\nIngresando datos para el jugador {i + 1}:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        posicion = input("Posición: ")
        edad = input("Edad: ")
        goles = input("Cantidad de goles en el torneo: ")
        jugador.extend([nombre, apellido, posicion, edad, goles])
        matriz.append(jugador)
    return matriz

def mostrar_matriz(matriz):
    print("\nEquipo titular:")
    print("{:<15} {:<15} {:<15} {:<10} {:<10}".format("Nombre", "Apellido", "Posición", "Edad", "Goles"))
    print("-" * 65)
    for jugador in matriz:
        print("{:<15} {:<15} {:<15} {:<10} {:<10}".format(*jugador))

def modificar_matriz(matriz):
    mostrar_matriz(matriz)
    try:
        fila = int(input("\nIngrese el número de jugador (fila 1-11) que desea modificar: ")) - 1
        columna = int(input("Ingrese el número de dato a modificar:\n0-Nombre\n1-Apellido\n2-Posición\n3-Edad\n4-Goles\nOpción: "))
        
        if 0 <= fila < 11 and 0 <= columna < 5:
            nuevo_dato = input("Ingrese el nuevo dato: ")
            matriz[fila][columna] = nuevo_dato
            print("\nDato actualizado correctamente.")
        else:
            print("Fila o columna fuera de rango.")
    except ValueError:
        print("Entrada inválida. Debe ingresar números.")

def menu():
    matriz = []
    while True:
        print("\n--- Menú de Gestión del Equipo de Fútbol ---")
        print("1. Cargar datos de jugadores")
        print("2. Mostrar matriz")
        print("3. Modificar datos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            matriz = cargar_matriz()
        elif opcion == "2":
            if matriz:
                mostrar_matriz(matriz)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "3":
            if matriz:
                modificar_matriz(matriz)
            else:
                print("Primero debe cargar los datos.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()


