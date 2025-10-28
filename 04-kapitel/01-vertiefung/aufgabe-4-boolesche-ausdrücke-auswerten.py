# Variablen und Zuweisungen
b1: bool = True
b2: bool = False
x: int = 17
y: int = 9
txt1: str = ""
txt2: str = "Hallo Welt"

# Boolesche Ausdrücke zum Auswerten
print(b1 and b2)                                             # True
print(b1 or b2)                                              # True
print(not b2)                                                # True
print(x > y)                                                 # False
print(x != y)                                                # True
print(bool(txt1) and y < x)                                  # True
print(bool(txt2) or b2)                                      # True
print((b1 or b2) and (bool(txt1) or bool(txt2)) and True)    # False
print(not (0 or ""))                                         # True
print("10" > "2")                                            # True
print("a" in "Hallo, Welt!")                                 # True
print("Python" not in "Hallo, Welt!")                        # True
print((x > y) and (b1 or b2) and (bool(txt1) or bool(txt2))) # False
print(x > y is not b1)                                       # True