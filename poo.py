"""Práctica de Programación Orientada a Objetos
1 -Clase para representar un Libro
Crear una clase Libro que tenga las características título, autor y año de publicación. Del
libro se debe poder obtener información, mostrando por mensaje todos sus datos. Se debe
crear la clase e implementarla.
2 - Clase para representar un Rectángulo Crear una clase rectángulo que tenga las
características base y altura. Del rectángulo se debe poder calcular el área y el perímetro.
Se debe crear la clase e implementarla.
3- Clase para representar una Calculadora Crear una clase Calculadora que pueda calcular
suma, resta, multiplicación y división. Se debe crear la clase e implementarla.
4- Herencia de clases
Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de
Animal las características y realice el sonido “guau guau”. La clase Gato que herede de
Animal las características y realice el sonido “Miau”. Del gato y el perro se debe poder
mostrar el sonido que realizan. Se debe crear la clase e implementarla.
5- Encapsulamiento Crear una clase Cuenta Bancaria que tenga las características titular y
saldo encapsulado. De la cuenta bancaria se puede obtener el saldo, depositar o retirar (en
cada caso imprimir que fue exitoso). Se debe crear la clase e implementarla.
CADENA DE CARACTERES-Métodos
Ejercicio 1: Desarrollar una función que Invierte el orden de los caracteres en una
cadena.
Ejercicio 2: Desarrollar una función que cuente cuántas palabras hay en una cadena.
Ejercicio 3: Desarrollar una función que reemplaza una palabra específica por otra
en una cadena.
Ejercicio 4: Desarrollar una función que convierta los elementos de lista_peli en una
cadena y muestre:
ej. "Se recomienda ver "Matrix", "El Padrino" y "Titanic" "" para cada elemento
lista_peli = [
["Matrix", "El Padrino", "Titanic"],
["Forrest Gump", "Pulp Fiction", "Gladiador"],
["Blade Runner", "El Rey León", "Volver al Futuro"],
["La La Land", "El Gran Lebowski", "Blade Runner"],
["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
["Harry Potter", "Forrest Gump", "Pulp Fiction"],
["Titanic", "Star Wars", "El Señor de los Anillos"],
["The Truman Show", "The Shape of Water", "The Big Lebowski"],
["Forrest Gump", "The Godfather", "Goodfellas"],
["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]
Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena.
Ejercicio 6: Desarrollar una función que verifique si una cadena es un palíndromo:
Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que resulta
la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo,
anilina.
Ejercicio 7: Desarrollar una función “ordenar” que recibe un string y un número (1 o
-1). Se debe retornar el string ordenado de manera ascendente (si recibió 1 por
parámetros) o descendente (si recibió -1)
Nota: Determinar parámetros y retornos de manera que las funciones sean
genéricas y reutilizables.
"""
#1
class Libro:
    def configurar(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"

# Ejemplo de uso
libro = Libro()
libro.configurar("Cien Años de Soledad", "Gabriel García Márquez", 1967)
print(libro.mostrar_informacion())

#2
class Rectangulo:
    def configurar(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Ejemplo de uso
rectangulo = Rectangulo()
rectangulo.configurar(4, 5)
print("Área:", rectangulo.calcular_area())
print("Perímetro:", rectangulo.calcular_perimetro())

#3
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "No se puede dividir por cero"
        return a / b

# Ejemplo de uso
calc = Calculadora()
print("Suma:", calc.sumar(5, 3))
print("Resta:", calc.restar(5, 3))
print("Multiplicación:", calc.multiplicar(5, 3))
print("División:", calc.dividir(5, 3))

#4
class Animal:
    def configurar(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def hacer_sonido(self):
        return "guau guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "miau"

# Ejemplo de uso
perro = Perro("Rex")
gato = Gato("Luna")
print(perro.nombre, "hace:", perro.hacer_sonido())
print(gato.nombre, "hace:", gato.hacer_sonido())

#5
class CuentaBancaria:
    def configurar(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print("Depósito exitoso. Saldo actual:", self.__saldo)

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Fondos insuficientes.")
        else:
            self.__saldo -= cantidad
            print("Retiro exitoso. Saldo actual:", self.__saldo)

# Ejemplo de uso
cuenta = CuentaBancaria("Juan", 1000)
print("Saldo inicial:", cuenta.obtener_saldo())
cuenta.depositar(500)
cuenta.retirar(300)

#Métodos de Cadenas de Caracteres
#Ejercicio 1: Invertir una cadena


def invertir_cadena(cadena):
    return cadena[::-1]

# Ejemplo de uso
print(invertir_cadena("Hola Mundo"))


#Ejercicio 2: Contar palabras en una cadena


def contar_palabras(cadena):
    return len(cadena.split())

# Ejemplo de uso
print(contar_palabras("Hola a todos en el mundo"))


#Ejercicio 3: Reemplazar una palabra en una cadena

def reemplazar_palabra(cadena, antigua, nueva):
    return cadena.replace(antigua, nueva)

# Ejemplo de uso
print(reemplazar_palabra("Hola mundo", "mundo", "a todos"))


#Ejercicio 4: Crear cadena de recomendación de películas

def recomendar_peliculas(lista_peli):
    return "Se recomienda ver " + ", ".join([f'"{peli}"' for sublista in lista_peli for peli in sublista])

# Ejemplo de uso
lista_peli = [["Matrix", "El Padrino", "Titanic"], ["Forrest Gump", "Pulp Fiction", "Gladiador"]]
print(recomendar_peliculas(lista_peli))


#Ejercicio 5: Capitalizar palabras en una cadena

def capitalizar_cadena(cadena):
    return cadena.title()

# Ejemplo de uso
print(capitalizar_cadena("hola mundo"))


#Ejercicio 6: Verificar si es un palíndromo

def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

# Ejemplo de uso
print(es_palindromo("anilina"))


#Ejercicio 7: Ordenar cadena de forma ascendente o descendente
def ordenar_cadena(cadena, orden):
    cadena_lista = list(cadena)
    n = len(cadena_lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if (orden == 1 and cadena_lista[j] > cadena_lista[j + 1]) or (orden == -1 and cadena_lista[j] < cadena_lista[j + 1]):
                cadena_lista[j], cadena_lista[j + 1] = cadena_lista[j + 1], cadena_lista[j]

    return "".join(cadena_lista)

# Ejemplo de uso
print(ordenar_cadena("edcba", 1))   # Ascendente
print(ordenar_cadena("edcba", -1))  # Descendente