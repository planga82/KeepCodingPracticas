
try:
    entrada = int(raw_input("Introduzca un entero: "))
    mensaje = ''
    salida = 0
    for num in range(1,entrada + 1):
        if num != 1:
            mensaje = mensaje + '+' + str(num)
        else:
            mensaje = mensaje + str(num)
        salida = salida + num
    print('Suma de nuemros: ' + mensaje + ' = ' + str(salida))

except ValueError:
    print('No introdujo un entero')