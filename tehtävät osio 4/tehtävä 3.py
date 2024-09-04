numero = int(input("Anna luku:"))
korkein = numero
pienin = numero
paalla = 1
luku = 0
while paalla == 1:
    luku = (input("Anna luku:"))
    if luku == "":
        print(f"Korkein luku on {korkein} ja pienin luku on {pienin}.")
        break
    luku = int(luku)
    if luku >= korkein:
        korkein = luku
    elif luku <= pienin:
        pienin = luku