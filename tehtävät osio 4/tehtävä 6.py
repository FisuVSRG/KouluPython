import random
pisteet = 0
n = 0
N = int(input("Anna laskettavien pisteiden määrä:"))
while pisteet < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x * x + y * y < 1:
        n = n + 1
    pisteet = pisteet + 1
pii = 4 * n / N
print(f"{pii}")
