

def pintar_fila():
    print('<tr><td></td></tr>')

numeroFilas = int(raw_input("Introduzca el numero de filas: "))

print('<table>')
for n in range(numeroFilas):
    pintar_fila()
print('</table>')