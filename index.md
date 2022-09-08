# Konvertor Markdown na HTML

---
Tento program slouží pro konverzi z textového formátu **markdown** do formátu **html**.

Buhužel knihovna markdown pro python nepodporuje implicitně rozšířenou syntax tohoto formátu.

Položky jako:

- Zvýraznění pozadí textu
- Tabulky
- Smajlíky

## Požadavky na spuštění

- python verze 3.10
- pip
- knihovna markdown
- venv modul pro python (optimální)

### Příprava virtuálního prostředí

    py -m venv .venv/md_app
    cd .venv
    cd md_app
    cd Scripts
    activate.bat

### Instalace markdown

    (md_app)> pip install markdown


---

## Spuštění aplikace

    (md_app)> py app.py

## Interakce s aplikací

Výsledný soubor se uloží pod stejným názvem s koncovkou html

### Soubor s výchozím názvem

    Default path .md file (index.md) Y/N: Y
### Soubor s odlišným názvem

    Default path .md file (index.md) Y/N: N
    Path to .md file: note.md

