"""Calcular el área del trangulo usando la formula de Herón"""

import sys
from math import *

#Conocer la longitud de los lados.
lados = [ ]

for i in range(0, 3, 1):
    try:
        lado = float(input("Ingrese el valor del lado: "))
    except ValueError as e:
        print("Error, ingrese un número", file = sys.stderr)
        sys.exit()
        #break
    lados.append(lado)

#Calculamos el semiperimetro t = (a + b + c) / 2.
semiPerimetro = (lados[0] + lados[1] + lados[2]) / 2
print('Semiperimetro =', semiPerimetro)

#Calculamos el área = raizCuadrada(semiPerimetro(s - a)(s - b)(s -c).
area = sqrt(semiPerimetro * (semiPerimetro - lados[0]) * (semiPerimetro - lados[1]) * (semiPerimetro - lados[2]))
print('Área =', area)


