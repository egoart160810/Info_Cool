"""
Zufallszahlen erzeugen mit random.random()
"""

import random

zufall: float = random.random() #1. Die Funktion gibt eine zufällige Zahl zwischen 0.0 und 1.0 zurück.
print(f"Zufallszahl: {zufall}") 


zufall = random.random()
print(f"Zufallszahl: {zufall}")

zufall = random.random()
print(f"Zufallszahl: {zufall}")

zufall = random.random()
print(f"Zufallszahl: {zufall}")

print(type(zufall)) #2. Der Datentyp von der Variable "zufall" ist float.



"""
Zufallsauswahl mit random.choice()
"""

import random

zufall = random.choice(["A", "B", "C"])          # 1. Die Funktion random.choice(["A", "B", "C"]) wählt einen zufälligen zwischen "A", "B" und "C" aus.
print(f"Zufällig gewählter Buchstabe: {zufall}")

zufall = random.choice(["A", "B", "C"])
print(f"Zufällig gewählter Buchstabe: {zufall}")

zufall = random.choice(["A", "B", "C"])
print(f"Zufällig gewählter Buchstabe: {zufall}")

zufall = random.choice(["A", "B", "C"])
print(f"Zufällig gewählter Buchstabe: {zufall}")

print(f"Datentyp der Variable 'zufall': {type(zufall)}")

print(type(zufall)) #2. Der Datentyp von der Variable "zufall" ist str.


"""
Liste mischen mit random.shuffle()
"""

import random

# Originale Liste
buchstaben = ["A", "B", "C"]             # 1. Die Funtion random.shuffle(["A", "B", "C"])  mischt die Reihenfolge der Buchstaben.
print(f"Originale Liste: {buchstaben}")

# Liste mischen
random.shuffle(buchstaben)
print(f"Gemischte Liste: {buchstaben}")

# Noch einmal mischen
random.shuffle(buchstaben)
print(f"Nochmals gemischt: {buchstaben}")

# Und noch einmal
random.shuffle(buchstaben)
print(f"Wieder gemischt: {buchstaben}")

# Datentyp überprüfen
zufall = buchstaben
print(f"Datentyp der Variable 'zufall': {type(zufall)}")

print(type(zufall)) #2. Der Datentyp von der Variable "zufall" ist list.