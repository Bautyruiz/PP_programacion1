"""Guía de ejercicios
“Funciones”
1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima un
saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función.
2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma, resta y
multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la función.
3. Definir una función area_triangulo(base, altura) que reciba la base y la altura de un triángulo y
devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado. Fórmul: area =
(b * h) / 2.
4. Crear una función mayor(num1, num2, num3) que reciba tres números y devuelva el mayor. Luego,
el programa debe pedir los números y mostrar el resultado.
5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si es
impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función.
6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y muestre
cuántas horas y minutos sobran.
7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si es
mayor de edad (18 años o más). Luego, el programa debe pedir la edad al usuario y mostrar un
mensaje apropiado.
8. Crear una función calcular_jornal(ventas, porcentaje) que reciba el monto de ventas de un
empleado y el porcentaje de comisión que le corresponde. La función debe devolver el monto de
comisión. Modificar el programa de Don Eusebio que se comenzó en la guía de secuenciales y
continuó en la de ciclos para implementar esta función. Verificar que se usen ciclos siempre que
corresponda.
9. Modificar el punto 6 de la guía de ciclos para que cada operación que se elija tenga su respectiva
función con las mismas especificaciones que el punto pide.
10. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y
devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el
año de nacimiento del usuario y mostrar la edad calculada."""

#1                                                                       
def saludar(nombre):
    print(f"¡Hola, {nombre}! ¿Cómo estás?")

# Pedimos el nombre al usuario
nombre_usuario = input("Por favor, ingresa tu nombre: ")

# Llamamos a la función con el nombre ingresado
saludar(nombre_usuario)

#Explicación:
#def saludar(nombre): → Define una función que recibe un parámetro nombre.
#input("...") → Solicita al usuario que escriba su nombre.
#saludar(nombre_usuario) → Llama a la función usando el nombre ingresado.

#2
def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")

# Pedimos dos números al usuario
numero1 = float(input("Ingresá el primer número: "))
numero2 = float(input("Ingresá el segundo número: "))

# Llamamos a la función
operaciones(numero1, numero2)

# Explicación:
#Se usa float() para permitir números con decimales, pero si solo querés enteros, podés usar int().
#La función calcula y muestra las tres operaciones básicas.

#3
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Pedimos los valores al usuario
base = float(input("Ingresá la base del triángulo: "))
altura = float(input("Ingresá la altura del triángulo: "))

# Llamamos a la función y mostramos el resultado
resultado = area_triangulo(base, altura)
print(f"El área del triángulo es: {resultado}")

#Explicación:
#return area: devuelve el valor calculado para que pueda ser usado fuera de la función.
#Luego, el resultado se guarda en la variable resultado y se muestra al usuario.

#4
def mayor(num1, num2, num3):
    return max(num1, num2, num3)

# Pedimos los números al usuario
n1 = float(input("Ingresá el primer número: "))
n2 = float(input("Ingresá el segundo número: "))
n3 = float(input("Ingresá el tercer número: "))

# Llamamos a la función y mostramos el mayor
resultado = mayor(n1, n2, n3)
print(f"El número mayor es: {resultado}")

#Explicación:
#Usamos la función incorporada max() para simplificar y encontrar el mayor de los tres números.
#Si querés hacerlo "a mano", también se puede comparar con condicionales (if), pero max es más limpio.

#5
def es_par(numero):
    return numero % 2 == 0

# Pedimos un número al usuario
numero = int(input("Ingresá un número: "))

# Usamos la función para verificar si es par
if es_par(numero):
    print("El número es par.")
else:
    print("El número es impar.")

#Explicación:
#numero % 2 == 0: si el resto de dividir por 2 es 0, entonces es par.
#La función devuelve True o False, y usamos un if para mostrar el mensaje correspondiente.

#6
def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    print(f"{minutos} minutos son {horas} hora(s) y {minutos_restantes} minuto(s).")

# Pedimos la cantidad de minutos al usuario
minutos_ingresados = int(input("Ingresá la cantidad de minutos: "))

# Llamamos a la función
convertir_minutos(minutos_ingresados)

#Explicación:
# // → división entera (cuántas veces entra 60 en los minutos).
# % → resto de la división (minutos que sobran).
# Se muestra un mensaje con la conversión.

#7
def verificar_acceso(edad):
    if edad >= 18:
        print("Acceso permitido. Sos mayor de edad.")
    else:
        print("Acceso denegado. Sos menor de edad.")

# Pedimos la edad al usuario
edad_usuario = int(input("Ingresá tu edad: "))

# Llamamos a la función
verificar_acceso(edad_usuario)

#Explicación:
#Se usa una estructura if/else dentro de la función para verificar si la edad es mayor o igual a 18.
#Se muestra un mensaje según el caso.

#8
def calcular_jornal(ventas, porcentaje):
    return ventas * (porcentaje / 100)

# Pedimos cuántos empleados hay
cantidad_empleados = int(input("¿Cuántos empleados desea procesar, Don Eusebio? "))

for i in range(cantidad_empleados):
    print(f"\nEmpleado {i + 1}:")
    ventas = float(input("  Ingresá el monto total de ventas: "))
    porcentaje = float(input("  Ingresá el porcentaje de comisión (%): "))

    comision = calcular_jornal(ventas, porcentaje)
    print(f"  La comisión correspondiente es: ${comision:.2f}")

#Explicación:
#La función calcular_jornal() hace el cálculo y devuelve el resultado.
#El for permite procesar a varios empleados de forma dinámica.
#El programa es claro, limpio y reutiliza la lógica gracias a la función.

#9
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

# Menú con ciclo
while True:
    print("\n--- Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elegí una opción (1-5): ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    # Pedir los dos números
    num1 = float(input("Ingresá el primer número: "))
    num2 = float(input("Ingresá el segundo número: "))

    # Ejecutar según la opción
    if opcion == "1":
        print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == "2":
        print(f"Resultado: {restar(num1, num2)}")
    elif opcion == "3":
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcion == "4":
        resultado = dividir(num1, num2)
        print(f"Resultado: {resultado}")
    else:
        print("Opción inválida. Por favor, elegí entre 1 y 5.")

#Claves del ejercicio:
#Cada operación tiene su función dedicada.
#El menú se repite hasta que el usuario elige salir (opción 5).
#Se verifica que no haya división por cero.
#Es un ejemplo claro de cómo usar modularización + ciclos

#10
from datetime import datetime

def calcular_edad(anio_nacimiento):
    anio_actual = datetime.now().year
    return anio_actual - anio_nacimiento

# Pedimos el año de nacimiento al usuario
anio = int(input("Ingresá tu año de nacimiento: "))

# Llamamos a la función y mostramos la edad
edad = calcular_edad(anio)
print(f"Tu edad es: {edad} años.")

#datetime.now().year obtiene automáticamente el año actual.
#La función calcula la diferencia entre el año actual y el de nacimiento.
#No se tiene en cuenta si el usuario ya cumplió años este año o no, como pide el enunciado.
