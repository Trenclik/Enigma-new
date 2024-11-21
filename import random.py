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


plugboard = {}
free_indexes = np.linspace(0, 25, num=26, dtype='int')
final_combination = np.array(list(alphabet))
for _ in range(13):
    index1 = random.choice(free_indexes)
    free_indexes = np.delete(free_indexes, np.where(free_indexes == index1))
    index2 = random.choice(free_indexes)
    free_indexes = np.delete(free_indexes, np.where(free_indexes == index2))
    final_combination[index1] = alphabet[index2]
    final_combination[index2] = alphabet[index1]
for letter, index in zip(alphabet, range(len(alphabet))):
    plugboard[letter] = final_combination[index]
print(plugboard)
print("\n\n\n")

rotors = []
for _ in range(3):
    random_rotor_combination = random.choice(possible_rotor_combinations)
    rotor = {alphabet[i]: random_rotor_combination[i] for i in range(len(alphabet))}
    rotors.append(rotor)
print(rotors)
print("\n\n\n")

random_reflector_combination = random.choice(possible_reflector_combinations)
reflector = {alphabet[i]: random_reflector_combination[i] for i in range(len(random_reflector_combination))}
print(reflector)
print("\n\n\n")
