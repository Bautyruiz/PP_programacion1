"""Actividad: "La máquina clasificadora de números"
Una empresa quiere automatizar una máquina que clasifica números ingresados por teclado. La máquina
permite cargar una cierta cantidad de números enteros positivos y luego procesa cada uno según las
siguientes reglas:
● Si el número es par y múltiplo de 3, se clasifica como "Tipo A".
● Si el número es impar y mayor que 50, se clasifica como "Tipo B".
● Si el número es igual a 0, se ignora y no se clasifica.
● Todos los demás números se clasifican como "Tipo C".
El programa debe:
1. Pedir al usuario cuántos números quiere ingresar (mínimo 1, validarlo).
2. Ingresar los números uno por uno.
3. Clasificar cada número según las reglas.
4. Mostrar al final cuántos números se clasificaron de cada tipo ("Tipo A", "Tipo B", "Tipo C").
5. Mostrar el porcentaje que representa cada tipo respecto del total clasificado (excluyendo ceros).
Restricciones:
● Usar funciones para organizar el código: por ejemplo una función que reciba un número y devuelva
el tipo.
● No usar listas ni estructuras avanzadas. Solo variables simples, condicionales, ciclos y funciones.
● Se debe validar que los números ingresados sean enteros mayores o iguales a 0."""




def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("¿Cuántos números desea ingresar? (mínimo 1): "))
            if cantidad >= 1:
                return cantidad
            else:
                print("Debe ingresar al menos un número.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo (>= 0): "))
            if numero >= 0:
                return numero
            else:
                print("El número debe ser mayor o igual a 0.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

def clasificar_numero(n):
    if n == 0:
        return "IGNORAR"
    elif n % 2 == 0 and n % 3 == 0:
        return "Tipo A"
    elif n % 2 == 1 and n > 50:
        return "Tipo B"
    else:
        return "Tipo C"

def calcular_porcentaje(cantidad, total):
    if total == 0:
        return 0
    return (cantidad / total) * 100

# Programa principal
def main():
    total_a = 0
    total_b = 0
    total_c = 0
    total_validos = 0

    cantidad = pedir_cantidad()

    for _ in range(cantidad):
        numero = pedir_numero()
        tipo = clasificar_numero(numero)

        if tipo == "Tipo A":
            total_a += 1
            total_validos += 1
        elif tipo == "Tipo B":
            total_b += 1
            total_validos += 1
        elif tipo == "Tipo C":
            total_c += 1
            total_validos += 1
        else:
            print("Número 0 ignorado.")

    # Mostrar resultados
    print("\nClasificación final:")
    print("Cantidad Tipo A:", total_a)
    print("Cantidad Tipo B:", total_b)
    print("Cantidad Tipo C:", total_c)

    print("\nPorcentajes sobre el total clasificado (sin contar ceros):")
    print(f"Tipo A: {calcular_porcentaje(total_a, total_validos):.2f}%")
    print(f"Tipo B: {calcular_porcentaje(total_b, total_validos):.2f}%")
    print(f"Tipo C: {calcular_porcentaje(total_c, total_validos):.2f}%")

# Ejecutar el programa
main()


"""¿Qué hace este programa?
Pide al usuario la cantidad de números a ingresar (mínimo 1).
Valida cada número para asegurarse que sea entero positivo (incluyendo 0).
Clasifica los números según las reglas dadas.
Cuenta cuántos números hay de cada tipo, ignorando los ceros.
Muestra el conteo y el porcentaje de cada tipo respecto al total clasificado."""