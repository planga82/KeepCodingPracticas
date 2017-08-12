

def segundoElementoTupla(tupla):
    element1,element2 = tupla
    return element2

terminar=False
print('Introduzca nombre y calificaciones separadas por comas o "terminar" para salir')
print('Ejemplo: Pedro 6,8,7')
listaPersonasCalificaciones = []
while not terminar:
    entrada = raw_input('Entrada: ')
    if entrada == "terminar":
        terminar = True
    else:
        nombre = entrada.split(' ')[0]
        listacalificaciones = entrada.split(' ')[1].split(',')
        listacalificaciones = map(int,listacalificaciones)
        calificacionMedia = round(sum(listacalificaciones) * 1.0 / len(listacalificaciones), 2)
        listaPersonasCalificaciones.append((nombre,calificacionMedia))

print('Media de calificaciones')

listaPersonasCalificaciones.sort(key=segundoElementoTupla, reverse=True)
for persona,claificacion in listaPersonasCalificaciones:
    print(persona + ' ' +  str(claificacion))
