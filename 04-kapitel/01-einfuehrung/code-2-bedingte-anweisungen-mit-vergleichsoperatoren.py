"""
Bedingte Anweisungen mit Vergleichsoperatoren
"""

zahl: int = int(input("Gib eine ganze Zahl ein: "))

if zahl > 0:
    print(f"{zahl} ist größer als 0.")

if zahl < 0:
    print(f"{zahl} ist kleiner als 0.")

if zahl == 0:
    print(f"{zahl} ist gleich 0.")

if zahl >= 0:
    print(f"{zahl} ist größer oder gleich 0.")

if zahl <= 0:
    print(f"{zahl} ist kleiner oder gleich 0.")

if zahl != 0:
    print(f"{zahl} ist nicht gleich 0.")

# "if" auf Deutsch ist "wenn"

# 0: 0 == 0; 0 <= 0; 0 >= 0
#-5: -5 < 0; -5 != 0; -5 <= 0
# 5: 5 > 0; 5 != 0; 5 >= 0

# Wenn der Ausdruck nach dem if wahr bzw. falsch ist, wird True oder False auf dem Terminal ausgegeben.