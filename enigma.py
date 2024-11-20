from rotor import Rotor
import sys


class Enigma:
    def __init__(self, key, rotors):
        # Inicializace třídy Enigma. Bere dva parametry:
        # 1. key - seznam znaků, který slouží jako počáteční klíč pro rotory.
        # 2. rotors - seznam objektů (pravděpodobně typu Rotor).
        self.key = list(key)  # Klíč je převeden na seznam znaků.
        self.rotors = []  # Inicializace seznamu rotorů.

        # Pro každý rotor ve vstupu vytvoří instanci Rotor s odpovídajícím klíčem.
        for i in range(0, len(rotors)):
            self.rotors.append(Rotor(self.key[i], rotors[i]))

    def encrypt(self, word):
        # Metoda pro šifrování vstupního textu `word`.
        cipher = ''  # Výsledný šifrovaný text.
        
        for i, char in enumerate(word.upper()):  # Pro každý znak ve vstupním slově.
            # Získání vzdálenosti aktuálního znaku od daného rotoru (zřejmě posun).
            distance = self.rotors[i % 2].get_distance(char)
            
            # Rotace třetího rotoru na základě vzdálenosti a indexu (i+1) % 2.
            # Výsledek přidá do zašifrovaného textu.
            cipher += self.rotors[2].rotate((i + 1) % 2, distance)
        
        return cipher  # Vrací šifrovaný text.

    def decrypt(self, cipher):
        # Metoda pro dešifrování šifrovaného textu `cipher`.
        word = ''  # Výsledný dešifrovaný text.
        
        for i, char in enumerate(cipher.upper()):  # Pro každý znak v šifrovaném textu.
            # Získání vzdálenosti aktuálního znaku na třetím rotoru.
            distance = self.rotors[2].get_distance(char)
            
            # Rotace odpovídajícího rotoru a přidání výsledku do dešifrovaného textu.
            word += self.rotors[i % 2].rotate((i + 1) % 2, distance)
        
        return word  # Vrací dešifrovaný text.



def print_help():
    print("\ncommand line arguments:\n" +
          "-h/--help: all possible options\n" +
          "-k/--key KEY: rotor starting key\n" +
          "-p/--phrase Phrase: phrase to encrypt/decrypt\n" +
          "-d/--decrypt: enables decrypt default is encrypt\n" +
          "--r1 ROTOR: sets rotor 1\n" +
          "--r2 ROTOR: sets rotor 2\n" +
          "--r3 ROTOR: sets rotor 3\n" +
          "possible rotors are 50, 51, 60, 61, 70 and 71\n")


def main(argv):
    volba = input("args: ")
    phrase = input("phrase: ")
    if volba in ("-d", "--decrypt"):
        encrypt = False

    if not phrase == '':
        machine = Enigma(key, rotors)
        if encrypt:
            print(machine.encrypt(phrase))
        else:
            print(machine.decrypt(phrase))
    else:
        print_help()

if __name__ == '__main__':
    main(sys.argv[1:])
