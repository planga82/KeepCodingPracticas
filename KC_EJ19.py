
try:
    listaNumeros = []
    for numero in range(10):
        entrada = int(raw_input('Introduzca un entero:'))
        listaNumeros.append(entrada)

    salida = []
    for numero in listaNumeros:
        if numero % 2 == 0:
            salida.append(str(numero))

    print('Son pares: ' + ','.join(salida))
except ValueError:
    print('No introdujo un entero')