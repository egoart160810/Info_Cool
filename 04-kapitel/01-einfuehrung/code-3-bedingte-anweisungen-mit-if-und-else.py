"""
if ... else-Anweisungen
"""

# Variablen deklarieren
zahl: int = int(input("Bitte gib eine ganze Zahl ein: "))

# Die Kontrollstruktur if ... else
if zahl > 0:
    print("Ich bin in der if-Anweisung gelandet.")
    print(f"{zahl} ist größer als 0.")
else:
    print("Ich bin in der else-Anweisung gelandet.")
    print(f"{zahl} ist nicht größer als 0.")

# Der else-Block wird ausgeführt, wenn die Bedingung der if-Anweisung nicht erfüllt ist.