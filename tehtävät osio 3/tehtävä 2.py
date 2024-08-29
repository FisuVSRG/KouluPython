hyttiluokka = input("Anna laivan hyttiluokka: \n1. LUX \n2. A \n3. B \n4. C\n")
if hyttiluokka == "1":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "2":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "3":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "4":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")