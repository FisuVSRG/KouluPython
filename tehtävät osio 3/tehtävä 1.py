kuhan_pituus = int(input("Anna kuhan pituus senttimetreinä:"))
puuttuva_mitta = 0
if kuhan_pituus < 37:
    puuttuva_mitta = 37 - kuhan_pituus
    print(f"Laske kuha takaisin järveen, sen mitasta puuttuu {puuttuva_mitta} senttimetriä.")
else:
    print("Kuha on sopivan mittainen.")