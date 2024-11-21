import random
import numpy as np

# Alphabet used by the Enigma machine
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Define possible rotor combinations and reflectors
possible_rotor_combinations = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJD",  # Rotor I
    "AJDKSIRUXBLHWTMCQGZNPYFVOECA",  # Rotor II
    "BDFHJLCPRTXVZNYEIWGAKMUSQO",  # Rotor III
    "ESOVPZJAYQUIRHXLNFTGKDCMWB",  # Rotor IV
    "VZBRGITYUPSDNHLXAWMJQOFECK",  # Rotor V
]

possible_reflector_combinations = [
    "YRUHQSLDPXNGOKMIEBFZCWVJAT",  # Reflector B
    "FVPJIAOYEDRZXWGCTKUQSBNMHL",  # Reflector C
]

def generate_random_plugboard_combination(nr_pairs=13):
    plugboard = {}
    free_indexes = np.linspace(0, 25, num=26, dtype='int')
    final_combination = np.array(list(alphabet))

    for _ in range(nr_pairs):
        index1 = random.choice(free_indexes)
        free_indexes = np.delete(free_indexes, np.where(free_indexes == index1))

        index2 = random.choice(free_indexes)
        free_indexes = np.delete(free_indexes, np.where(free_indexes == index2))

        final_combination[index1] = alphabet[index2]
        final_combination[index2] = alphabet[index1]

    for letter, index in zip(alphabet, range(len(alphabet))):
        plugboard[letter] = final_combination[index]
        
    return plugboard

def run_plugboard(letter, letter_path, plugboard, is_reverse=False):
    if not is_reverse:
        new_letter = plugboard[letter]
        letter_path = letter_path + " -> " + new_letter
    else:
        new_letter = list(plugboard.keys())[list(plugboard.values()).index(letter)]
        letter_path = letter_path + " -> " + new_letter

    return new_letter, letter_path

def create_rotors(nr_rotors):
    rotors = []
    for _ in range(nr_rotors):
        random_rotor_combination = random.choice(possible_rotor_combinations)
        rotor = {alphabet[i]: random_rotor_combination[i] for i in range(len(alphabet))}
        rotors.append(rotor)
    return rotors

def create_reflector():
    random_reflector_combination = random.choice(possible_reflector_combinations)
    reflector = {alphabet[i]: random_reflector_combination[i] for i in range(len(random_reflector_combination))}
    return reflector

def create_random_enigma_setup(nr_rotors):
    plugboard = generate_random_plugboard_combination()
    rotors = create_rotors(nr_rotors)
    reflector = create_reflector()
    return plugboard, rotors, reflector

def run_rotors(letter, rotors, reflector):
    new_letter = letter
    for rotor in rotors:
        new_letter = rotor[new_letter]
    new_letter = reflector[new_letter]
    for rotor in reversed(rotors):
        new_letter = list(rotor.keys())[list(rotor.values()).index(new_letter)]
    return new_letter

def update_rotors(rotors, rotors_rotation):
    rotors_rotation[0] += 1
    for i in range(1, len(rotors_rotation)):
        if rotors_rotation[i-1] % len(alphabet) == 0 and rotors_rotation[i-1] != 0:
            rotors_rotation[i] += 1
    return rotors

def encode_letter(letter, plugboard, rotors, reflector, is_reverse=False):
    path = ""
    coded_letter, path = run_plugboard(letter, path, plugboard, is_reverse)
    coded_letter = run_rotors(coded_letter, rotors, reflector)
    coded_letter, path = run_plugboard(coded_letter, path, plugboard, is_reverse)
    return coded_letter

def decode_word(word, plugboard, rotors, reflector):
    decoded_word = ""
    for letter in word:
        if letter in alphabet:  # Only decode valid letters
            decoded_letter = encode_letter(letter, plugboard, rotors, reflector, is_reverse=True)
            decoded_word += decoded_letter
    return decoded_word

if __name__ == '__main__':
    nr_rotors = 3
    rotors_rotation = [0] * nr_rotors

    plugboard, rotors, reflector = create_random_enigma_setup(nr_rotors)



    while True:
        word = input("Type word to decode (or type empty to exit):\n")
        if word == "":
            break
        else:
            word = word.upper()
            decoded_word = decode_word(word, plugboard, rotors, reflector)
            print("Decoded word: ", decoded_word)

