

print("Introduzca 3 valores enteros")

try:
    numeros = []
    for numero in range(3):
         numeros.append(int(raw_input("Numero:")))
    numeros.sort()
    print("El mayor numero es: " + str(numeros[2]))
    print("El menor numero es: " + str(numeros[0]))


except ValueError:
    print "Valor no entero"
