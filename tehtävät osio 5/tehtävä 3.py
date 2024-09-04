luku = int(input("Anna luku tai lopeta painamalla enter:"))

if luku == 1 or luku == 2:
    print("Luku on alkuluku.")
    exit(0)

for i in range(3, luku):
    if luku % i == 0:
        print("Ei ole alkuluku.")
        exit(0)

print(f"{luku} on alkuluku.")