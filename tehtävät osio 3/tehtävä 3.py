sukupuoli = input("Anna sukupuoli (mies tai nainen):")
hemoglobiini = int(input("Anna hemoglobiini (g/l):"))
if sukupuoli == "mies" and 134 <= hemoglobiini <= 195 or sukupuoli == "nainen" and 117 <= hemoglobiini <= 175:
    print("Hemoglobiinin arvo on normaali")
elif sukupuoli == "mies" and hemoglobiini < 134 or sukupuoli == "nainen" and hemoglobiini < 117:
    print("Hemoglobiinin arvo on alhainen.")
elif sukupuoli == "mies" and hemoglobiini > 195 or sukupuoli == "nainen" and hemoglobiini > 175:
    print("Hemoglobiinin arvo on korkea.")
else:
    print("Virhe. Ilmoitetut tiedot ovat väärässä muodossa.")
