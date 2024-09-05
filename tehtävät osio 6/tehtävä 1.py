import random
luku = 0
def nopanheitto():
    heitto = random.randint(1,6)
    return heitto
while luku != 6:
    luku = nopanheitto()
    print(luku)