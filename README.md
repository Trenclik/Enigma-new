# Dokumentace **SifrovaciStrojEnigma**

Tato knihovna implementuje simulaci šifrovacího stroje Enigma a poskytuje funkcionalitu pro šifrování, dešifrování a zpracování textových souborů.

---

## Obsah:
1. [Třída `SifrovaciStrojEnigma`](#třída-sifrovacistrojenigma)
   - [Inicializace](#inicializace)
   - [Metody](#metody)
2. [Příklad použití](#příklad-použití)

---

## Třída `SifrovaciStrojEnigma`

Třída simuluje šifrovací stroj Enigma, včetně propojovací desky, rotorů a reflektoru.

### Inicializace

```python
SifrovaciStrojEnigma(propojovaci_deska=None, rotory=None, reflektor=None)
```

- **Parametry:**
  - `propojovaci_deska` *(slovník)*: Mapování znaků na propojovací desce (výchozí hodnota je předdefinované propojení).
  - `rotory` *(seznam slovníků)*: Seznam mapování jednotlivých rotorů (výchozí je jeden předdefinovaný rotor).
  - `reflektor` *(slovník)*: Mapování reflektoru (výchozí je předdefinované mapování).

---

### Metody

#### 1. **`spustit_propojovaci_desku`**
```python
spustit_propojovaci_desku(znak: str, obracene: bool = False) -> str
```
Zpracuje zadaný znak přes propojovací desku.

- **Parametry:**
  - `znak` *(str)*: Znak k zpracování.
  - `obracene` *(bool)*: Určuje, zda má být zpracování obrácené (výchozí `False`).

- **Návratová hodnota:** Zpracovaný znak.

---

#### 2. **`spustit_rotory`**
```python
spustit_rotory(znak: str) -> str
```
Zpracuje znak postupně přes všechny rotory a reflektor.

- **Parametry:**
  - `znak` *(str)*: Znak k zpracování.

- **Návratová hodnota:** Zpracovaný znak.

---

#### 3. **`zasifrovat_znak`**
```python
zasifrovat_znak(znak: str, obracene: bool = False) -> str
```
Zašifruje nebo dešifruje jeden znak.

- **Parametry:**
  - `znak` *(str)*: Znak k šifrování nebo dešifrování.
  - `obracene` *(bool)*: Určuje, zda se má znak dešifrovat (výchozí `False`).

- **Návratová hodnota:** Zašifrovaný nebo dešifrovaný znak.

---

#### 4. **`desifrovat_slovo`**
```python
desifrovat_slovo(slovo: str) -> str
```
Dešifruje jedno celé slovo.

- **Parametry:**
  - `slovo` *(str)*: Slovo k dešifrování.

- **Návratová hodnota:** Dešifrované slovo (všechna písmena jsou malá).

---

#### 5. **`zpracovat_textovy_soubor`**
```python
zpracovat_textovy_soubor(cesta_souboru: str, procento: int, vystupni_cesta: str) -> None
```
Zpracuje textový soubor, dešifruje zadané procento velkých písmen a uloží výstup do souboru.

- **Parametry:**
  - `cesta_souboru` *(str)*: Cesta k vstupnímu textovému souboru.
  - `procento` *(int)*: Procento velkých slov, která mají být dešifrována.
  - `vystupni_cesta` *(str)*: Cesta k výstupnímu souboru.

- **Výjimky:**
  - `FileNotFoundError`: Pokud soubor na zadané cestě neexistuje.

- **Návratová hodnota:** Žádná. Výsledek je uložen do souboru.

---

## Příklad použití

```python
from sifrovaci_stroj import SifrovaciStrojEnigma

# Inicializace stroje Enigma
enigma = SifrovaciStrojEnigma()

# Dešifrování jednotlivého slova
slovo = "HELLO"
desifrovane = enigma.desifrovat_slovo(slovo)
print(f"Dešifrované slovo: {desifrovane}")

# Zpracování textového souboru
cesta_vstup = "vstupni_text.txt"
cesta_vystup = "vystupni_text.txt"
enigma.zpracovat_textovy_soubor(cesta_vstup, procento=50, vystupni_cesta=cesta_vystup)