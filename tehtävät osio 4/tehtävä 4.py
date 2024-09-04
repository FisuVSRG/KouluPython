import random
paalla = 1
arvaus = 0
numero = random.randint(1,11)
while paalla == 1:
    arvaus = int(input("Arvaa numero 1-10:"))
    if numero == arvaus:
        print("Oikein. Voitit pelin.")
        paalla = 0
    elif numero > arvaus:
        print("Liian pieni arvaus.")
    elif numero < arvaus:
        print("Liian suuri arvaus.")