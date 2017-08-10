# Ejercicio 5
import math


mes = []
anio = []

for numero in range(2):
    mes.append(raw_input("mes " + str(numero) + " "))
    anio.append(raw_input("anio " + str(numero) + " "))

print(mes[0] == mes[1] and anio[0] == anio[1])
