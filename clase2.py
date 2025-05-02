""""🧠 La Torre del Conocimiento
🏰 Historia:
Eres un valiente aventurero que ha llegado a la legendaria Torre del Conocimiento, un lugar donde solo los
sabios logran llegar a la cima.
Para subir cada uno de sus 4 pisos, deberás demostrar tu inteligencia y lógica respondiendo preguntas de
Verdadero (V) o Falso (F).
¡Cada respuesta correcta te lleva un piso más alto! Pero si te equivocas... deberás intentarlo de nuevo hasta
acertar.
¿Podrás alcanzar la cima y obtener el conocimiento supremo?
🎯 Objetivo:
● El jugador debe responder correctamente 4 preguntas de V o F.
● Si la respuesta es correcta ✅, sube al siguiente piso.
● Si la respuesta es incorrecta ❌, debe volver a intentarlo en ese mismo piso.
🔧 Instrucciones:
● Utilizá un bucle for para representar los 4 pisos.
● Dentro del for, agregá un bucle while que repita la pregunta hasta que la respuesta sea correcta.
● Validá que solo se puedan ingresar "V" o "F" (ignorá mayúsculas o minúsculas, pero no aceptes otro
valor).
● No se deben utilizar listas ni estructuras avanzadas.
🪜 Reglas del juego:
1. Se empieza en el piso 1.
2. Cada piso tiene una única pregunta.
3. Solo se avanza si se responde correctamente.
4. El programa termina cuando el jugador llega al piso 5 (es decir, después de responder las 4
preguntas).
💡 Pistas para el desafío:
● Pensá qué ciclo te sirve para repetir hasta que algo salga bien.
● Prestá atención a la validación de la entrada: solo se aceptan "V" o "F".
● Usá una variable para llevar cuenta del piso actual.
● Antes de avanzar de piso, asegurate de que la respuesta sea válida y correcta """

import datetime

def calcular_edad(anio_nacimiento):
    anio_actual = datetime.datetime.now().year
    return anio_actual - anio_nacimiento

def torre_del_conocimiento():
    print("¡Bienvenido a la Torre del Conocimiento!\n")
    
    preguntas = [
        ("El sol es una estrella. (V/F): ", "V"),
        ("La Tierra tiene dos lunas. (V/F): ", "F"),
        ("El agua hierve a 100°C a nivel del mar. (V/F): ", "V"),
        ("Los seres humanos tienen tres pulmones. (V/F): ", "F")
    ]
    
    for piso in range(4):
        while True:
            respuesta = input(f"Piso {piso + 1}: {preguntas[piso][0]}")
            
            if respuesta not in ["V", "F"]:
                print("⚠️ Respuesta inválida. Solo se acepta 'V' o 'F'. Intentá de nuevo.")
                continue
            
            if respuesta == preguntas[piso][1]:
                print("✅ Respuesta correcta! Subes al siguiente piso.\n")
                break
            else:
                print("❌ Respuesta incorrecta. Intenta de nuevo.\n")
    
    print("¡Felicitaciones! Has alcanzado la cima y obtenido el conocimiento supremo. 🏆")

"""Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el 
programa debe pedir el año de nacimiento del usuario y mostrar la edad calculada."""

# Pedir año de nacimiento y calcular edad
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = calcular_edad(anio_nacimiento)
print(f"Tienes {edad} años.")

torre_del_conocimiento()

"""     **hecho en clase**
print("Bienvenidos a La torre del conocimiento")

print("para llegar a la cima, debes responder 4 preguntas correctamente")
respuestas_correctas = 0
piso_actual = 1

for piso in range(4):
    
    if piso_actual == 1:
        respuesta_correcta = "f"
        pregunta = "El mes de febrero siempre tiene la misma cantidad de dias"

    elif piso_actual == 2:
        respuesta_correcta = "f"
        pregunta = "Estamos en una clase de ingles"
    elif piso_actual == 3:
        respuesta_correcta ="f"
        pregunta = "Messi es un poeta argentino"
    else:
        respuesta_correcta = "v"
        pregunta = "Hoy es viernes"
            
    print(pregunta)

    while True:
        respuesta = input("Ingrese respuesta: ")

        if respuesta == "v" or respuesta == "f":
            if respuesta == respuesta_correcta:
                print("Respuesta correcta")
                piso_actual += 1
                respuestas_correctas += 1
                break
            else:
                print("Respuesta incorrecta")
        else:
            print("Letra ingresada es incorrecta")

print("Felicitaciones, llegaste al piso 5\nJuego Terminado")"""

