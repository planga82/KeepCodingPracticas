listaNombres = ['Pedro Picapiedra', 'Pablo Marmol', 'Bob Esponja', 'Patricio']

indice = raw_input("Introduzca el indice de la lista: ")

try:
    indice = int(indice)
    if(indice<0 or indice>3):
        print('indice no valido')
    else:
        print(listaNombres[indice])
except ValueError:
    print('Valor no numerico')