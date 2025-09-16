"""
Einfache Benutzereingabe und Ausgabe mit f-Strings
"""

name: str = input("Bitte gib deinen Namen ein: ") # 1. Die Funktion input("irgendein Text") zeigt den Text in der Konsole an und wartet auf eine Eingaben.
print(f"Du heißt: {name}")

alter: int = int(input("Bitte gib dein Alter ein: "))
print(f"Du bist {alter} Jahre alt.")

print(type(name))  # 2. name = string
print(type(alter)) #    alter = intenger