
def pintar_rectangulo(lado):
    pintarFilaInferiorYSuperior(lado)
    for x in range(lado):
        pintarFilaIntermedia(lado)
    pintarFilaInferiorYSuperior(lado)

def pintarFilaInferiorYSuperior(n):
    salida = ''
    for x in range(n):
        salida = salida + 'X'
    print(salida)

def pintarFilaIntermedia(n):
    salida = 'X'
    for x in range(n-2):
        salida = salida + ' '
    salida = salida + 'X'
    print(salida)

entrada = int(raw_input('Introduzca el lado del cuadrilatero: '))

pintar_rectangulo(entrada)