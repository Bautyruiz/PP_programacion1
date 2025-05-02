"""
🧪 Desafío: El Laboratorio del Doctor Código 🧪
🧬 Historia:
El Doctor Código, un científico algo olvidadizo, está construyendo un experimento con 3 ingredientes. Cada
uno debe tener una cantidad precisa para que el experimento no explote 💥.
Tu misión es ayudarlo a:
1. Pedir al usuario la cantidad de cada ingrediente.
2. Verificar si las cantidades están dentro del rango permitido.
3. Intentar 3 veces el experimento hasta que sea exitoso o explote.
4. Encapsular la lógica en funciones.
🎯 Objetivo del programa:
● Pedir al usuario que ingrese la cantidad (en mililitros) de Ingrediente A, B y C.
● Cada ingrediente tiene un rango válido:
○ A: entre 5 y 10 ml
○ B: entre 15 y 20 ml
○ C: entre 25 y 30 ml
● Si las 3 cantidades están dentro de los rangos: el experimento es exitoso 🎉
● Si alguna está mal: explota 💥 y puede reintentarse hasta 3 veces.
🧩 Requisitos técnicos:
● Usar funciones para:
○ Validar un ingrediente (validar_ingrediente)
○ Intentar el experimento (intentar_experimento)
● Usar condicionales (if) para validar rangos
● Usar un ciclo while o for para permitir 3 intentos
● Usar variables simples (no listas, no strings complejos)"""

print(" Bienvenidos al Laboratorio del Doctor Código ")
print("Debes ayudar al Doctor a mezclar los ingredientes correctos sin que explote ")

intentos = 0
experimento_exitoso = False

# Función para validar un ingrediente
def validar_ingrediente(nombre, cantidad):
    if nombre == "A":
        if cantidad >= 5:
            if cantidad <= 10:
                return True
        return False

    if nombre == "B":
        if cantidad >= 15:
            if cantidad <= 20:
                return True
        return False

    if nombre == "C":
        if cantidad >= 25:
            if cantidad <= 30:
                return True
        return False

    return False

# Función para intentar el experimento
def intentar_experimento():
    print("🔬 Ingresando cantidades para el experimento:")

    print("Cantidad de Ingrediente A (5-10 ml): ")
    a = input()
    print("Cantidad de Ingrediente B (15-20 ml): ")
    b = input()
    print("Cantidad de Ingrediente C (25-30 ml): ")
    c = input()

    if a.isdigit():
        a = int(a)
    else:
        print(" Entrada inválida para A. ¡Explosión!")
        return False

    if b.isdigit():
        b = int(b)
    else:
        print(" Entrada inválida para B. ¡Explosión!")
        return False

    if c.isdigit():
        c = int(c)
    else:
        print(" Entrada inválida para C. ¡Explosión!")
        return False

    # Validaciones encadenadas con return
    if validar_ingrediente("A", a):
        if validar_ingrediente("B", b):
            if validar_ingrediente("C", c):
                return True

    print(" Alguno de los ingredientes no está en el rango. ¡Explosión!")
    return False

# Ciclo de intentos
while intentos < 3:
    intentos = intentos + 1
    print("\n Intento", intentos, "de 3")

    if intentar_experimento():
        print(" ¡Experimento exitoso! ¡Buen trabajo, Doctor!")
        experimento_exitoso = True
        break
    else:
        print(" ¡El experimento explotó! Intenta nuevamente...")

# Resultado final
if experimento_exitoso:
    print("\n Fin del experimento. Todo bajo control ")
else:
    print("\n Has agotado tus intentos. El laboratorio quedó en ruinas ")