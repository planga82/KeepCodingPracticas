# -*- coding: Cp1252 -*-

import random

numeroAdivinar = random.randint(1,100)

print('Numero a adivinar: '  + str(numeroAdivinar))

for oportunidad in range(1,6):
    entrada = int(raw_input('Introduzca un numero: '))
    if entrada == numeroAdivinar:
        print('¡Bien, has adivinado!')
        break
    else:
        if entrada > numeroAdivinar:
            print('Intenta con un numero menor (Te quedan ' + str(5-oportunidad) + ' intentos)')
        else:
            print('Intenta con un mayor menor (Te quedan ' + str(5-oportunidad) + ')')

