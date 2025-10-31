# Variablen und Zuweisungen
b1: bool = True
b2: bool = False
x: int = 17
y: int = 9
txt1: str = ""
txt2: str = "Hallo Welt"

# Boolesche Ausdrücke zum Auswerten
print(b1 and b2)                                             # False, weil True und False ergibt False 
print(b1 or b2)                                              # True, weil nur eine Bedienung richtig sein soll
print(not b2)                                                # True, weil es nicht b2 (False) ist
print(x > y)                                                 # True, weil 17 (x) > 9 (y) ist
print(x != y)                                                # True, weil 17 (x) ungleich 9 (y) ist
print(bool(txt1) and y < x)                                  # False, weil txt1 False ist, weil es leer ist, ergibt txt1 und y < x False
print(bool(txt2) or b2)                                      # True, weil nur eine Bedienung richtig sein soll
print((b1 or b2) and (bool(txt1) or bool(txt2)) and True)    # True, weil "(b1 or b2)"" True ergibt und "(bool(txt1) or bool(txt2)) and True" auch True ergibt
print(not (0 or ""))                                         # True, weil 0 und "" False sind und die Anweisung Lautet NICHT False(0 oder "")
print("10" > "2")                                            # True, weil "10" mehr Zeichen hat als "2"
print("a" in "Hallo, Welt!")                                 # False, weil es kein "a" in "Hallo, Welt!" gibt
print("Python" not in "Hallo, Welt!")                        # True, weil es kein "Python" in "Hallo, Welt!" gibt
print((x > y) and (b1 or b2) and (bool(txt1) or bool(txt2))) # True, weil alles richtig ist
print(x > y is not b1)                                       # True, weil 17 (x) > 9 (y) nicht b1 ist