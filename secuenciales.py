"""Guia de ejercicios
“Secuenciales”
1. Pedir por teclado el nombre del usuario e imprimir por pantalla un saludo mencionando su nombre.
Por ejemplo “Hola, Roque!”
2. Pedir por teclado el nombre, apellido, la edad y la altura del usuario, luego imprimir por pantalla los
datos ingresados acomodados en una oración.
3. Pedir por teclado el año de nacimiento de una persona e imprimir por pantalla la edad actual (No
contemplar el mes de cumpleaños, por ejemplo, si se ingresa el año 1990, imprimir por pantalla la
edad 25)
4. Hacer un programa que pida por teclado dos números y luego mostrar el resultado de la suma, la
resta y la multiplicación entre ambos.
5. Pedir a un usuario que ingrese tres frases, luego mostrar por pantalla las tres frases juntas en el
siguiente orden: frase 2, frase 3, frase 1.
Ejemplo:
Frase 1: “Los árboles son altos”
Frase 2: “Las casas están lejos”
Frase 3: “La música se escucha fuerte”
Frases juntas: “Las casas están lejos La música se escucha fuerte Los árboles son
altos”
6. Pedir por teclado la base y la altura de un triángulo, luego mostrar por pantalla el área.
7. Nicanor fue a una tienda de electrodomésticos a comprar una heladera nueva. Escribe un
programa en Python que realice lo siguiente:
● Solicite por pantalla el importe bruto de la heladera (un número decimal).
● Calcule el IVA (21%) y determine el importe total a pagar.
● Muestre en pantalla el importe total de la compra.
● Como Nicanor paga en efectivo, debe contar el dinero utilizando la menor cantidad posible
de billetes. Para ello, el programa debe calcular cuántos billetes de cada denominación
se necesitan para abonar el importe exacto.
● Tener en cuenta billetes de $20000 a $10 y monedas de $5 a $0.10.
8. Pedir por pantalla una cantidad de minutos y mostrar por pantalla cuantas horas son y cuantos
minutos sobran.
9. La ferretería de Don Eusebio necesita un programa para calcular cual es la comisión que debe
pagar a cada uno de sus 3 empleados. El programa debe pedir el nombre del empleado, la
cantidad en pesos que este vendió en el día, el porcentaje de comisión que le paga y la comisión
que cobrará.
Ejemplo de como se debería mostrar por pantalla:
Empleado 1: Rómulo - Vendido: $50000 - 10% de comisión - A cobrar: $5000.
Empleado 2: Domingo - Vendido: $60000 - 10% de comisión - A cobrar: $6000.
Empleado 3: Rómulo - Vendido: $70000 - 10% de comisión - A cobrar: $7000.
Por último, Don Eusebio necesita saber todo lo recaudado en el día, el total en comisiones que
pagó y el dinero que le quedó.
10. Don Eusebio acordó con sus empleados pagar parte del almuerzo de cada día, para esto, modificar
el programa del punto 9 para que se pueda ingresar el monto total del almuerzo. Cada empleado
pondrá el 10% de la comisión obtenida y el resto va por cuenta de Don Eusebio. Mostrar por
pantalla al final que monto debe abonar cada uno."""

#1
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")

#2
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
altura = input("Ingrese su altura en metros: ")
print(f"Hola, {nombre} {apellido}. Tenés {edad} años y tu altura es {altura} metros.")

#3
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2025 - año_nacimiento
print(f"Su edad es {edad} años.")

#4
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")

#5
frase1 = input("Ingrese la primera frase: ")
frase2 = input("Ingrese la segunda frase: ")
frase3 = input("Ingrese la tercera frase: ")

print(f"{frase2} {frase3} {frase1}")

#6
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = (base * altura) / 2
print(f"El área del triángulo es {area}")

#7
importe_bruto = float(input("Ingrese el importe bruto de la heladera: "))
iva = importe_bruto * 0.21
importe_total = importe_bruto + iva
print(f"Importe total a pagar: ${importe_total:.2f}")

billetes = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10]
monedas = [5, 2, 1, 0.5, 0.25, 0.1]

resto = importe_total

print("\nCantidad de billetes/monedas necesarias:")
for billete in billetes:
    cantidad = int(resto // billete)
    if cantidad > 0:
        print(f"${billete}: {cantidad}")
        resto -= cantidad * billete

for moneda in monedas:
    cantidad = int(resto // moneda)
    if cantidad > 0:
        print(f"${moneda:.2f}: {cantidad}")
        resto -= cantidad * moneda

resto = round(resto, 2)
if resto > 0:
    print(f"Falta abonar ${resto:.2f} debido al redondeo.")

#8
minutos = int(input("Ingrese la cantidad de minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60

print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")

#9
recaudado = 0
total_comisiones = 0

for i in range(1, 4):
    nombre = input(f"Ingrese el nombre del empleado {i}: ")
    vendido = float(input(f"Ingrese el monto vendido por {nombre}: "))
    porcentaje = float(input(f"Ingrese el porcentaje de comisión para {nombre}: "))

    comision = vendido * (porcentaje / 100)

    print(f"Empleado {i}: {nombre} - Vendido: ${vendido} - {porcentaje}% de comisión - A cobrar: ${comision}")

    recaudado += vendido
    total_comisiones += comision

dinero_quedo = recaudado - total_comisiones

print(f"\nTotal recaudado: ${recaudado}")
print(f"Total en comisiones pagadas: ${total_comisiones}")
print(f"Dinero que le quedó a Don Eusebio: ${dinero_quedo}")

#10
recaudado = 0
total_comisiones = 0
aportes = []

almuerzo = float(input("Ingrese el monto total del almuerzo: "))

for i in range(1, 4):
    nombre = input(f"Ingrese el nombre del empleado {i}: ")
    vendido = float(input(f"Ingrese el monto vendido por {nombre}: "))
    porcentaje = float(input(f"Ingrese el porcentaje de comisión para {nombre}: "))

    comision = vendido * (porcentaje / 100)
    aporte_almuerzo = comision * 0.10
    aportes.append(aporte_almuerzo)

    print(f"Empleado {i}: {nombre} - Vendido: ${vendido} - {porcentaje}% de comisión - A cobrar: ${comision} - Aporta al almuerzo: ${aporte_almuerzo:.2f}")

    recaudado += vendido
    total_comisiones += comision

dinero_quedo = recaudado - total_comisiones
aporte_total_empleados = sum(aportes)
don_eusebio_paga = almuerzo - aporte_total_empleados

print(f"\nTotal recaudado: ${recaudado}")
print(f"Total en comisiones pagadas: ${total_comisiones}")
print(f"Dinero que le quedó a Don Eusebio: ${dinero_quedo}")
print(f"Aporte total de empleados para el almuerzo: ${aporte_total_empleados:.2f}")
print(f"Don Eusebio debe pagar del almuerzo: ${don_eusebio_paga:.2f}")