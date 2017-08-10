
# Ejercicio 1
import math

correcto = False
while not correcto:
    entrada = raw_input("Radio del circulo: ")
    try:
        radio = int(entrada)
        correcto = True
        area = round(math.pi * radio ** 2,1)
        print("El area del circulo es: " + str(area))
    except ValueError:
        print('El valor introducido no es un numero')