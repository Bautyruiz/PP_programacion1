"""Guia de ejercicios
“Ciclos”
1. Hacer un programa que pida ingresar números y corte cuando se ingresa cero. Luego imprimir por
pantalla al mayor de todos los ingresados
2. Hacer un programa que pida ingresar diez números e imprima el promedio de todos ellos.
3. Modificar el programa de Don Eusebio de la guía de secuenciales para que pueda ingresar una
cantidad indefinida de montos de ventas y no los totales diarios por cada empleado. El programa
debe pedir el monto de venta y el empleado que efectuó esa operación. Al final se debe mostrar lo
mismo que en el ejercicio de la guía de secuenciales y debe agregar al vendedor que más vendió.
4. Hacer un programa para ingresar un número e imprimir por pantalla si este es primo o no. Recordar
que los números primos son aquellos que solo son divisibles por uno y por si mismos.
5. Una encuestadora entrevistó gente solicitando los siguientes datos:
● Año de nacimiento
● Género (M-F-N)
● Ingreso mensual
● Estudio universitario (true o false)
Hacer un programa para ingresar los datos de la encuesta y luego mostrar por pantalla:
● Sueldo promedio de las personas que poseen estudio universitario
● Porcentaje de hombres con estudio universitario
● Porcentaje de mujeres con estudio universitario
● Edad de la persona más jóven que gane más de $800000
6. Hacer un programa que tenga un menú con las siguientes opciones:
● Sumar
● Restar
● Multiplicar
● Dividir
● Salir
Si se elige dividir debe pedir dos números y mostrar el resultado (recordar que no se puede dividir
por cero, si se ingresa cero volver al menú principal aclarando el motivo. Si se elige cualquiera de
las otras tres operaciones, permitir ingreso múltiple y mostrar el resultado.
Luego de mostrar resultado, sea la operación que sea, volver al menú.
7. Hacer un programa que permita ingresar ventas agrupadas por meses, es decir que las facturas
con dichos montos de venta de están agrupadas por meses. La cantidad de facturas por mes es
desconocida, el programa cambia de mes cuando se ingresa un importe negativo. Cuando se
termina de ingresar las facturas del mes se debe imprimir por pantalla el total facturado ese mes. Y
cuando se terminan de ingresar todas las facturas de todos los meses se debe mostrar por pantalla
el mes que más facturo y el promedio de venta mensual.
8. ACTIVIDAD PARCIAL (PARTIDA) FF: hacer un programa con un menú que contenga las siguientes
opciones:
● Jugar
● Instrucciones
● Estadísticas
● Salir
Cuando se selecciona una opción del menú se debe limpiar la consola y se debe mostrar la opción
que se seleccionó a modo de título. La opción salir debe terminar la ejecución.
NOTA: Actividad parcial no quiere decir que sea un exámen, sino que es parte de una actividad
más grande. FF es el nombre de la actividad.
9. Hacer un programa que permita elegir las siguientes opciones:
● Múltiplos
● Dobles por 3
● Mitad por 6
● Salir
Cuando se selecciona una opción el usuario debe ingresar números hasta que la condición deje de
cumplirse con respecto al último número ingresado, por ejemplo si elige múltiplos, empieza
ingresando un 6, luego un múltiplo de 6 que puede ser 12, a continuación, el número que se
ingrese debe ser múltiplo de este último, 48 y así sucesivamente. Cuando la condición deje de
cumplirse se debe volver al menú principal.
10. Hacer un programa que permita ingresar materias, entre sus datos se necesita el código de materia
(MA-01, MA,02…), su nombre, el código del cuatrimestre (CU-01, CU-02…) y la cantidad de
alumnos. Al finalizar el programa se debe saber cuantas materias tienen más de 30 alumnos, la
materia con más cantidad de alumnos.
Si en cada materia necesito un profesor cada 15 alumnos ¿cuántos profesores necesito contratar?
Imprimir por pantalla dicha cantidad (no importa cuántos por materias, sino el total)"""

#1
mayor = None

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    if (mayor is None) or (numero > mayor):
        mayor = numero

if mayor is not None:
    print(f"El mayor número ingresado fue: {mayor}")
else:
    print("No se ingresaron números.")

#2
suma = 0

for _ in range(10):
    numero = float(input("Ingrese un número: "))
    suma += numero

promedio = suma / 10
print(f"El promedio de los números es: {promedio}")

#3
ventas = {"Empleado 1": 0, "Empleado 2": 0, "Empleado 3": 0}

while True:
    monto = float(input("Ingrese el monto de la venta (0 para terminar): "))
    if monto == 0:
        break
    empleado = input("Ingrese el nombre del empleado (Empleado 1, Empleado 2 o Empleado 3): ")
    if empleado in ventas:
        ventas[empleado] += monto
    else:
        print("Empleado no válido.")

comisiones = {}
total_ventas = 0
total_comisiones = 0

for empleado, monto_total in ventas.items():
    comision = monto_total * 0.10
    comisiones[empleado] = comision
    total_ventas += monto_total
    total_comisiones += comision
    print(f"{empleado} - Vendido: ${monto_total} - 10% de comisión - A cobrar: ${comision}")

mejor_vendedor = max(ventas, key=ventas.get)

print(f"\nTotal recaudado: ${total_ventas}")
print(f"Total en comisiones pagadas: ${total_comisiones}")
print(f"Dinero que le quedó a Don Eusebio: ${total_ventas - total_comisiones}")
print(f"El mejor vendedor fue: {mejor_vendedor}")

#4
numero = int(input("Ingrese un número: "))
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("El número es primo.")
else:
    print("El número no es primo.")

#5
total_ingreso = 0
total_con_estudios = 0
hombres_con_estudios = 0
mujeres_con_estudios = 0
total_hombres = 0
total_mujeres = 0
edad_mas_joven = None

while True:
    nacimiento = input("Ingrese el año de nacimiento (o 'fin' para terminar): ")
    if nacimiento == "fin":
        break
    nacimiento = int(nacimiento)
    genero = input("Ingrese el género (M-F-N): ").upper()
    ingreso = float(input("Ingrese ingreso mensual: "))
    estudio = input("¿Posee estudios universitarios? (true/false): ").lower() == "true"

    if estudio:
        total_con_estudios += 1
        total_ingreso += ingreso
        if genero == "M":
            hombres_con_estudios += 1
        elif genero == "F":
            mujeres_con_estudios += 1
    
    if genero == "M":
        total_hombres += 1
    elif genero == "F":
        total_mujeres += 1

    edad = 2025 - nacimiento
    if ingreso > 800000:
        if (edad_mas_joven is None) or (edad < edad_mas_joven):
            edad_mas_joven = edad

if total_con_estudios > 0:
    print(f"Sueldo promedio con estudios universitarios: ${total_ingreso / total_con_estudios:.2f}")
else:
    print("No hay personas con estudios universitarios.")

if total_hombres > 0:
    print(f"Porcentaje de hombres con estudios universitarios: {(hombres_con_estudios / total_hombres) * 100:.2f}%")

if total_mujeres > 0:
    print(f"Porcentaje de mujeres con estudios universitarios: {(mujeres_con_estudios / total_mujeres) * 100:.2f}%")

if edad_mas_joven is not None:
    print(f"La persona más joven que gana más de $800000 tiene {edad_mas_joven} años.")
else:
    print("Nadie gana más de $800000.")

#6
while True:
    print("\nMenú:\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        print("¡Adiós!")
        break

    if opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 == 0:
            print("No se puede dividir por cero. Volviendo al menú...")
            continue
        print(f"Resultado: {num1 / num2}")
    else:
        numeros = []
        while True:
            num = input("Ingrese un número (o 'fin' para calcular): ")
            if num == "fin":
                break
            numeros.append(float(num))

        if not numeros:
            print("No se ingresaron números.")
            continue

        resultado = numeros[0]
        for n in numeros[1:]:
            if opcion == "1":
                resultado += n
            elif opcion == "2":
                resultado -= n
            elif opcion == "3":
                resultado *= n
        print(f"Resultado: {resultado}")

#7
mes = 1
mejor_mes = 0
mayor_facturacion = 0
total_general = 0
cantidad_meses = 0

while True:
    total_mes = 0
    print(f"\nIngrese ventas del mes {mes} (importe negativo para cambiar de mes):")

    while True:
        venta = float(input("Ingrese monto de venta: "))
        if venta < 0:
            break
        total_mes += venta

    if total_mes == 0:
        break

    print(f"Total facturado en el mes {mes}: ${total_mes}")
    if total_mes > mayor_facturacion:
        mayor_facturacion = total_mes
        mejor_mes = mes

    total_general += total_mes
    cantidad_meses += 1
    mes += 1

if cantidad_meses > 0:
    print(f"\nEl mes que más facturó fue el mes {mejor_mes} con ${mayor_facturacion}")
    print(f"Promedio de facturación mensual: ${total_general / cantidad_meses:.2f}")
else:
    print("No se ingresaron ventas.")

#8
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("\nMenú:\n1. Jugar\n2. Instrucciones\n3. Estadísticas\n4. Salir")
    opcion = input("Seleccione una opción: ")

    limpiar_pantalla()

    if opcion == "1":
        print("=== JUGAR ===")
    elif opcion == "2":
        print("=== INSTRUCCIONES ===")
    elif opcion == "3":
        print("=== ESTADÍSTICAS ===")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")

#9
while True:
    print("\nMenú:\n1. Múltiplos\n2. Dobles por 3\n3. Mitad por 6\n4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "4":
        print("Saliendo...")
        break

    numero = int(input("Ingrese el primer número: "))

    while True:
        siguiente = int(input("Ingrese siguiente número: "))

        if opcion == "1":
            if siguiente % numero != 0:
                print("No es múltiplo. Volviendo al menú...")
                break
        elif opcion == "2":
            if siguiente != numero * 2 * 3:
                print("No cumple ser doble por tres. Volviendo al menú...")
                break
        elif opcion == "3":
            if numero / 2 / 6 != siguiente:
                print("No cumple ser mitad por seis. Volviendo al menú...")
                break
        else:
            print("Opción inválida.")
            break
        numero = siguiente

#10
materias_mas_30 = 0
materia_max_alumnos = ""
max_alumnos = 0
total_profesores = 0

while True:
    codigo = input("Ingrese el código de la materia (o 'fin' para terminar): ")
    if codigo == "fin":
        break
    nombre = input("Ingrese el nombre de la materia: ")
    cuatrimestre = input("Ingrese el código del cuatrimestre: ")
    alumnos = int(input("Ingrese cantidad de alumnos: "))

    if alumnos > 30:
        materias_mas_30 += 1
    if alumnos > max_alumnos:
        max_alumnos = alumnos
        materia_max_alumnos = nombre

    total_profesores += (alumnos + 14) // 15  # Redondeo hacia arriba

print(f"\nCantidad de materias con más de 30 alumnos: {materias_mas_30}")
print(f"Materia con más alumnos: {materia_max_alumnos} ({max_alumnos} alumnos)")
print(f"Total de profesores a contratar: {total_profesores}")

