
try:
    personasDerechoVoto = []
    for i in range(10):
        nombre = raw_input('Introduzca nombre: ')
        edad = int(raw_input('Introduzca edad: ' ))
        if edad>=18:
            personasDerechoVoto.append(nombre)

    print('Pesonas con derecho a voto: ' + ','.join(personasDerechoVoto))

except ValueError:
    print('No introdujjo un numero')

