
bebidas=['Fanta','Pepsi','7Up']
monedas=['10 cent','20 cent','50 cent','1 euro']
mapaMonedasValor = {'10 cent':0.1,'20 cent':0.2,'50 cent':0.5,'1 euro':1}
precioBebida = 1

def imprimeOpcionesLista(lista):
    indice = 1
    for x in lista:
        print('Opcion ' + str(indice) +  ': ' + str(x))
        indice = indice + 1

def haLlegadoAlEuro(cantidad):
    return cantidad>=1,cantidad-1


print('Seleccione la bebida')
imprimeOpcionesLista(bebidas)
opcion = int(raw_input('Opcion: '))
bebida = bebidas[opcion-1]
print('Bebida seleccionada: ' + bebida)
print('Inroduzca la opcion de las monedas que va introduciendo')
imprimeOpcionesLista(monedas)


cantidad = 0
while cantidad < 1:
    opcion = int(raw_input('Opcion: '))
    cantidad = cantidad + mapaMonedasValor[monedas[opcion-1]]
resto = cantidad - 1
print(bebida + ' apunto de caer')
print('Cambio: ' + str(resto * 100) + ' centimos')
