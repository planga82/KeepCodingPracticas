# Ejercicio 3
import math

def validaEntrada(string):
    try:
        numero = float(string)
        return True,numero
    except ValueError:
        print('No ha introdcido un numero: ' + string)
        return False,None

correcto1 = False
while not correcto1:
    entrada = raw_input("Introduzca numero Euros: ")
    correcto1, euros = validaEntrada(entrada)

dolares = round(euros * 1.006,2)
print("$" + str(dolares)  + " USD")