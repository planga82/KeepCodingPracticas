

letra = raw_input("Introduzca una letra:")
if not letra.isalpha():
    print("No ha introducido una letra")
elif len(letra) != 1:
    print("Ha introducido mas de una letra")
else:
    vocales = ['A','E','I','O','U']
    if letra.upper() in vocales:
        print("Es una vocal")
    else:
        print("Es una consonante")
