"""1. Convertir temperaturas de Farenheit a Celsius y viceversa"""
import os
import ValidacionDeDatos

# Creamos el menú
def menu():
    os.system('cls')
    print("\t1. Convertir a grados Centigrados.")
    print("\t2. Convertir a grados Farenheit.")
    print("\t3. Salir")

# Mostramos el menú
while True:
    menu()

    # Pedir al usuario que seleccione la opción de conversión.
    opcion = ValidacionDeDatos.validarEnteros("Seleccione una opción: ")

    if opcion == 1:
        # Pedir al usuario el valor de la temperatura
        temperatura = ValidacionDeDatos.validarReales("Ingrese el valor de la temperatura: ")
        centigrados = (5/9) * (float(temperatura) - float(32))
        print("Centigrados = ", format(centigrados, ".3f"))

    elif opcion == 2:
        # Pedir al usuario el valor de la temperatura
        temperatura = ValidacionDeDatos.validarReales("Ingrese el valor de la temperatura: ")
        farenheit = 32 + 9 * (temperatura / 5)
        print("Farenheit = ", format(farenheit, ".3f"))

    elif opcion == 3:
        break

    else:
        print("Error, seleccione una opción correcta")
