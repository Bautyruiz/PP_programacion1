"""Guia de ejercicios
“Condicionales”
1. Hacer un programa que pida el ingreso por teclado de dos números e imprima por pantalla al mayor
de ellos.
2. Modificar el punto 1 para que imprima por pantalla que número es el mayor y que número es
menor.
3. Pedir el ingreso de un número e imprimir por pantalla si es positivo, negativo o cero.
4. Solicitar el ingreso de tres números y mostrar por pantalla cuales de ellos son pares y cuales
impares
5. Pedir al usuario que ingrese su nombre, edad y altura. Luego imprimir por pantalla si es mayor de
edad y su etiqueta de altura.
Etiquetas de altura
Bajo: 0 - 1,20
Medio: 1,21 - 1,70
Alto: 1,71 - 2,00
Muy alto: 2,00 en adelante
6. Pedir el ingreso de tres números y mostrarlos en orden ascendente.
7. Pedir el ingreso de cuatro números y mostrar por pantalla al segundo mayor.
8. Pedir el ingreso de cuatro números e indicar cuantos de ellos son pares y cuantos impares. Si uno
de los números es negativo imprimir por pantalla un cartel aclaratorio que diga: “Alguno de los
números es negativo”
9. Hacer un programa que pida ingresar dos números, luego imprimir el resultado de la división.
Matemáticamente no se puede dividir por cero, por lo tanto si se ingresa como divisor un cero se
debe aclarar que esa cuenta no es posible realizarla y terminar el programa. De lo contrario,
imprimir el resultado.
10. Hacer un programa para ingresar tres modelos de auto y sus colores. Si dos son celeste y uno es
blanco imprimir un cartel aclaratorio que diga: “Con estos autos puedo simular la bandera
Argentina”. De lo contrario, si al menos uno es color amarillo imprimir un cartel que diga: “Al menos
tengo el color del sol”"""


# Ejercicio 1: Comparar dos números y mostrar el mayor

# Pedimos al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Comparamos los números
if numero1 > numero2:
    print("El número mayor es:", numero1)
elif numero2 > numero1:
    print("El número mayor es:", numero2)
else:
    print("Ambos números son iguales.")

#Este código:
#Pide al usuario que ingrese dos números.
#Compara cuál de los dos es mayor.
#Muestra por pantalla el número mayor, o indica si son iguales.


# Ejercicio 2: Mostrar el mayor y el menor de dos números

# Pedimos al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Comparamos los números y mostramos cuál es mayor y cuál es menor
if numero1 > numero2:
    print("El número mayor es:", numero1)
    print("El número menor es:", numero2)
elif numero2 > numero1:
    print("El número mayor es:", numero2)
    print("El número menor es:", numero1)
else:
    print("Ambos números son iguales.")


# Ejercicio 3: Determinar si un número es positivo, negativo o cero

# Pedimos al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Verificamos si es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Ejercicio 4: Verificar si tres números son pares o impares

# Pedimos al usuario que ingrese tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Verificamos y mostramos si cada número es par o impar
if num1 % 2 == 0:
    print(f"El número {num1} es par.")
else:
    print(f"El número {num1} es impar.")

if num2 % 2 == 0:
    print(f"El número {num2} es par.")
else:
    print(f"El número {num2} es impar.")

if num3 % 2 == 0:
    print(f"El número {num3} es par.")
else:
    print(f"El número {num3} es impar.")

# Ejercicio 5: Edad y etiqueta de altura

# Pedimos los datos al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en metros (por ejemplo: 1.65): "))

# Verificamos si es mayor de edad
if edad >= 18:
    print(f"{nombre} es mayor de edad.")
else:
    print(f"{nombre} es menor de edad.")

# Determinamos la etiqueta de altura
if altura <= 1.20:
    etiqueta = "Bajo"
elif altura <= 1.70:
    etiqueta = "Medio"
elif altura <= 2.00:
    etiqueta = "Alto"
else:
    etiqueta = "Muy alto"

print(f"Etiqueta de altura: {etiqueta}")

#Este script hace lo siguiente:
#Pide nombre, edad y altura.
#Dice si la persona es mayor o menor de edad.
#Clasifica su altura con las etiquetas dadas.

# Ejercicio 6: Mostrar tres números en orden ascendente

# Pedimos los tres números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Guardamos los números en una lista
numeros = [num1, num2, num3]

# Ordenamos la lista
numeros.sort()

# Mostramos los números en orden ascendente
print("Los números en orden ascendente son:", numeros)

# Este método es práctico porque list.sort() ya se encarga de ordenar los valores por nosotros.

# Ejercicio 7 (mejorado): Mostrar el segundo número mayor distinto entre cuatro

# Pedimos los cuatro números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
num4 = float(input("Ingrese el cuarto número: "))

# Guardamos los números en una lista
numeros = [num1, num2, num3, num4]

# Usamos un set para eliminar duplicados y luego ordenamos de mayor a menor
numeros_unicos = sorted(set(numeros), reverse=True)

# Verificamos si hay al menos dos valores distintos
if len(numeros_unicos) >= 2:
    print("El segundo número mayor (distinto) es:", numeros_unicos[1])
else:
    print("No hay un segundo número mayor distinto (todos los números son iguales).")
    #Usa set() para eliminar duplicados.

# Ejercicio 8: Contar pares e impares, y detectar si hay negativos

# Pedimos los cuatro números
numeros = []
for i in range(1, 5):
    numero = int(input(f"Ingrese el número {i}: "))
    numeros.append(numero)

# Contadores
pares = 0
impares = 0
hay_negativos = False

# Analizamos los números
for num in numeros:
    if num < 0:
        hay_negativos = True
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostramos resultados
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")

if hay_negativos:
    print("Alguno de los números es negativo.")

# Ejercicio 9: División con validación de división por cero

# Pedimos los dos números
dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))

# Verificamos si el divisor es cero
if divisor == 0:
    print("No se puede dividir por cero. Operación no válida.")
else:
    resultado = dividendo / divisor
    print("El resultado de la división es:", resultado)

# Ejercicio 10: Colores de autos y condiciones especiales

# Listas para guardar los colores
colores = []

# Ingresamos modelo y color de 3 autos
for i in range(1, 4):
    modelo = input(f"Ingrese el modelo del auto {i}: ")
    color = input(f"Ingrese el color del auto {i}: ").strip().lower()
    colores.append(color)

# Contamos cuántos celestes, blancos y amarillos hay
celestes = colores.count("celeste")
blancos = colores.count("blanco")
amarillos = colores.count("amarillo")

# Verificamos las condiciones
if celestes == 2 and blancos == 1:
    print("Con estos autos puedo simular la bandera Argentina.")
elif amarillos >= 1:
    print("Al menos tengo el color del sol.")


#Notas útiles:
#.strip().lower() permite ignorar mayúsculas/minúsculas y espacios extra.
#Se usa .count() para contar cada color.