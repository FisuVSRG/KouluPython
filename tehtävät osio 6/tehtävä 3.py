def gallonamuutos(gallona):
    litra = gallona * 3.785
    return litra

gallona = 1
while gallona >= 0:
    gallona = int(input("Anna gallonien määrä, negatiivinen lopettaa ohjelman toiminnan:"))
    if gallona >= 0:
        print(gallonamuutos(gallona))
print("Kiitos ohjelman käyttämisestä.")