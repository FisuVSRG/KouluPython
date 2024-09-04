luvut = []
luku = input("Anna luku tai lopeta painamalla Enter:")
while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luku = input("Anna luku tai lopeta painamalla Enter:")
luvut.sort(reverse=True)
print(luvut[0:5])