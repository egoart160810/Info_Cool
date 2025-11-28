spielzeug = ["Ball", "Puppe", "Auto", "Puzzle", "Buch", "Teddy", "Lego", "Karten"]

print(spielzeug[:3])


print(spielzeug[-2:])


print(spielzeug[2:5])

neue_spielzeuge = spielzeug[:]

print(neue_spielzeuge[::2])

spielzeug.reverse()
print(spielzeug)