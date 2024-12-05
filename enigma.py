import numpy as np

class EnigmaMachine:
    def __init__(self, plugboard: dict[str, str], rotors: list[dict[str, str]], reflector: dict[str, str]):
        """
        Inicializuje šifrovací stroj Enigma.

        :param plugboard: Slovník definující zapojení plugboardu (propojení písmen).
        :param rotors: Seznam slovníků reprezentujících rotory (mapování vstupních písmen na výstupní).
        :param reflector: Slovník reprezentující reflektor (zpětné mapování písmen).
        """
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = reflector
        self.rotors_rotation = [0] * len(rotors)

    def run_plugboard(self, letter: str, is_reverse: bool = False) -> str:
        """
        Provádí substituci přes plugboard.

        :param letter: Vstupní písmeno, které bude substituováno.
        :param is_reverse: Pokud True, provádí zpětnou substituci.
        :return: Substituované písmeno.
        """
        if not is_reverse:
            return self.plugboard[letter]
        else:
            return list(self.plugboard.keys())[list(self.plugboard.values()).index(letter)]

    def run_rotors(self, letter: str) -> str:
        """
        Provede průchod písmena rotory a reflektorem.

        :param letter: Vstupní písmeno.
        :return: Výstupní písmeno po průchodu rotory a reflektorem.
        """
        for rotor in self.rotors:
            letter = rotor[letter]

        letter = self.reflector[letter]

        for rotor in reversed(self.rotors):
            letter = list(rotor.keys())[list(rotor.values()).index(letter)]
        return letter

    def update_rotors(self) -> None:
        """
        Aktualizuje pozice rotorů simulací jejich rotace.
        Každý rotor se posune o jednu pozici po každém znaku, přičemž vyšší rotory se posouvají
        podle přesahu nižších rotorů.
        """
        self.rotors_rotation[0] += 1
        for i in range(1, len(self.rotors_rotation)):
            if self.rotors_rotation[i-1] % len(self.alphabet) == 0 and self.rotors_rotation[i-1] != 0:
                self.rotors_rotation[i] += 1

    def encode_letter(self, letter: str, is_reverse: bool = False) -> str:
        """
        Zakóduje jedno písmeno prostřednictvím plugboardu, rotorů a reflektoru.

        :param letter: Vstupní písmeno k zakódování.
        :param is_reverse: Pokud True, provádí dekódování (obrácený směr plugboardu).
        """
        letter = self.run_plugboard(letter, is_reverse)
        letter = self.run_rotors(letter)
        letter = self.run_plugboard(letter, is_reverse)
        return letter

    def decode_word(self, word: str) -> str:
        """
        Dekóduje celý text/slovo.

        :param word: Vstupní zašifrovaný text.
        :return: Dekódovaný text.
        """
        decoded_word = ""
        for letter in word:
            if letter in self.alphabet:
                decoded_letter = self.encode_letter(letter, is_reverse=True)
                decoded_word += decoded_letter
            else:
                decoded_word += " "
        return decoded_word

    def run(self) -> None:
        """
        Spustí šifrovací/dešifrovací režim stroje Enigma.
        Uživatel může opakovaně zadávat text k dekódování.
        """
        print("Welcome to the Enigma Machine!")
        print("Napiš slovo k dekódovaní. K ukončení stiskni enter")
        while True:
            word = input("Type word to decode (or type empty to exit): ")
            if word == "":
                print("Ukončuji enigmu...")
                break
            else:
                word = word.upper()
                decoded_word = self.decode_word(word)
                print("Dekódované slovo:", decoded_word)


plugboard = {'A': 'M', 'B': 'C', 'C': 'B', 'D': 'F', 'E': 'Z', 'F': 'D', 'G': 'J', 'H': 'O',
             'I': 'L', 'J': 'G', 'K': 'W', 'L': 'I', 'M': 'A', 'N': 'S', 'O': 'H', 'P': 'U',
             'Q': 'V', 'R': 'X', 'S': 'N', 'T': 'Y', 'U': 'P', 'V': 'Q', 'W': 'K', 'X': 'R',
             'Y': 'T', 'Z': 'E'}
rotors = [{'A': 'A', 'B': 'J', 'C': 'D', 'D': 'K', 'E': 'S', 'F': 'I', 'G': 'R', 'H': 'U',
           'I': 'X', 'J': 'B', 'K': 'L', 'L': 'H', 'M': 'W', 'N': 'T', 'O': 'M', 'P': 'C',
           'Q': 'Q', 'R': 'G', 'S': 'Z', 'T': 'N', 'U': 'P', 'V': 'Y', 'W': 'F', 'X': 'V',
           'Y': 'O', 'Z': 'E'},
          {'A': 'E', 'B': 'S', 'C': 'O', 'D': 'V', 'E': 'P', 'F': 'Z', 'G': 'J', 'H': 'A',
           'I': 'Y', 'J': 'Q', 'K': 'U', 'L': 'I', 'M': 'R', 'N': 'H', 'O': 'X', 'P': 'L',
           'Q': 'N', 'R': 'F', 'S': 'T', 'T': 'G', 'U': 'K', 'V': 'D', 'W': 'C', 'X': 'M',
           'Y': 'W', 'Z': 'B'},
          {'A': 'E', 'B': 'K', 'C': 'M', 'D': 'F', 'E': 'L', 'F': 'G', 'G': 'D', 'H': 'Q',
           'I': 'V', 'J': 'Z', 'K': 'N', 'L': 'T', 'M': 'O', 'N': 'W', 'O': 'Y', 'P': 'H',
           'Q': 'X', 'R': 'U', 'S': 'S', 'T': 'P', 'U': 'A', 'V': 'I', 'W': 'B', 'X': 'R',
           'Y': 'C', 'Z': 'J'}]
reflector = {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D',
             'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I',
             'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J',
             'Y': 'A', 'Z': 'T'}

enigma = EnigmaMachine(plugboard, rotors, reflector)

enigma.run()