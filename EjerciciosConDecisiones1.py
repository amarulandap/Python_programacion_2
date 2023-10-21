"""1. calcular el área o el volumen de un cilindro"""
# import ValidacionDeDatos
from ValidacionDeDatos import *
import math

# Pedimos al usuario que ingrese los valores del radio y de la altura.
radioCilindro = validarReales("Ingrese el radio del cilindro: ")
alturaCilindro = validarReales("Ingrese la altura del cilindro: ")

if alturaCilindro > radioCilindro:
    volumenCilindro = math.pi * math.pow(float(radioCilindro), 2) * float(alturaCilindro)

    print("El volumen del cilindro es: ",format(volumenCilindro, ".3f"))
elif radioCilindro > alturaCilindro:
    areaCilindro = (2 * float(math.pi)) * (float(radioCilindro) * float(alturaCilindro)) + (2 * math.pi * math.pow(float(radioCilindro), 2))

    print("El área del cilindro es: ",format(areaCilindro, ".3f"))
else:
    print("El radio y la altura son iguales")


"""2. Calcular las diagonales de un bloque rectangular y mostrar la mayor"""

# Pedir que se ingrese el valor de los lados.
lado1 = validarReales("\nIngrese el valor del primer lado: ")
lado2 = validarReales("Ingrese el valor del segundo lado: ")
lado3 = validarReales("Ingrese el valro del tercer lado: ")

# Calcular cada una de las diagonales o hipotenusas.
diagonal1 = math.sqrt(math.pow(float(lado1), 2) + math.pow(float(lado2), 2))
diagonal2 = math.sqrt(math.pow(float(lado1), 2) + math.pow(float(lado3), 2))
diagonal3 = math.sqrt(math.pow(float(lado2), 2) + math.pow(float(lado3), 2))

# Calcular cual es la diagonal mayor.
if diagonal1 > diagonal2:
    if diagonal1 > diagonal3:
        diagonalMayor = diagonal1
    else:
        diagonalMayor = diagonal3
elif diagonal2 > diagonal3:
    diagonalMayor = diagonal2
else:
    diagonalMayor = diagonal3

print(format(diagonal1, ".4f"), format(diagonal2, ".4f"), format(diagonal3, ".4f"))
print("La diagonal mayor es: ",format(diagonalMayor, ".4f"))


"""3. Leer un número y probar si es entero y multiplo de 7"""
#Para probar si es un número entero usamos la validación de datos.
numeroAValidar = validarEnteros("\nIngrese el número a validar: ")

if numeroAValidar % 7 == 0:
    print("El número",numeroAValidar, "es multiplo de 7")
else:
    print("El número ", numeroAValidar, "no es multiplo de 7")

