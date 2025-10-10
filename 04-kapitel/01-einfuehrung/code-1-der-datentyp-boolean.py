"""
Mit dem Datentyp bool experimentieren
"""

print(17 > 5)
# Ausgabe der Konsole: True. Beobachtung: 17 > 5 ist richtig, also True.

print(17 < 5)
# Ausgabe der Konsole: False. Beobachtung: 17 < 5 ist falsch, also False.

print(type(17 > 5))
# Ausgabe der Konsole: <class 'bool'>. Beobachtung: Der Datentyp von 17 > 5 ist bool.

x = 17 > 5
y = 17 < 5

print(x, y)
# Ausgabe der Konsole: True False. Beobachtung: x ist True, weil x = 17 > 5 und 17 > 5 richtig ist. y ist False, weil y = 17 < 5 und 17 < 5 falsch ist.

print(type(x), type(y))
# Ausgabe der Konsole: <class 'bool'> <class 'bool'>. Beobachtung: Der Datentyp von x und y ist bool.

# Die beiden bool Werte sind True und False. Er wird verwendet, um herauszufinden, ob eine Aussage richtig oder falsch ist.