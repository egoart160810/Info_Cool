"""
Formatierte Ausgaben.
"""

x: int = 7
y: int = 9
z: int = x + y

print(str(z) + " = " + str(x) + " + " + str(y))
print(f"{z} = {x} + {y}")
# Man braucht eine  Typ-Konvertierung um die 16, die 7 und die 9 mit dem "=" zu verbinden, ohne das es ein Fehler anzeigt.
# Der f-String konvertiert alles was in den {} steht in string und verbindet es automatisch mit dem was außerhalb ist, also braucht man nicht die ganze Zeit str(), "" und + benutzen.