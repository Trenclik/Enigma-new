import numpy as np
import os

# Alphabet used by the Enigma machine
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plugboard = {'A': np.str_('M'), 'B': np.str_('C'), 'C': np.str_('B'), 'D': np.str_('F'), 'E': np.str_('Z'), 'F': np.str_('D'), 'G': np.str_('J'), 'H': np.str_('O'), 'I': np.str_('L'), 'J': np.str_('G'), 'K': np.str_('W'), 'L': np.str_('I'), 'M': np.str_('A'), 'N': np.str_('S'), 'O': np.str_('H'), 'P': np.str_('U'), 'Q': np.str_('V'), 'R': np.str_('X'), 'S': np.str_('N'), 'T': np.str_('Y'), 'U': np.str_('P'), 'V': np.str_('Q'), 'W': np.str_('K'), 'X': np.str_('R'), 'Y': np.str_('T'), 'Z': np.str_('E')}
rotors = [{'A': 'A', 'B': 'J', 'C': 'D', 'D': 'K', 'E': 'S', 'F': 'I', 'G': 'R', 'H': 'U', 'I': 'X', 'J': 'B', 'K': 'L', 'L': 'H', 'M': 'W', 'N': 'T', 'O': 'M', 'P': 'C', 'Q': 'Q', 'R': 'G', 'S': 'Z', 'T': 'N', 'U': 'P', 'V': 'Y', 'W': 'F', 'X': 'V', 'Y': 'O', 'Z': 'E'},
          {'A': 'E', 'B': 'S', 'C': 'O', 'D': 'V', 'E': 'P', 'F': 'Z', 'G': 'J', 'H': 'A', 'I': 'Y', 'J': 'Q', 'K': 'U', 'L': 'I', 'M': 'R', 'N': 'H', 'O': 'X', 'P': 'L', 'Q': 'N', 'R': 'F', 'S': 'T', 'T': 'G', 'U': 'K', 'V': 'D', 'W': 'C', 'X': 'M', 'Y': 'W', 'Z': 'B'},
          {'A': 'E', 'B': 'K', 'C': 'M', 'D': 'F', 'E': 'L', 'F': 'G', 'G': 'D', 'H': 'Q', 'I': 'V', 'J': 'Z', 'K': 'N', 'L': 'T', 'M': 'O', 'N': 'W', 'O': 'Y', 'P': 'H', 'Q': 'X', 'R': 'U', 'S': 'S', 'T': 'P', 'U': 'A', 'V': 'I', 'W': 'B', 'X': 'R', 'Y': 'C', 'Z': 'J'}]
reflector = {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D', 'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I', 'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A', 'Z': 'T'}

def run_plugboard(letter: str, letter_path: str, plugboard: dict, is_reverse=False):
    """Provede průchod litery skrze plugboard Enigmy.

    Vstup:
        letter (str): Litera, již jest třeba zakódovati či dekódovati.
        letter_path (str): Sled proměn litery během průchodu.
        plugboard (dict): Tabulka spojení spojovací desky.
        is_reverse (bool): Pokud-li je pravda, provede dekódování.

    Výstup:
        tuple: Nová toť litera a cesta její proměny.
    """
    if not is_reverse:
        new_letter = plugboard[letter]
        letter_path = letter_path + " -> " + new_letter
    else:
        new_letter = list(plugboard.keys())[list(plugboard.values()).index(letter)]
        letter_path = letter_path + " -> " + new_letter
    return new_letter, letter_path

def run_rotors(letter: str, rotors: list, reflector: dict):
    """Provede průchod litery skrze rotory a reflektor stroje Enigma.

    Vstup:
        letter (str): Litera vstupující do rotorů.
        rotors (list): Seznam rotorů Enigmy.
        reflector (dict): Reflektor odrážející signál zpět skrze rotory.

    Výstup:
        str: Litera po průchodu rotory a reflektorem.
    """
    new_letter = letter
    for rotor in rotors:
        new_letter = rotor[new_letter]
    new_letter = reflector[new_letter]
    for rotor in reversed(rotors):
        new_letter = list(rotor.keys())[list(rotor.values()).index(new_letter)]
    return new_letter

def update_rotors(rotors, rotors_rotation):
    """Posune rotory po každém stisku klávesy.

    Vstup:
        rotors (list): Seznam rotorů Enigmy.
        rotors_rotation (list): Počet rotací jednotlivých rotorů.

    Výstup:
        list: Rotory s aktualizovanými pozicemi.
    """
    rotors_rotation[0] += 1
    for i in range(1, len(rotors_rotation)):
        if rotors_rotation[i-1] % len(alphabet) == 0 and rotors_rotation[i-1] != 0:
            rotors_rotation[i] += 1
    return rotors

def encode_letter(letter: str, plugboard: dict, rotors: list, reflector: dict, is_reverse=False):
    """
    Zakóduje či dekóduje literu pomocí mechanismu Enigmy.

    Vstup:
        letter (str): Litera k zakódování.
        plugboard (dict): Tabulka spojení spojovací desky.
        rotors (list): Seznam rotorů.
        reflector (dict): Reflektor.
        is_reverse (bool): Pravda-li, provádí dekódování.

    Výstup:
        str: Zakódovaná či dekódovaná litera.
    """
    path = ""
    coded_letter, path = run_plugboard(letter, path, plugboard, is_reverse)
    coded_letter = run_rotors(coded_letter, rotors, reflector)
    coded_letter, path = run_plugboard(coded_letter, path, plugboard, is_reverse)
    return coded_letter

def decode_word(word: str, plugboard: dict, rotors: list, reflector: dict):
    """Dekóduje slovo složené z liter.

    Vstup:
        word (str): Slovo určené k dekódování.
        plugboard (dict): Tabulka spojení plugboard.
        rotors (list): Seznam rotorů Enigmy.
        reflector (dict): Reflektor.

    Výstup:
        str: Dekódované slovo a potažmo text.
    """
    decoded_word = ""
    for letter in word:
        if letter in alphabet:
            decoded_letter = encode_letter(letter, plugboard, rotors, reflector, is_reverse=True)
            decoded_word += decoded_letter
        else:
            decoded_word += " "
    return decoded_word

if __name__ == '__main__':
    rotors_rotation = [0] * 3
    for x in os.listdir():
        if x.endswith(".txt"):
            print(x)
    text_file_name = input("\nZadejte název souboru k dekódování (i s příponou): ")
    tfn = text_file_name.replace(".txt", "")
    _word = open(text_file_name, "r")
    word = _word.read()
    if word == "":
        print("Žádný text")
    else:
        word = word.upper()
        decoded_word = decode_word(word, plugboard, rotors, reflector)
        with open(tfn + '_decoded-text.txt', "a") as file:
            file.write(f"{decoded_word}\n")

