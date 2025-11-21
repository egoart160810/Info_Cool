
Anweisungen	koffer_lisa	koffer_paul
# Lisa und Paul fahren in Urlaub — also müssen sie ihre Koffer packen!

koffer_lisa = ["Pullover", "Pullover", "kurze Hose", "lange Hose", "Duschgel"] # In Lisas Koffer sind 2 Pullover, kurze Hose, lange Hose und Duschgel.

koffer_paul = [] # Paul hat nocht nichts im Koffer

koffer_lisa.append("Haarbürste") # Lisa legt in ihren Koffer noch eine Zahnbürste dazu.

koffer_lisa.append("Turnschuhe") # Fügt noch die Turnschue hinzu.

koffer_lisa.insert(2, "Pullover") # Zwischen den 2 Pullovern und kurzer Hose kommt noch ein Pullover dazu.

koffer_paul.append("Laptop") # Pauel steckt in seinen Koffer seinen(oder geklauten) Leptop.

koffer_paul.append("Fußball") # Er fügt den Fußball hinzu

koffer_paul.append(koffer_lisa[0]) # Pauel nimmt sich den ersten Pullover von Lisa und legt es in seinen Koffer.

koffer_paul.insert(0, koffer_lisa[-1]) # Pauel fügt seinem Koffer Lisas Duschgel hinzu.

koffer_paul.remove("Fußball") # Der Fußball verlässt Pauels Koffer.

koffer_paul.insert(koffer_paul.index("Laptop"), "Stromkabel")

koffer_lisa.insert(3, koffer_paul.pop(1))

koffer_paul.append(koffer_lisa.pop(len(koffer_lisa) - 3))