"""1. Determinar el equivalente en años, meses y días de un número."""

from ValidacionDeDatos import *

# Pedir que se ingrese el número de días.
diasAConvertir = validarEnteros("Ingrese un número entero: ")

# Calcular el equivalente en años.
equivalenteEnAños = diasAConvertir // 365

# Calcular el equivalente en meses.
equivalenteEnMeses = (diasAConvertir % 365) // 30

# Calcular el equivalente en días.
equivalenteEnDias = (diasAConvertir % 365) % 30

print("El Equivalente de", diasAConvertir, "es:", equivalenteEnAños, "Años", equivalenteEnMeses, "Meses", equivalenteEnDias, "Días")


"""2. Sumar las cifras centrales de dos números de tres cifras"""

# Definir una función para realizar ambas divisiones.
def hallarCifraCentral(numero):

    primeraConversion = numero // 10            # Truncar para reducir de 3 a 2 cifras.
    cifraCentral = primeraConversion % 10       # Dividimos por 10 para hallar el residuo que es la cifra del medio.

    return cifraCentral

listaCifrasCentrales = [ ]
for i in range(0, 2, 1):

    numeroTresCifras = validarEnteros("\nIngrese un número entero de 3 cifras: ")   # Ingresar número.
    listaCifrasCentrales.append(hallarCifraCentral(numeroTresCifras))               # Invocamos el método para hallar la cifra central.


sumaCifrasCentrales = listaCifrasCentrales[0] + listaCifrasCentrales[1]
print("la suma de las cifras centrales es: ",sumaCifrasCentrales)


"""3. Equivalente en cantidad de billetes de un número"""

# Pedir que se ingrese el número.
cantidadDolares = validarEnteros("\nIngrese la cantidad de dolares: ")

cantidadBilletesCien = cantidadDolares // 100                                       # Cantidad de billetes de 100.
if cantidadDolares % 100 != 0:
    cantidadBilletesCincuenta = (cantidadDolares % 100) // 50                       # Cantidad de billetes de 50.

    if ((cantidadDolares % 100) % 50) != 0:
        cantidadBilletesVeinte = ((cantidadDolares % 100) % 50) // 20

        if (((cantidadDolares % 100) % 50) % 20) != 0:
            cantidadBilletesDiez = (((cantidadDolares % 100) % 50) % 20) // 10

            if((((cantidadDolares % 100) % 50) % 20) % 10) != 0:
                cantidadBilletesCinco = ((((cantidadDolares % 100) % 50) % 20) % 10) // 5

                if (((((cantidadDolares % 100) % 50) % 20) % 10) % 5) != 0:
                    cantidadBilletesUno = (((((cantidadDolares % 100) % 50) % 20) % 10) % 5) // 1

            else:
                cantidadBilletesUno = 0
                cantidadBilletesCinco = 0

        else:
            cantidadBilletesUno = 0
            cantidadBilletesCinco = 0
            cantidadBilletesDiez = 0

    else:
        cantidadBilletesUno = 0
        cantidadBilletesCinco = 0
        cantidadBilletesDiez = 0
        cantidadBilletesVeinte = 0

else:
    cantidadBilletesUno = 0
    cantidadBilletesCinco = 0
    cantidadBilletesDiez = 0
    cantidadBilletesVeinte = 0
    cantidadBilletesCincuenta = 0

print("$", cantidadDolares, "equivale a: ", cantidadBilletesCien, "billetes de cien +", cantidadBilletesCincuenta,
     "billetes de cincuenta +", cantidadBilletesVeinte, "billetes de veinte +", cantidadBilletesDiez, "billetes de diez +",
     cantidadBilletesCinco, "billetes de cinco +", cantidadBilletesUno, "billetes de uno")