# Elections Scraper

Třetí projekt pro Engeto Online Python Akademii.

---

## Autor
- **Jméno:** Lukáš Svoboda
- **Email:** lukas.svobo1@seznam.cz

---

## Popis projektu

Tento skript slouží ke scrapování výsledků voleb z roku 2017 přímo ze stránek [volby.cz](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).  
Po spuštění stáhne výsledky pro všechny obce v daném územním celku a uloží je do souboru ve formátu `.csv`.

---

## Instalace

1. Vytvoř si nové virtuální prostředí:

    ```bash
    python -m venv .venv
    ```

2. Aktivuj virtuální prostředí:
   - **Windows (CMD):**
     ```bash
     .venv\Scripts\activate.bat
     ```
   - **Windows (PowerShell):**
     ```bash
     .\.venv\Scripts\Activate.ps1
     ```
   - **Mac/Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. Nainstaluj potřebné knihovny pomocí příkazu:

    ```bash
    pip install -r requirements.txt
    ```

---

## Jak skript spustit

Skript potřebuje **2 argumenty**:
- první argument: odkaz na územní celek na stránkách volby.cz
- druhý argument: název výstupního `.csv` souboru

### Ukázka spuštění:

```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "vysledky_prostejov.csv"
