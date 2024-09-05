import random
def nopanheitto(tahkot):
    heitto = random.randint(1,tahkot)
    return heitto

luku=0
maksimi = int(input("Anna nopan tahkojen määrä:"))

while luku != maksimi:
    luku = nopanheitto(maksimi)
    print(luku)