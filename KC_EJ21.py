
try:
    entrada = int(raw_input('Introduzca un nuemro natural:'))
    if(entrada < 0):
        print('No introdujo un numero natural')
    else:
        for num in range(1,11):
            salida = entrada * num
            mensaje = str(entrada) + 'x' + str(num) + '=' + str(salida)
            print(mensaje)

except ValueError:
    print('No introdujo un numero')