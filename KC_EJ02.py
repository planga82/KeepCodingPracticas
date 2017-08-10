
# Ejercicio 2
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

suma = numero1 + numero2
resta = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2
exp = numero1 ** numero2
mod = numero1 % numero2
print(str(numero1) + "+" + str(numero2) + "=" + str(suma))
print(str(numero1) + "-" + str(numero2) + "=" + str(resta))
print(str(numero1) + "*" + str(numero2) + "=" + str(mult))
print(str(numero1) + "/" + str(numero2) + "=" + str(div))
print(str(numero1) + "**" + str(numero2) + "=" + str(exp))
print(str(numero1) + "%" + str(numero2) + "=" + str(mod))



