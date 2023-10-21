"""Ejercicios de introducción a la estructura if"""

import ValidacionDeDatos

"""1. Calcular el valor total que una persona debe pagar por la compra de una llantas."""

# Pedimos ingresar al valor de cada llanta.
precioLlanta = ValidacionDeDatos.validarEnteros("Ingrese el precio de la llanta: ")

# Pedimos ingresar la cantidad de llantas compradas.
cantidadLlantas = ValidacionDeDatos.validarEnteros("Ingrese la cantidad de llantas: ")

if cantidadLlantas > 0:
    if cantidadLlantas <= 4:
        totalAPagar = precioLlanta * cantidadLlantas
    else:
        totalAPagar = (precioLlanta - (precioLlanta * .1)) * cantidadLlantas

    print("Total a pagar $", totalAPagar)
else:
    print("Error, ingrese un número positivo")


"""2. Validar si un número real está dentro de un intervalo"""

# Pedir que se ingrese el número.
numeroAValidar = ValidacionDeDatos.validarReales("\nIngrese un número real: ")

if 2.0 <= float(numeroAValidar) and  float(numeroAValidar) <= 5.0:
    print("Número pertenece al intervalo [2,5]")


"""3. Decisión para pagar una cuenta de restaurante"""

# Pedir que se ingrese el total de la cuenta.
totalCuenta = ValidacionDeDatos.validarEnteros("\nTotal cuenta: ")

if totalCuenta <= 500000:
    print("Pago en efectivo")
elif totalCuenta > 500000 and totalCuenta <= 1000000:
    print("Pago por transferencia")
elif totalCuenta > 1000000 and totalCuenta <= 2000000:
    print("Pago con tarjeta débito")
else:
    print("pago con tarjeta crédito")

# las decisiones consecutivas son una estructura condicional que se puede usar en los mismos casos de las decisiones
# anidadas.
# if totalCuenta <= 500000:
#   print...
# else:
#   if totalCuenta > 500000 and totalCuenta <= 1000000:
#       print...

"""4. Calcular el precio de la Pizza."""

# Pedir que se ingrese el tamaño de la Pizza.
print("\n1. Pizza pequeña $25000")
print("2. Pizza mediana $40000")
print("3. Pizza grande $60000")
tamañoPizza = ValidacionDeDatos.validarEnteros("\nSeleccione el tamaño de la pizza: ")

# Pedir el número de ingredientes adicionales.
ingredienteAdicional = ValidacionDeDatos.validarEnteros("Número de ingredientes adicionales: ")

if tamañoPizza == 1:
    costoTotal = 25000 + (ingredienteAdicional * 3500)
else:
    if tamañoPizza == 2:
        costoTotal = 40000 + (ingredienteAdicional * 3500)
    else:
        if tamañoPizza == 3:
            costoTotal = 60000 + (ingredienteAdicional * 3500)
        else:
            print("Seleccione uno de los tres tamaños")
            costoTotal = 0

print("El costo es: $",costoTotal)



