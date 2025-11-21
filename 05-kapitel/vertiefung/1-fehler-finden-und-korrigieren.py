haupt_staedte: list[str] = ["Berlin", "Oslo", "Wien", "Paris", "London", "Madrid", "Rom"] # IndexFehler, TypeFehler, NameFehler
haupt_staedte.append("Berlin")            
anzahl = len(haupt_staedte)                                                               # Python sagt was für ein Fehler es ist, wo es ist und gibt den Grund, warum es ein Fehler ist.
print("Die Liste besteht aus anzahl europäischen Hauptstädten")
print("Die fünfte Hauptstadt in der Liste ist: " + haupt_staedte[4])
print(f"Die letzte Hauptstadt in der Liste ist: {haupt_staedte[anzahl - 1]}")   