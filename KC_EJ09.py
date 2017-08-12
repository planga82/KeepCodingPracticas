
print("Elija la opcion para convertir:")
print("1: Euros a USD")
print("2: USD a EUROS")
opcion = raw_input("Opcion: ")


try:
    cantidad = float(raw_input("Catidad a convertir: "))
    if opcion == "1":
        dolares = round(cantidad * 1.006, 2)
        print("$" + str(dolares) + " USD")
    elif opcion == "2":
        euros = round(cantidad / 1.006,2)
        print(str(euros) + " Euros")
    else:
        print("opcion invalida")
except ValueError:
    print("Cantidad incorrecta")