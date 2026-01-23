
x = -20
while x < 20:
    print(x)
    x += 1


y = 100
while y > 0:
    print(y)
    y -= 1


z = 7
while z < 100:
    print(z)
    z += 7


v = 1
quadrat = v * v
v = int = 1
while quadrat < 1000:
    print(quadrat)
    v += 1
    quadrat = v * v


import random

o = int = random.randint(1, 10)
while o != 7:
    print(o)
    o = int = random.randint(1, 10)

if o == 7:
    print(o)


wort = str = input("Gib bitte Exit ein: ")
wort_list = str = []
while wort != "Exit":
    wort_list.append(wort)
    wort = str = input("Gib bitte Exit ein: ")

if wort == "Exit":
    print(wort_list)


zahl_a = int = random.randint(1, 6)
zahl_b = int = random.randint(1, 6)

while zahl_a != zahl_b:
    print(f"Erste Zahl {zahl_a}")
    print(f" Zweite Zahl {zahl_b}")
    zahl_a = int = random.randint(1, 6)
    zahl_b = int = random.randint(1, 6)

if zahl_a == zahl_b:
    print("PASCH!")
    print(f"Erste Zahl {zahl_a}")
    print(f" Zweite Zahl {zahl_b}")

wuerfel_a = 1
wuerfel_b = 1

while wuerfel_a != 7 and wuerfel_b != 7:

    print(f"{wuerfel_a} - {wuerfel_b}")
    wuerfel_b += 1

    if wuerfel_b == 7:
        wuerfel_b = 1
        wuerfel_a += 1


 