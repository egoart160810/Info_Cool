#######################################
# Aufgaben zu Methoden des Datentyps Liste
#
# Implementiere die in den Kommentaren beschriebenen Aktionen jeweils unterhalb
# des entsprechenden Kommentars
# - LÖSCHE den Kommentar bitte NICHT! -
#
# Gib zusätzlich jedes Mal den Inhalt der Liste mit einem print-Befehl in der Konsole aus,
# um zu testen, ob dein Code richtig ist.
#######################################
#
# - Lege eine leere Liste mit dem Namen 'farben' an.

# - Füge die Farben 'Blau', 'Grün', 'Gelb' und 'Rot' (Datentyp String) in die Liste ein.

# - Füge 3 Mal den String 'Blau' hinten an die Liste an.

# - Gib aus, wie viele Elemente die Liste hat.

# - Gib aus, wie oft 'Blau' in der Liste vorkommt.

# - Füge die Farbe 'Grün' ganz vorne in die Liste ein.

# - Gib aus, an welchem Index sich die Farbe 'Gelb' befindet und speichere diesen Wert in der
#   Variable 'idx_gelb'.

# - Füge die Farben 'Blau', 'Grün', 'Lila', 'Grün' und 'Blau' hinter 'Gelb' ein. Benutze die
#   Variable 'idx_gelb'.

# - Lösche die Farbe 'Gelb' wieder aus der Liste.

# - Gib aus, an welchem Index sich die Farbe 'Rot' befindet und speichere diesen Wert in der
#   Variable 'idx_rot'.

# - Ersetze 'Rot' durch 'Lila' (benutze die Variable 'idx_rot').

# - Gib aus, an welcher Position sich zum ersten Mal die Farbe 'Grün' befindet.

# - Lösche die zweite Farbe aus der Liste und gib aus, welche Farbe das war.

# - Gib aus, welche Farbe jetzt die zweite Farbe in der Liste ist.

# - Gib aus, welche Farbe als Letztes in der Liste steht.

# - Wenn es die Farbe 'Orange' noch nicht in der Liste gibt, dann füge sie ans Ende der Liste ein.

# - Sortiere die erste Liste.

# - Lösche alle Elemente aus der Liste.





farben: list[str] = []


farben.append('Blau')
farben.append('Grün')
farben.append('Gelb')
farben.append('Rot')

farben.extend(["Blau"] * 3)

print(len(farben))

print(f"Blau: {farben.count("Blau")}")

farben.insert(0, "Grün")

idx_gelb = farben.index("Gelb")
print(idx_gelb)

farben[idx_gelb + 1: idx_gelb + 1] =['Blau', 'Grün', 'Lila', 'Grün', 'Blau']

farben.pop(3)

idx_rot = farben.index("Rot")
print(idx_rot)

farben.pop(idx_rot)
farben.insert(idx_rot, "Lila")

print(f"Zweite Farbe hat den Index: 1 ")
farben.pop(1)

print(f"Die zweite Farbe ist jetzt {farben[1]}")

print(f"Letzte Farbe der Liste ist {farben[-1]}")


farben.append('Orange')

print(sorted(farben))

farben.clear()

print(farben)






# 'Blau', 'Grün', 'Lila', 'Grün' und 'Blau' hinter 'Gelb'