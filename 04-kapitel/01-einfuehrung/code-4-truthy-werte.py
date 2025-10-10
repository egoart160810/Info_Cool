"""
Gängiges Beispiel für Truthiness und Falsiness.
"""

benutzereingabe: str = input("Gib etwas ein: ")

if benutzereingabe:
    print(f"Hast du etwas eingegeben: {bool(benutzereingabe)}")
else:
    print(f"Hast du etwas eingegeben: {bool(benutzereingabe)}")

# Wenn ich nichts eingebe wird auf dem Terminal False ausgegeben.
# Wenn ich etwas eingebe wird auf dem Terminal True ausgegeben.     

# In diesen Code prüfen if und else ob User etwas eigegeben hat oder nicht. 