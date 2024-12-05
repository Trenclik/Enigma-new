import warnings as w
from random import choice
import os
class Procenta():
    
    """třída pro náhodný výběr textu pro dešifrování podle zadaných procent\n
    slice()\n
    vyber()\n
    """
    
    def custom_showwarning(message, category, filename, lineno, file=None, line=None):
        print(f"\033[1;30;43mVAROVÁNÍ: {message}\033[0m")
    w.showwarning = custom_showwarning
    def stringify():
        for i in os.listdir("texty"):
            procenta
    def slice(text: str):
        """Rozdělí text na jednotlivá slova v listu. Nevrací mezery.

        Vstup:
            text (string): text k rozdělení

        Výstup:
            list: list se stringy slov oddělených od sebe
        """
        if not isinstance(text, str):
            raise TypeError("Vstup musí být string!")
        if text == "":
            w.warn("Prázdný vstup do funkce slice Funkce by měla stále fungovat ale výstup bude prázdný.")
        
        sliced = []
        slovo = ""

        for i in text + " ":
            if i == " ":
                sliced.append(slovo)
                slovo = ""
            else:
                slovo += i
        return sliced
    
    def vyber(sliced: list ,procenta: int):
        """Náhodně vybere určité procento slov z listu a vrátí jiný list s vybranými slovy.
        Zapamatuje si dekódovaná slova aby nedošlo k chybám v dešifrování.
        
        Vstup:
            slova (list): slova rozdělená do listu
            procenta (int): procento slov která budou zakódována
        Výstup:
            slova (list): náhodný výběr slov
        """
        
        if not isinstance(procenta, int):
            raise TypeError("Vstup musí být celé číslo!")
        if procenta == 0:
            w.warn("Vstupní hodnota nastavena na nulu. Funkce by měla stále fungovat ale výstup bude prázdný. Doporučuji nastavit alespoň na 10%")
        if procenta <0:
            w.warn("Nelze vybrat číslo menší než 0! Měním na 0%.")
            procenta = 0
        if procenta >100:
            w.warn("Nelze vybrat číslo větší než 100! Měním na 100%")
            procenta = 100
        
        vratka = []
        pica = []
        for i in range(int((len(sliced)/100)*procenta)):
            while True:
                ind = choice(sliced)
                if ind in pica:
                    pass
                else:
                    pica.append(ind)
                    break
            vratka.append(ind)
        return vratka
print("kokotfdf"-"fdf")