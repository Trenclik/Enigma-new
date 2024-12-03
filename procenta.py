import warnings as w
from inspect import currentframe
class Procenta():
    """třída pro náhodný výběr textu pro dešifrování podle zadaných procent\n
    slice()\n
    vyber()\n
    """
    
    def custom_showwarning(message, category, filename, lineno, file=None, line=None):
        print(f"\033[1;30;43mVAROVÁNÍ: {message}\033[0m")
    w.showwarning = custom_showwarning
    
    def slice(text: str):
        """Rozdělí text na jednotlivá slova v listu. Nevrací mezery.

        Vstup:
            text (string): text k rozdělení

        Výstup:
            list: list se stringy slov oddělených od sebe
        """
        if text == "":
            w.warn(f"Prázdný vstup do funkce {currentframe().f_code.co_name}. Funkce by měla stále fungovat ale výstup bude prázdný.")
        sliced = []
        slovo = ""
        for i in text + " ":
            if i != " ":
                slovo += i
            else:
                sliced.append(slovo)
                slovo = ""
        return sliced
    
    def vyber(procenta: int):
        """Náhodně vybere určité procento slov z listu a vrátí jiný list s vybranými slovy.
        Zapamatuje si dekódovaná slova aby nedošlo k chybám v dešifrování.
        
        Vstup:
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
        #dodělat zbytek logiky
Procenta.slice("")