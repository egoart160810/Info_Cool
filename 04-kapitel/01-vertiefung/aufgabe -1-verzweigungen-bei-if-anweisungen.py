"""
Bedingte Anweisungen mit if, elif und else.
"""

zahl: int = int(input("Bitte eine Zahl eingeben: "))
msg: str = ""

if zahl > 0:
    msg = "Die Zahl ist größer 0!"
elif zahl < 0:
    msg = "Die Zahl ist kleiner 0!"
else:
    msg = "Treffer!"

print(msg)



# 10: Die Zahl ist größer 0!

# -7: Die Zahl ist kleiner 0!

# 0: Treffer!

# 'Hallo': Fehler


# Es wird überprüft, ob die Zahl größer als 0, kleiner als 0 oder gleich 0 ist.

#  True: wird zu "Die Zahl ist größer 0!" ausgewertet. # False: wird zu "Die Zahl ist kleiner 0!" ausgewertet.

# a: zahl > 0: msg = "Die Zahl ist größer 0!"; b: zahl < 0: msg = "Die Zahl ist kleiner 0!"; c: else: msg = "Treffer!".; c: else: msg = "Treffer!".; d: Fehler




                                                                                    