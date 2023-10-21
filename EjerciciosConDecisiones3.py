"""1. Encontrar la calificación mayor y menor de un estudiante"""

import ValidacionDeDatos
import math

# Pedimos al usuario que ingrese cada una de las notas y las almacenamos en una lista.

calificaciones = [ ]
for i in range(0, 3, 1):
    calificacionAlumno = ValidacionDeDatos.validarReales("Calificación: ")
    calificaciones.append(calificacionAlumno)

# Comparar cada una de las posiciones de la lista.

if calificaciones[0] > calificaciones[1]:

    if calificaciones[0] > calificaciones[2] and calificaciones[2] > calificaciones[1]:
        calificacionMayor = calificaciones[0]
        calificacionMenor = calificaciones[1]

    elif calificaciones[0] > calificaciones[2] and calificaciones[2] < calificaciones[1]:
        calificacionMayor = calificaciones[0]
        calificacionMenor = calificaciones[2]

elif calificaciones[1] > calificaciones[2] and calificaciones[0] > calificaciones[2]:
    calificacionMayor = calificaciones[1]
    calificacionMenor = calificaciones[2]

elif calificaciones[1] > calificaciones[2] and calificaciones[2] > calificaciones[0]:
    calificacionMayor = calificaciones[1]
    calificacionMenor = calificaciones[0]

else:
    calificacionMayor = calificaciones[2]

    if calificaciones[1] > calificaciones[0]:
        calificacionMenor = calificaciones[0]
    else:
        calificacionMenor = calificaciones[1]

print("Calificación mayor: ", calificacionMayor, "Calificación menor: ", calificacionMenor)

"""2. Calcular la distancia al origen de dos puntos y hallar la menor."""

# Pedir al usuario que ingrese los valores de las abscisas y las ordenadas.

x1 = ValidacionDeDatos.validarReales("\nIngrese x1: ")
y1 = ValidacionDeDatos.validarReales("Ingrese y1: ")
x2 = ValidacionDeDatos.validarReales("Ingrese x2: ")
y2 = ValidacionDeDatos.validarReales("Ingrese y2: ")

# Calcular las distancias de los puntos al origen.

distancia1 = math.sqrt(math.pow(float(x1), 2) + math.pow(float(y1), 2))
distancia2 = math.sqrt(math.pow(float(x2), 2) + math.pow(float(y2), 2))

if distancia1 > distancia2:
    menorDistancia = distancia2
    print("La distancia 2 de ", format(distancia2, ".3f"), " es menor.")
elif distancia1 < distancia2:
    menorDistancia = distancia1
    print("La distancia 1 de ", format(distancia1, ".3f"), " es menor.")
else:
    print("Las distancias son iguales.")


"""3. calcular el salario semanal de 3 empleados"""

# Ingresar el valor de la hora trabajada.
valorHora = 4833

# Ingresar las horas trabajadas por cada empleado y los descuentos.
pagoSemanal = [ ]
contador = 0

while contador < 3:
    horasTrabajadas = ValidacionDeDatos.validarEnteros("\nIngrese el número de horas trabajadas por el empleado: ")
    descuentos = ValidacionDeDatos.validarEnteros("Ingrese el total de los descuentos del empleado: ")

    pagoSemanalEmpleado = (valorHora * horasTrabajadas) - descuentos

    pagoSemanal.append(pagoSemanalEmpleado)

    contador += 1

if pagoSemanal[0] > pagoSemanal[1]:

    if pagoSemanal[0] > pagoSemanal[2]:
        pagoMayor = pagoSemanal[0]
    else:
        pagoMayor = pagoSemanal[2]

else:
    if pagoSemanal[1] > pagoSemanal[2]:
        pagoMayor = pagoSemanal[1]
    else:
        pagoMayor = pagoSemanal[2]

print("El pago mayor es: ", pagoMayor)