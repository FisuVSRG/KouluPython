import math

def pizzalaskuri(halkaisija, hinta):
    sade = halkaisija / 2
    pintaala = sade * sade * math.pi
    arvo = pintaala / hinta
    return arvo

halkaisija1 = int(input("Anna pizzan halkaisija senttimetreinä: "))
hinta1 = int(input("Anna pizzan hinta euroina: "))
arvo1 = pizzalaskuri(halkaisija1, hinta1)

halkaisija2 = int(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = int(input("Anna toisen pizzan hinta euroina: "))
arvo2 = pizzalaskuri(halkaisija2, hinta2)


if arvo1 > arvo2:
    print("Ensimmäinen pizza on paremman arvoinen kuin toinen.")
elif arvo1 == arvo2:
    print("Pizzat ovat samanarvoiset")
else:
    print("Toinen pizza on paremman arvoinen kuin ensimmäinen.")