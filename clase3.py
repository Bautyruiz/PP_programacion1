"""Vas a desarrollar un programa que permita al usuario realizar operaciones matemáticas básicas: suma, resta,
multiplicación y división.
1. Creá un archivo llamado operaciones.py, que contendrá las siguientes funciones:
○ sumar(a, b)
○ restar(a, b)
○ multiplicar(a, b)
○ dividir(a, b) → esta función debe validar que el segundo número no sea cero. En ese caso, debe
devolver un mensaje de error.
2. Creá otro archivo llamado main.py, que cumpla estas funciones:
○ Muestre un menú para que el usuario elija qué operación desea realizar.
○ Solicite al usuario dos números (pueden ser enteros o decimales).
○ Llame a la función correspondiente (importada desde el módulo operaciones).
○ Muestre el resultado.
○ El programa debe repetirse hasta que el usuario elija la opción de salir."""

#operaciones.py

# operaciones.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero."
    else:
        return a / b
    

# main.py

import operaciones.

def mostrar_menu():
    print("\n=== Calculadora básica ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def pedir_numeros():
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            return a, b
        except ValueError:
            print("Entrada inválida. Por favor ingrese números válidos.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion in ["1", "2", "3", "4"]:
            a, b = pedir_numeros()

            if opcion == "1":
                resultado = operaciones.sumar(a, b)
            elif opcion == "2":
                resultado = operaciones.restar(a, b)
            elif opcion == "3":
                resultado = operaciones.multiplicar(a, b)
            elif opcion == "4":
                resultado = operaciones.dividir(a, b)

            print(f"Resultado: {resultado}")
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()





"""def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero."
    else:
        return a / b

def mostrar_menu():
    print("\n=== Calculadora básica ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def pedir_numeros():
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            return a, b
        except ValueError:
            print("Entrada inválida. Por favor ingrese números válidos.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion in ["1", "2", "3", "4"]:
            a, b = pedir_numeros()

            if opcion == "1":
                resultado = sumar(a, b)
            elif opcion == "2":
                resultado = restar(a, b)
            elif opcion == "3":
                resultado = multiplicar(a, b)
            elif opcion == "4":
                resultado = dividir(a, b)

            print(f"Resultado: {resultado}")
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

#Este programa maneja entradas inválidas con try-except para que no se rompa si el usuario ingresa algo que no es un número.
#La división por cero está controlada en la función dividir."""