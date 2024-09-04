paalla = 1
tuuma = 0
sentti = 0
while paalla == 1:
    tuuma = int(input("Anna tuumien määrä:"))
    if tuuma >= 0:
        sentti = tuuma * 2.54
        print(f"{tuuma} tuumaa on {sentti} senttiä.")
    else:
        print("Kiitos ohjelman käytöstä.")
        paalla = 0