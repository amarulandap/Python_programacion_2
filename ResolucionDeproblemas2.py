"""1. Calcular las ganancias mensuales de una compañia"""
import sys
from math import *

# Ingresar la cantidad de articulos.
try:
    cantidadArticulos = int(input("Ingrese la cantidad de articulos fabricados: "))
except ValueError as e:
    print("Error, ingrese un número entero", file=sys.stderr)
    sys.exit()

# calcular el costo mensual.
costoMensual = 50 + 2 * cantidadArticulos
print("El costo mensual es: $", costoMensual , "pesos")

# Calcular el ingreso por la venta de los articulos
ingresoVenta = 2.4 * cantidadArticulos
print("El ingreso ventas es: $", ingresoVenta , "pesos")

# Calcular la ganancia.
ganancia = ingresoVenta - costoMensual
print("la ganancia es: $", ganancia , "pesos")

# Ganancia = 0 --> ingresos = gastos.
# 50 + 2x = 2.4x
# 50 = 0.4x
# 125 = x



""""2. Calcular la cantidad de dinero acumulada en una cuenta de ahorros."""

def validarDatos (mensaje):

    try:
        dato = float(input(mensaje))
    except ValueError as e:
        print("Error, ingrese un número", file=sys.stderr)
        sys.exit()

    return dato

# Ingresar el valor de cada deposito mensual.
valorDeposito = validarDatos("\nIngrese el valor a depositar: ")

# Ingresar el valor nominal del intéres mensual.
interesMensual = validarDatos("Ingrese el valor del interes mensual: ")

# Ingresar el número de depósitos mensuales realizados.
numeroDepositos = validarDatos("Ingrese el número de depositos: ")

# Calcular lo acumulado
valorAcumulado = valorDeposito * ((pow((1 + interesMensual), numeroDepositos) - 1) / interesMensual)
print("El valor acumulado después de", numeroDepositos, "depósitos realizados es $", valorAcumulado)

"""20000 / ((pow((1 + interesMensual), numeroDepositos) - 1) / interesMensual) = valorDeposito"""

