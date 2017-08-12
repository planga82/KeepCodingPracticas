

def eliminaBlancos(texto):
    return ''.join(texto.split(' '))

def esPalindromo(textoSinBlancos):
    lista1 = list(textoSinBlancos)
    lista2 = lista1[:]
    lista2.reverse()
    return lista1 == lista2

entrada = raw_input('Introduzca una frase: ')
entrada = eliminaBlancos(entrada)
if esPalindromo(entrada):
    print('El texto es palindromo')
else:
    print('El texto no es palindromo')