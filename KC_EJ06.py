
# Ejercicio 6
import math

def validaEntrada(string):
    try:
        numero = int(string)
        return True,numero
    except ValueError:
        print('No ha introdcido un numero: ' + string)
        return False,None

correcto1 = False
correcto2 = False
while not correcto1 or not correcto2:
    entrada = raw_input("Introduzca un numero: ")
    entrada2 = raw_input("Introduzca otro numero: ")
    correcto1, numero1 = validaEntrada(entrada)
    correcto2, numero2 = validaEntrada(entrada2)


print(str(numero1) + " < " + str(numero2) + " = " + str(numero1 < numero2))
print(str(numero1) + " > " + str(numero2) + " = " + str(numero1 > numero2))
print(str(numero1) + " y " + str(numero2) + " son iguales = " + str(numero1 == numero2))
print(str(numero1) + " y " + str(numero2) + " son distintos = " + str(numero1 != numero2))



