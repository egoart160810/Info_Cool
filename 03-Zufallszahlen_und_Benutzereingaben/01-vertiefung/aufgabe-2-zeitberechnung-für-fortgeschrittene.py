import random
Zeit = random.randint(1200, 2100) # Zeit in Sekunden
Minuten = Zeit // 60
Sekunden = Zeit % 60
print(f"{Zeit} Sekunden sind {Minuten} Minuten und {Sekunden} Sekunden.")