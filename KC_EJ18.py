
try:
    numero = int(raw_input('Introduzca un numero: '))
    lista = []
    for i in range(1,numero+1):
        lista.append(str(i))
    print(','.join(lista))
except ValueError:
    print('Valor no numerico')