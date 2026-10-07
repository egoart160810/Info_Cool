---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #312e81 100%);
    color: white;
  }

  section::before {
    content: "";
    position: absolute;
    left: -12%;
    top: -16%;
    width: 72%;
    height: 78%;
    background: radial-gradient(circle at 30% 30%, rgba(168, 85, 247, 0.85), rgba(168, 85, 247, 0.18) 37%, transparent 60%);
    border-radius: 55% 45% 52% 48% / 42% 58% 42% 58%;
    transform: rotate(-16deg);
    filter: blur(6px);
    opacity: 0.9;
  }

  section::after {
    content: "";
    position: absolute;
    right: -8%;
    bottom: -16%;
    width: 70%;
    height: 60%;
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.55), rgba(59, 130, 246, 0.12), transparent);
    border-radius: 52% 48% 0% 100% / 100% 100% 0% 0%;
    transform: rotate(12deg);
    filter: blur(2px);
    opacity: 0.95;
  }

  .float-shape {
    position: absolute;
    z-index: 0;
    opacity: 0.9;
    filter: drop-shadow(0 12px 24px rgba(0,0,0,0.25));
  }

  .triangle {
    width: 120px;
    height: 120px;
    clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
  }

  .t1 { left: 69%; top: 12%; background: rgba(168, 85, 247, 0.75); transform: rotate(18deg); }
  .t2 { left: 18%; top: 62%; background: rgba(59, 130, 246, 0.55); transform: rotate(-18deg); }
  .t3 { left: 76%; top: 56%; background: rgba(45, 212, 191, 0.55); transform: rotate(12deg); }
  .t4 { left: 50%; top: 78%; background: rgba(244, 114, 182, 0.45); transform: rotate(-20deg); }

  h1, h2, h3 {
    position: relative;
    z-index: 1;
    color: white;
    font-weight: 700;
    letter-spacing: -0.03em;
  }

  h1 {
    font-size: 52px;
    margin-top: 150px;
    margin-bottom: 20px;
  }

  h2 {
    font-size: 30px;
    margin-bottom: 15px;
    padding-left: 18px;
    border-left: 7px solid #c084fc;
  }

  p, li {
    position: relative;
    z-index: 1;
    font-size: 24px;
    line-height: 1.5;
    color: #e2e8f0;
  }

  ul {
    position: relative;
    z-index: 1;
    padding-left: 28px;
  }

---

# Passwortmanager

Egor Artamonow

<div class="float-shape triangle t1"></div>
<div class="float-shape triangle t2"></div>
<div class="float-shape triangle t3"></div>
<div class="float-shape triangle t4"></div>

---

<!-- ## Inhaltsverzeichnis

- Was ist ein Passwortmanager
- Wie funktioniert ein Passwortmanager
- Welche Passwortmanager sind sicher
- Was ist ein Masterpasswort

-->

## Was ist ein Passwortmanager?

- Ein Passwortmanager ist ein Programm zur sicheren Verwaltung von Passwoertern.
- Er speichert Zugangsdaten verschluesselt in einem digitalen Tresor.
- Fuer jedes Konto kann ein eigenes, starkes Passwort verwendet werden.
- Der Passwortmanager kann Passwoerter automatisch ausfuellen und neue erstellen.

<div class="float-shape triangle t1"></div>
<div class="float-shape triangle t2"></div>
<div class="float-shape triangle t3"></div>
<div class="float-shape triangle t4"></div>

---

## Wie funktioniert ein Passwortmanager?

- Beim ersten Start wird ein verschluesselter Tresor angelegt.
- Der Tresor wird mit einem Masterpasswort geschuetzt.
- Der Passwortmanager erzeugt bei Bedarf lange und zufaellige Passwoerter.
- Je nach Dienst werden die Daten verschluesselt auf dem Geraet oder in der Cloud gespeichert.
- Mit Synchronisation koennen die Zugangsdaten auf mehreren Geraeten genutzt werden.

<div class="float-shape triangle t1"></div>
<div class="float-shape triangle t2"></div>
<div class="float-shape triangle t3"></div>
<div class="float-shape triangle t4"></div>

---

## Welche Passwortmanager sind sicher?

- Gute Anbieter verwenden starke Verschluesselung und kennen den Inhalt des Tresors nicht.
- Eine unabhaengige Sicherheitspruefung und transparente Informationen sind wichtige Merkmale.
- Zwei-Faktor-Authentifizierung schuetzt zusaetzlich das Benutzerkonto.
- Beispiele fuer bekannte Passwortmanager sind Bitwarden, 1Password und KeePassXC.
- Wichtig: Auch ein guter Dienst ist nur so sicher wie das eigene Masterpasswort.

<div class="float-shape triangle t1"></div>
<div class="float-shape triangle t2"></div>
<div class="float-shape triangle t3"></div>
<div class="float-shape triangle t4"></div>

---

## Welche wichtigen Kriteien soll ein Passwortmanager haben?

<div class="float-shape triangle t1"></div>
<div class="float-shape triangle t2"></div>
<div class="float-shape triangle t3"></div>
<div class="float-shape triangle t4"></div>

---
## Was ist ein Masterpasswort?

- Das Masterpasswort ist der einzige Zugang zum Passwort-Tresor.
- Es sollte lang, einmalig und leicht merkbar sein.
- Am besten eignet sich eine Passphrase aus mehreren zufaelligen Woertern.
- Das Masterpasswort darf nicht in anderen Konten verwendet werden.
- Es sollte nicht ungeschuetzt weitergegeben oder gespeichert werden.

<div class="float-shape triangle t1"></div>
<div class="float-shape triangle t2"></div>
<div class="float-shape triangle t3"></div>
<div class="float-shape triangle t4"></div>

---

## Fazit

- Passwortmanager machen sichere und unterschiedliche Passwoerter alltagstauglich.
- Ein starkes Masterpasswort und Zwei-Faktor-Authentifizierung sind besonders wichtig.
- Vor der Auswahl sollte man Sicherheit, Transparenz und Bedienung vergleichen.
<div class="float-shape triangle t1"></div>
<div class="float-shape triangle t2"></div>
<div class="float-shape triangle t3"></div>
<div class="float-shape triangle t4"></div>

---

## Quellen

<div class="float-shape triangle t1"></div>
<div class="float-shape triangle t2"></div>
<div class="float-shape triangle t3"></div>
<div class="float-shape triangle t4"></div>