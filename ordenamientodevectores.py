"""Guia de ejercicios
“Ordenamiento de vectores”
1. Dado un vector de 5 números desordenados, ordenarlo de menor a mayor utilizando el método de
intercambio simple (bubble sort).
2. Dado un vector de 7 números enteros, ordenarlo de mayor a menor utilizando selección directa.
3. Crear un programa que cargue un vector de N elementos (a definir por el usuario) y luego lo ordene
de menor a mayor usando inserción directa (Insertion Sort)
4. Implementar un programa que ordene dos vectores por separado de menor a mayor y luego
fusione ambos vectores ordenados en uno solo (sin usar métodos de listas, simulando arrays
estáticos).
5. Ordenar un vector de 10 letras (caracteres) alfabéticamente utilizando el algoritmo de selección
directa.
6. Dado un vector de números positivos, ordenarlo utilizando el método de mergesort.
7. Dado un vector de números, separar en dos vectores: uno con los pares y otro con los impares, y
luego ordenar ambos vectores de menor a mayor.
8. Implementar el método de quicksort para ordenar un vector de números cargados manualmente."""

#1
vector = []

for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    vector.append(num)

# Bubble Sort
for i in range(len(vector)-1):
    for j in range(len(vector)-i-1):
        if vector[j] > vector[j+1]:
            vector[j], vector[j+1] = vector[j+1], vector[j]

print(f"\nVector ordenado de menor a mayor: {vector}")

#2
vector = []

for i in range(7):
    num = int(input(f"Ingrese el número {i+1}: "))
    vector.append(num)

# Selección directa
for i in range(len(vector)):
    max_idx = i
    for j in range(i+1, len(vector)):
        if vector[j] > vector[max_idx]:
            max_idx = j
    vector[i], vector[max_idx] = vector[max_idx], vector[i]

print(f"\nVector ordenado de mayor a menor: {vector}")

#3
n = int(input("Ingrese la cantidad de elementos: "))
vector = []

for i in range(n):
    num = int(input(f"Ingrese el número {i+1}: "))
    vector.append(num)

# Inserción directa
for i in range(1, len(vector)):
    clave = vector[i]
    j = i-1
    while j >= 0 and vector[j] > clave:
        vector[j+1] = vector[j]
        j -= 1
    vector[j+1] = clave

print(f"\nVector ordenado de menor a mayor: {vector}")

#4
# Cargar primer vector
vector1 = []
print("Primer vector:")
for i in range(3):
    vector1.append(int(input(f"Elemento {i+1}: ")))

# Cargar segundo vector
vector2 = []
print("Segundo vector:")
for i in range(3):
    vector2.append(int(input(f"Elemento {i+1}: ")))

# Ordenar ambos (bubble simple)
for v in [vector1, vector2]:
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]

# Fusionar
fusionado = []
i = j = 0

while i < len(vector1) and j < len(vector2):
    if vector1[i] < vector2[j]:
        fusionado.append(vector1[i])
        i += 1
    else:
        fusionado.append(vector2[j])
        j += 1

# Agregar sobrantes
while i < len(vector1):
    fusionado.append(vector1[i])
    i += 1
while j < len(vector2):
    fusionado.append(vector2[j])
    j += 1

print(f"\nVector fusionado y ordenado: {fusionado}")

#5
vector = []

for i in range(10):
    letra = input(f"Ingrese la letra {i+1}: ").upper()
    vector.append(letra)

# Selección directa
for i in range(len(vector)):
    min_idx = i
    for j in range(i+1, len(vector)):
        if vector[j] < vector[min_idx]:
            min_idx = j
    vector[i], vector[min_idx] = vector[min_idx], vector[i]

print(f"\nLetras ordenadas alfabéticamente: {vector}")

#6
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Cargar el vector
vector = []
n = int(input("Ingrese la cantidad de números positivos: "))
for i in range(n):
    vector.append(int(input(f"Número {i+1}: ")))

merge_sort(vector)
print(f"\nVector ordenado (mergesort): {vector}")

#7
vector = []
n = int(input("Cantidad de números: "))
for i in range(n):
    vector.append(int(input(f"Número {i+1}: ")))

pares = [num for num in vector if num % 2 == 0]
impares = [num for num in vector if num % 2 != 0]

pares.sort()
impares.sort()

print(f"\nPares ordenados: {pares}")
print(f"Impares ordenados: {impares}")

#8
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x < pivote]
        mayores = [x for x in arr[1:] if x >= pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Cargar el vector
vector = []
n = int(input("Ingrese la cantidad de números: "))
for i in range(n):
    vector.append(int(input(f"Número {i+1}: ")))

vector = quicksort(vector)
print(f"\nVector ordenado (quicksort): {vector}")
