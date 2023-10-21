"""1. calcular el área total de un bloque de dimensiones a, b, c cm"""

import sys                      # Importamos el bloque de funciones necesarias para la validación de datos.
from math import *

ladosBloque = [ ]

cantidadLados = 0

while cantidadLados < 3:

    # Validamos que se esten ingresando datos numericos.
    try:
        valorLado = float(input("Ingrese el valor del lado: "))
    except ValueError as e:
        print("Error, ingrese un número", file=sys.stderr)
        sys.exit()

    # Agregar los valores a la lista.
    ladosBloque.append(valorLado)

    cantidadLados += 1

# Calculamos al área del bloque (Solo se pueden concatenar Strings).

areaBloque = 2 * ((ladosBloque[0] * ladosBloque[1]) + (ladosBloque[0] * ladosBloque[2]) + (ladosBloque[1] * ladosBloque[2]) )
print("El area del bloque es:", areaBloque)


"""2. Calcular el área total de un cilindro de radio a y altura b"""

# Crear una función para validar que se ingresen datos enteros.
def validardatos (mensaje):

    try:
        valor = int(input(mensaje))
    except ValueError as e:
        print("Error, ingrese un número entero.", file=sys.stderr)
        sys.exit()

    return valor

# Ingrese el valor del radio.
valorRadio = validardatos("\nIngrese el valor del radio: ")

# Ingrese el valor de la altura.
valorAltura = validardatos("Ingrese el valor de la altura: ")

# Calcular el área de la base.
areaBase = pi * pow(valorRadio, 2)
print("Área de la base: ", areaBase)

#Calcular el área del lado.
areaLado = 2 * pi * valorRadio * valorAltura
print("Área del lado: ", areaLado)

# Calcular el área total.
areaTotal = (2 * areaBase) + areaLado
print("Área total: ", areaTotal)




