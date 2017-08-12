
valores = list(range(1,21))

inicioRago = int(raw_input("Introduzca el inicio del rango: "))
if inicioRago in range(1,21):
    finRango = int(raw_input("Introduzca el fin del rango: "))
    if finRango in range(1, 21):
        lista = valores[inicioRago:finRango]
        print(','.join(str(e) for e in lista))
    else:
        print("El rango debe ser de 1 a 20")
else:
    print("El rango debe ser de 1 a 20")