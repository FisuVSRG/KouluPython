def lukulistat(luvut):
    parilliset = []
    for i in luvut:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

kokonaisluvut = [1, 2, 3, 4, 5, 6, 7, 8]
parilliset = lukulistat(kokonaisluvut)
print(kokonaisluvut)
print(parilliset)
