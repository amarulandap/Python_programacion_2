"""Funciones para validar el ingreso correcto de los datos"""
import sys

# Validar datos tipo entero.
def validarEnteros(mensaje):

    try:
        numeroEntero = int(input(mensaje))
    except ValueError as e:
        print("Error, ingrese un dato entero", file=sys.stderr)
        sys.exit()

    return numeroEntero


# Validar datos tipo real.
def validarReales(mensaje):

    try:
        numeroReal = float(input(mensaje))
    except ValueError as e:
        print("Error, ingrese un número real", file=sys.stderr)
        sys.exit()

    return format(numeroReal, ".4f")      # Damos formato al número real usando solo 4 decimales.



