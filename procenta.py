import warnings as w
from random import choice
import os

class Procenta:
    """Třída pro náhodný výběr textu pro dešifrování podle zadaných procent\n
    slice()\n
    vyber()\n
    nacti_text()\n
    nahrad()\n
    """
    
    def __init__(self):
        self._zapamatovana_slova = {}

    def custom_showwarning(message, category, filename, lineno, file=None, line=None):
        print(f"\033[1;30;43mVAROVÁNÍ: {message}\033[0m")
    w.showwarning = custom_showwarning

    def slice(self, text: str):
        """Rozdělí text na jednotlivá slova v listu. Nevrací mezery.

        Vstup:
            text (string): text k rozdělení

        Výstup:
            list: list se stringy slov oddělených od sebe
        """
        if not isinstance(text, str):
            raise TypeError("Vstup musí být string!")
        if text == "":
            w.warn("Prázdný vstup do funkce slice. Funkce by měla stále fungovat, ale výstup bude prázdný.")
        
        sliced = []
        slovo = ""

        for i in text + " ":
            if i == " ":
                sliced.append(slovo)
                slovo = ""
            else:
                slovo += i
        return sliced
    
    def vyber(self, sliced: list, procenta: int):
        """Náhodně vybere určité procento slov z listu a vrátí jiný list s vybranými slovy.
        Zapamatuje si dekódovaná slova, aby nedošlo k chybám v dešifrování.
        
        Vstup:
            sliced (list): slova rozdělená do listu
            procenta (int): procento slov, která budou zakódována

        Výstup:
            list: náhodný výběr slov
        """
        if not isinstance(procenta, int):
            raise TypeError("Vstup musí být celé číslo!")
        if procenta == 0:
            w.warn("Vstupní hodnota nastavena na nulu. Funkce by měla stále fungovat, ale výstup bude prázdný. Doporučuji nastavit alespoň na 10%")
        if procenta < 0:
            w.warn("Nelze vybrat číslo menší než 0! Měním na 0%.")
            procenta = 0
        if procenta > 100:
            w.warn("Nelze vybrat číslo větší než 100! Měním na 100%.")
            procenta = 100

        vratka = []
        pica = []
        for i in range(int((len(sliced) / 100) * procenta)):
            while True:
                ind = choice(range(len(sliced)))
                if ind in pica:
                    pass
                else:
                    pica.append(ind)
                    break
            vratka.append(sliced[ind])
            self._zapamatovana_slova[ind] = sliced[ind]  # Zapamatuj slovo s jeho indexem
        return vratka

    def nacti_text(self, cesta: str):
        """Načte text ze souboru.

        Vstup:
            cesta (str): cesta k souboru

        Výstup:
            str: obsah souboru jako text
        """
        if not os.path.isfile(cesta):
            raise FileNotFoundError(f"Soubor '{cesta}' neexistuje!")
        
        with open(cesta, "r", encoding="utf-8") as file:
            return file.read()
    
    def nahrad(self, sliced: list):
        """Nahradí zapamatovaná slova na jejich původní pozice v seznamu.

        Vstup:
            sliced (list): původní list se slovy

        Výstup:
            list: upravený list se zapamatovanými slovy na správných pozicích
        """
        for index, slovo in self._zapamatovana_slova.items():
            sliced[index] = slovo
        return sliced