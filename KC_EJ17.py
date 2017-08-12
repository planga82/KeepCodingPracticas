
diccionario = {'Pedro':'pedro.picapiedra@gmail.com','Pablo':'pmarmol123@gmail.com','Bob':'bob@gmail.com'}

nombre = raw_input('Introduzca el nombre: ')

if diccionario.has_key(nombre):
    print(diccionario[nombre])
else:
    print('El nombre no se encuentra en el diccionario')
    