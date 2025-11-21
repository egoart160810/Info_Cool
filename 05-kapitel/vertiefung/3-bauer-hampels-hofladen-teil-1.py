name = str = input("Guten Tag, könnte ich Ihren Namen wissen? (Gib den Namen ein: ")

waren: list[str] = ["Äpfel", "Birnen", "Erdbeeren", "Kartoffeln", "Eier"] # type: ignore

print(f"Ich hab folgende Produkte im Angebot: {waren}")

wunsch = str = input(f"Was willst du denn kaufen, {name}? Sag ruhig: ")

if wunsch in waren:
    preis: list[float] = [2.59, 2.79, 4.29, 5.99, 2.29]
    idx = waren.index(wunsch)
    print(f"Bitte schön, hier sind ihre {wunsch}.")
    print(f"Es werden dann {preis[idx]}")

elif wunsch not in waren:
    print(f"Schade, wir haben leider keine {wunsch}.")


print(f"Tschüss, bis zum nächsten Mal, {name}!")




