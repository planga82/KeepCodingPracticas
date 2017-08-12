
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
        listaPersonasCalificaciones.append((nombre,listacalificaciones))

print('Media de calidicaciones')

for persona,claificacion in listaPersonasCalificaciones:
    calificacionMedia = round(sum(claificacion)*1.0/len(claificacion),2)
    print(persona + ' ' +  str(calificacionMedia))
