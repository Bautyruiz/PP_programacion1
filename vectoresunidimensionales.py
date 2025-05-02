"""Guia de ejercicios
“Vectores unidimensionales”
1. Cargar y mostrar array:
Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un
ciclo for.
2. Sumar todos los elementos:
Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los
elementos.
3. Promedio de valores:
Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
de los valores.
4. Contar mayores a un valor:
Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.
5. Buscar un valor:
Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
Informar la posición en caso afirmativo, o indicar que no se encuentra.
6. Mayor y su posición:
Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
encuentra.
7. Invertir orden:
Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.
8. Comparar dos arrays:
Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
y mostrar un mensaje indicando si son o no iguales.
9. Intercambiar elementos pares por ceros:
Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
resultante.
10. Función para buscar la primera aparición de un valor:
Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
la posición de la primera aparición de ese número o -1 si no se encuentra"""

#1
array = []

for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    array.append(numero)

print("Contenido del array:")
for num in array:
    print(num)

#2
array = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    array.append(numero)

suma = sum(array)
print(f"La suma de todos los elementos es: {suma}")

#3
array = []

for i in range(6):
    numero = float(input(f"Ingrese el número real {i+1}: "))
    array.append(numero)

promedio = sum(array) / len(array)
print(f"El promedio de los valores es: {promedio:.2f}")

#4
array = []

for i in range(8):
    numero = int(input(f"Ingrese el número {i+1}: "))
    array.append(numero)

mayores_a_100 = sum(1 for num in array if num > 100)
print(f"Cantidad de números mayores a 100: {mayores_a_100}")

#5
array = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    array.append(numero)

buscar = int(input("Ingrese el número a buscar: "))

if buscar in array:
    posicion = array.index(buscar)
    print(f"El número {buscar} se encuentra en la posición {posicion}.")
else:
    print("El número no se encuentra en el array.")

#6
array = []

for i in range(7):
    numero = int(input(f"Ingrese el número {i+1}: "))
    array.append(numero)

mayor = max(array)
posicion = array.index(mayor)

print(f"El mayor valor es {mayor} y se encuentra en la posición {posicion}.")

#7
array = []

for i in range(6):
    numero = int(input(f"Ingrese el número {i+1}: "))
    array.append(numero)

print("Array invertido:")
for num in reversed(array):
    print(num)

#8
array1 = []
array2 = []

print("Cargar primer array:")
for i in range(5):
    array1.append(int(input(f"Ingrese el número {i+1}: ")))

print("Cargar segundo array:")
for i in range(5):
    array2.append(int(input(f"Ingrese el número {i+1}: ")))

if array1 == array2:
    print("Ambos arrays son iguales.")
else:
    print("Los arrays son diferentes.")

#9
array = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    array.append(numero)

for i in range(len(array)):
    if array[i] % 2 == 0:
        array[i] = 0

print("Array luego de reemplazar pares por ceros:")
print(array)

#10
def buscar_primera_aparicion(array, valor):
    for i in range(len(array)):
        if array[i] == valor:
            return i
    return -1

# Ejemplo de uso
array = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    array.append(numero)

valor = int(input("Ingrese el valor a buscar: "))

posicion = buscar_primera_aparicion(array, valor)

if posicion != -1:
    print(f"El valor {valor} se encontró en la posición {posicion}.")
else:
    print("El valor no se encuentra en el array.")