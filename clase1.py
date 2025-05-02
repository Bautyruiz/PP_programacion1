#La ferretería de Don Eusebio necesita un programa para calcular la comisión que debe pagar a cada uno de sus 3 empleados.

#El programa debe:
    #Pedir el nombre de cada empleado.
    #Solicitar el monto total en pesos que cada empleado vendió en el día.
    #Pedir el porcentaje de comisión que recibe cada empleado.
    #Calcular y mostrar la comisión que cobrará cada uno.
    
#Al finalizar, el programa debe mostrar:

   # El total de dinero recaudado en el día.
   # El total de comisiones pagadas.
#El dinero restante que le quedó a la ferretería.
    
#Tiempo despues, Don Eusebio ha decidido cubrir parte del almuerzo de cada día. Modificar lo necesario para que también se
#cumplan las siguientes consignas:

    #Se debe ingresar el monto total del almuerzo.
    #Cada empleado contribuirá con el 10% de su comisión.
    #El resto lo pagará Don Eusebio.
    #Mostrar cuánto debe abonar cada empleado y cuánto pagará Don Eusebio


def calcular_comisiones():
    empleados = []
    total_recaudado = 0
    total_comisiones = 0

    for i in range(3):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        ventas = float(input(f"Ingrese el monto total de ventas de {nombre}: "))
        porcentaje = float(input(f"Ingrese el porcentaje de comisión de {nombre} (sin %): "))
        
        comision = (ventas * porcentaje) / 100
        empleados.append({"nombre": nombre, "ventas": ventas, "comision": comision})
        
        total_recaudado += ventas
        total_comisiones += comision
    
    dinero_restante = total_recaudado - total_comisiones
    
    print("\nResumen del día:")
    for emp in empleados:
        print(f"{emp['nombre']} cobrará una comisión de: ${emp['comision']:.2f}")
    
    print(f"Total recaudado: ${total_recaudado:.2f}")
    print(f"Total de comisiones pagadas: ${total_comisiones:.2f}")
    print(f"Dinero restante en la ferretería: ${dinero_restante:.2f}")
    
    # Agregamos el cálculo del almuerzo
    monto_almuerzo = float(input("Ingrese el monto total del almuerzo: "))
    aporte_empleados = 0
    
    print("\nAportes para el almuerzo:")
    for emp in empleados:
        aporte = emp['comision'] * 0.10
        aporte_empleados += aporte
        print(f"{emp['nombre']} aportará: ${aporte:.2f}")
    
    aporte_don_eusebio = monto_almuerzo - aporte_empleados
    print(f"Don Eusebio pagará: ${aporte_don_eusebio:.2f}")

# Ejecutamos la función
calcular_comisiones()

"""hecho en clase
nombre_epleado_1 = input("Ingrese el nombre del empleado: ")
monto_total_1 = float(input("Ingrese monto vendido: "))
porcentaje_1 = float(input("Ingrese porcentaje de comision: "))

nombre_epleado_2 = input("Ingrese el nombre del empleado: ")
monto_total_2 = float(input("Ingrese monto vendido: "))
porcentaje_2 = float(input("Ingrese porcentaje de comision: "))

nombre_epleado_3 = input("Ingrese el nombre del empleado: ")
monto_total_3 = float(input("Ingrese monto vendido: "))
porcentaje_3 = float(input("Ingrese porcentaje de comision: "))

comision_1 = monto_total_1 * porcentaje_1 / 100
comision_2 = monto_total_2 * porcentaje_2 / 100
comision_3 = monto_total_3 * porcentaje_3 / 100

print(f"{nombre_epleado_1} vendió {monto_total_1} y obtuvo de comision {comision_1}")
print(f"{nombre_epleado_2} vendió {monto_total_2} y obtuvo de comision {comision_2}")
print(f"{nombre_epleado_3} vendió {monto_total_3} y obtuvo de comision {comision_3}")

recaudacion_diaria = monto_total_2 + monto_total_1 + monto_total_3
comisiones_totales = comision_1 + comision_2 + comision_3
total_del_dia = recaudacion_diaria - comisiones_totales

print(f"Recaudacion diaria: {recaudacion_diaria}")
print(f"Comisiones pagadas: {comisiones_totales}")
print(f"Saldo disponible: {total_del_dia}")

pago_1 = comision_1 * 0.1
pago_2 = comision_2 * 0.1
pago_3 = comision_3 * 0.1

total_almuerzo = float(input("Ingrese total de almuerzo"))

pago_Don_Eusebio = total_almuerzo - pago_1 - pago_2 - pago_3

print(f"Total Almuerzo: {total_almuerzo}")
print(f"{nombre_epleado_1}: {pago_1}")
print(f"{nombre_epleado_2}: {pago_2}")
print(f"{nombre_epleado_3}: {pago_3}")
print(f"Don Eusebio: {pago_Don_Eusebio}")"""

#modificar el programa de la ferretería para que al final del programa
#se sumen el total del almuerzo y los gastos de comisión y emita por pantalla si hubo ganancia o perdida

"""def calcular_comisiones():
    empleados = []
    total_recaudado = 0
    total_comisiones = 0

    for i in range(3):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        ventas = float(input(f"Ingrese el monto total de ventas de {nombre}: "))
        porcentaje = float(input(f"Ingrese el porcentaje de comisión de {nombre} (sin %): "))
        
        comision = (ventas * porcentaje) / 100
        empleados.append({"nombre": nombre, "ventas": ventas, "comision": comision})
        
        total_recaudado += ventas
        total_comisiones += comision
    
    dinero_restante = total_recaudado - total_comisiones
    
    print("\nResumen del día:")
    for emp in empleados:
        print(f"{emp['nombre']} cobrará una comisión de: ${emp['comision']:.2f}")
    
    print(f"Total recaudado: ${total_recaudado:.2f}")
    print(f"Total de comisiones pagadas: ${total_comisiones:.2f}")
    print(f"Dinero restante en la ferretería: ${dinero_restante:.2f}")
    
    # Agregamos el cálculo del almuerzo
    monto_almuerzo = float(input("Ingrese el monto total del almuerzo: "))
    aporte_empleados = 0
    
    print("\nAportes para el almuerzo:")
    for emp in empleados:
        aporte = emp['comision'] * 0.10
        aporte_empleados += aporte
        print(f"{emp['nombre']} aportará: ${aporte:.2f}")
    
    aporte_don_eusebio = monto_almuerzo - aporte_empleados
    print(f"Don Eusebio pagará: ${aporte_don_eusebio:.2f}")
    
    # Calcular resultado final (ganancia o pérdida)
    total_gastos = total_comisiones + monto_almuerzo
    resultado_final = total_recaudado - total_gastos
    
    print("\nBalance del día:")
    print(f"Total de gastos (comisiones + almuerzo): ${total_gastos:.2f}")
    if resultado_final >= 0:
        print(f"Ganancia del día: ${resultado_final:.2f}")
    else:
        print(f"Pérdida del día: ${abs(resultado_final):.2f}")

# Ejecutamos la función
calcular_comisiones()"""