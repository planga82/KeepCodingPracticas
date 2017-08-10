def validaEntrada(string):
    try:
        numero = int(string)
        return True,numero
    except ValueError:
        print('No ha introdcido un numero: ' + string)
        return False,None

correcto1 = False
while not correcto1:
    entrada = raw_input("Introduzca un numero: ")
    correcto1, numero1 = validaEntrada(entrada)


if numero1 % 2 == 0:
    parImpar = 'par'
else:
    parImpar = 'impar'

if numero1 > 0:
    posNeg = 'positivo'
elif numero1 < 0:
    posNeg = 'negativo'
else:
    posNeg = 'cero'

print(parImpar + "," + posNeg)