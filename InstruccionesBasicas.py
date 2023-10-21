"""Ejercicios con instrucciones de asignación básicas"""
import math

import ValidacionDeDatos
from ValidacionDeDatos import *             # para no tener que usar la notación punto al invocar un método.
from math import *

"""1. calcular el diametro de la base de un cilindro a partir de su volumen (pi * (radio ** 2) * h)"""

# Pedimos que se ingrese el volumen del cilindro.
volumenCilindro = validarEnteros("Ingrese el volumen del cilindro: ")

# Pedimos que se ingrese el valor de la altura.
alturaCilindro = validarEnteros("Ingrese la altura del cilindro: ")

# Diametro es igual a 2R.
"""Despejar el valor del radio:
Volumen = pi * radio**2 * h
Volumen / pi = radio** 2 * h
(Volumen / pi) / h = radio ** 2
sqrt((volumen / pi) / h) = radio"""

radioCilindro = sqrt((volumenCilindro / pi) / alturaCilindro)
print("El radio del cilindro es: ", format(radioCilindro, '.3f'))


"""2. Calcular la razón entre dos términos consecutivos de una progresión aritmética"""

# u = a + (n - 1)r. enesimo término.
# a, es el primer término.
# n, es la cantidad de términos.
# r, es la razón entre dos términos consecutivos.

# r = (u - a) / (n - 1).

# Pedimos al usuario que ingrese la cantidad de términos de la progresión.
cantidadTerminos = validarEnteros("\nIngrese la cantidad de términos de la progresión: ")

# Pedimos al usuario que ingrese el valor del primer término.
primerTermino = validarEnteros("Ingrese el valor del primer término de la progresión: ")

# Pedimos al usuario que ingrese el último término de la progresión.
terminoEnesimo = validarEnteros("Ingrese el último término de la progresión: ")

# Calculamos r.
razon = (terminoEnesimo - primerTermino) / (cantidadTerminos - 1)
print("la razón entre dos términos consecutivos de la progresión es: ", razon)


"""3. Calcular la calificación total"""

# Exámenes = 70%
# Lecciones = 20%.
# Tareas = 10%.

def cargarNotas(numeroNotas, mensaje):          # numeroNotas es el número de notas de cada item.

    notas = [ ]
    contador = 0
    while contador < numeroNotas:
        nota = ValidacionDeDatos.validarReales(mensaje)
        notas.append(nota)
        contador += 1

    contador1 = 0
    while contador1 < numeroNotas:
        print(notas[contador1], end=" ")   # el atributo end nos permite imprimir sobre la misma linea.
        contador1 += 1

    return notas

def calcularNota(notas, cantidadNotas):

    sumatoriaNotas = 0.0
    for i in range(0, len(notas), 1):
        sumatoriaNotas = sumatoriaNotas + float(notas[i])

    return sumatoriaNotas / float(cantidadNotas)


# Pedir que se ingrese el número de examenes.
numeroExamenes = validarEnteros("\nIngrese el número de examenes: ")

# Pedir que se ingrese el número de lecciones.
numeroLecciones = validarEnteros("\nIngrese el número de lecciones: ")

# Pedir que se ingrese el número de tareas.
numeroTareas = validarEnteros("\nIngrese el número de tareas: ")


# Crear listas para almacenar los datos de las diferentes notas.
notasExamenes = cargarNotas(numeroExamenes, "\nIngrese la nota del examen: ")
notasLecciones = cargarNotas(numeroLecciones, "\nIngrese la nota de la lección: " )
notasTareas = cargarNotas(numeroTareas, "\nIngrese la nota de la tarea: ")


# Calcular la nota definitiva de cada item.
finalExamenes = calcularNota(notasExamenes, numeroExamenes)
finalLecciones = calcularNota(notasLecciones, numeroLecciones)
finaltareas = calcularNota(notasTareas, numeroTareas)

print("\n")
print("\nDefinitiva exámenes: ", finalExamenes, "\nDefintiva lecciones: ", finalLecciones, "\nDefinitiva tareas: ", finaltareas)

definitiva = (finalExamenes + finalLecciones + finaltareas) / float(3)
print("\nNota definitiva materia: ", definitiva)






