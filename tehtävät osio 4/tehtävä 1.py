numero = 0
tosi = 1
while tosi == 1:
    if numero > 1000:
        tosi = 0
    elif numero % 3 == 0:
        print(numero)
        numero = numero + 1
    else:
        numero = numero + 1
print("Kiitos ohjelman käytöstä.")