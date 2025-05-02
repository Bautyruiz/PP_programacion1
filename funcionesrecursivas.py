"""Guia de ejercicios
“Funciones recursivas”
1. Sumar todos los elementos de una lista: Crear una función recursiva que reciba una lista de
números y retorne la suma de todos sus elementos.
2. Contar la cantidad de dígitos de un número: Crear una función recursiva que reciba un número
entero positivo y devuelva cuántos dígitos tiene.
3. Invertir una cadena de texto: Crear una función recursiva que reciba una cadena y la devuelva
invertida, sin utilizar funciones o métodos especiales de Python como reverse o [::-1].
4. Calcular la potencia de un número: Crear una función recursiva que reciba dos números enteros
positivos, base y exponente, y calcule base elevado a exponente.
5. Verificar si una cadena es un palíndromo: Crear una función recursiva que reciba una cadena y
devuelva True si es palíndromo (se lee igual de adelante hacia atrás), o False si no lo es."""

#1
def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
print(f"La suma de la lista es: {suma_lista(numeros)}")

#2
def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

# Ejemplo de uso
numero = 12345
print(f"El número {numero} tiene {contar_digitos(numero)} dígitos.")

#3
def invertir_cadena(cadena):
    if cadena == "":
        return ""
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]

# Ejemplo de uso
texto = "Hola Mundo"
print(f"La cadena invertida es: '{invertir_cadena(texto)}'")

#4
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Ejemplo de uso
base = 2
exponente = 5
print(f"{base} elevado a {exponente} es: {potencia(base, exponente)}")

#5
def es_palindromo(cadena):
    if len(cadena) <= 1:
        return True
    if cadena[0] != cadena[-1]:
        return False
    return es_palindromo(cadena[1:-1])

# Ejemplo de uso
palabra = "reconocer"
print(f"¿La palabra '{palabra}' es un palíndromo? {es_palindromo(palabra)}")