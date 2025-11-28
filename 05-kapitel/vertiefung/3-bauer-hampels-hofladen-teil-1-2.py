
name = str = input("Guten Tag, könnte ich Ihren Namen wissen? (Gib den Namen ein: ")

waren: list[str] = ["Äpfel", "Birnen", "Erdbeeren", "Kartoffeln", "Eier"] # type: ignore
mengen = [4, 1, 6, 10, 0]

print(f"Ich hab folgende Produkte im Angebot: {waren}")

wunsch = str = input(f"Was willst du denn kaufen, {name}? Sag ruhig: ")
gewuenschte_menge = int = int(input("Wie viel: "))
nein = int = 0

if wunsch in waren:
    preis: list[float] = [2.59, 2.79, 4.29, 5.99, 2.29]
    idx = int = waren.index(wunsch)
    if gewuenschte_menge > mengen[idx]:
        ja_nein = str = input(f"Wir haben leider nur {mengen[idx]} {wunsch}. Soll ich die fehlenden {gewuenschte_menge - mengen[idx]} für morgen bestellen?(Nein oder Ja): ")
        if ja_nein == "Nein":
            print("Gut, dann nicht.")
          
            nein = int = gewuenschte_menge - mengen[idx]
        else:
            print("Mach ich!")
    else:
        print(f"Bitte schön, hier sind ihre {wunsch}.")




    
elif wunsch not in waren:
    print(f"Schade, wir haben leider keine {wunsch}.")

print(f"Es werden dann {preis[idx] * (gewuenschte_menge - nein)}")
print(f"Tschüss, bis zum nächsten Mal, {name}!")




