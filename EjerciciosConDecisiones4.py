import ValidacionDeDatos
import sys
import math

"""1. Validar si un código de 3 cifras es correcto"""

# Pedimos que se ingrese el código.

codigo = input("Ingrese el código de tres dígitos: ")

if len(codigo) != 3:                                           # Validamos que el código sea de tres dígitos.
    print("Error, ingrese un código de 3 digitos")
else:
    # Recorrer el String para validar que si sean dígitos entre 0 y 9 y convertir cada dato en un entero.

    cifrasCodigo = [ ]                                         # Almacenar cada uno de los dígitos del código.
    for digito in codigo:
        try:
            cifrasCodigo.append(int(digito))
        except ValueError as e:
            print("Error, ingrese solo digítos entre 0 y 9", file=sys.stderr)
            sys.exit()

    # print("cifrasCodigo = ", cifrasCodigo[0], cifrasCodigo[1], cifrasCodigo[2])

    # Verificar si el código es correcto.

    productoDigitos = cifrasCodigo[0] * cifrasCodigo[1]        # Almacenar el producto de los dos primeros dígitos.
    moduloDiez = productoDigitos % 10                          # Almacenó el residuo de la división.

    if moduloDiez == cifrasCodigo[2]:
        print("Código válido")
    else:
        print("Código invalido")


"""2. Calcular el indice de masa corporal de una persona"""

# Pedir que se ingrese el peso y la masa.
pesoCorporal = ValidacionDeDatos.validarReales("\nPeso(kgs): ")
estatura = ValidacionDeDatos.validarReales("Estatura(mts): ")

# Calculamos el IMC.
imc = float(pesoCorporal) / math.pow(float(estatura), 2)
print("Indice de masa corporal = ", format(imc, ".4f"))

# Mostramos el reporte de salud.
if imc < 20:
    print("Desnutrido")
elif imc >= 20 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Obesidad grado 1")
elif imc >= 35 and imc < 40:
    print("Obesidad grado 2")
else:
    print("Obesidad grado 3")


"""3. Calcular el número de votos favorables de un participante"""

# Ingresar el voto de los tres jueces.
juez1 = ValidacionDeDatos.validarEnteros("\nVoto: ")
juez2 = ValidacionDeDatos.validarEnteros("Voto: ")
juez3 = ValidacionDeDatos.validarEnteros("Voto: ")

if juez1 == 0 or juez1 == 1:
    if juez2 == 0 or juez2 == 1:
        if juez3 == 0 or juez3 == 1:

            if juez1 == juez2 == juez3 == 1:
                print("CONTINUA")
            elif juez1 == juez2 == 1:
                print("CONTINUA")
            elif juez1 == juez3 == 1:
                print("CONTINUA")
            elif juez2 == juez3 == 1:
                print("CONTINUA")
            else:
                print("ELIMINADO")

        else:
            print("Error juez 3, ingrese 0 o 1")
    else:
        print("Error juez 2, ingrese 0 o 1")
else:
    print("Error juez 1, ingrese 0 o 1")





