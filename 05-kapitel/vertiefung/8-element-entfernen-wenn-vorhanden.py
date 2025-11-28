
gesucht_spielzeug = str = input("Was suchst du: ")

spielzeug = ["Ball", "Puppe", "Auto", "Puzzle", "Buch", "Teddy", "Lego", "Karten"]

suche = spielzeug.count(gesucht_spielzeug)

print(f"Du hast gefunden: {spielzeug[suche - 1]}")
spielzeug.pop(suche-1)
print(spielzeug)
