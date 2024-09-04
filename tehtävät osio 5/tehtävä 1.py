import random
summa = 0
nopat = int(input("Anna noppien lukumäärä:"))
for i in range(nopat):
    summa = summa + random.randint(1,6)
print (summa)