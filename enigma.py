from rotor import Rotor


class Enigma:
    def __init__(self, key, rotors):
        self.key = list(key)
        self.rotors = []
        for i in range(0, len(rotors)):
            self.rotors.append(Rotor(self.key[i], rotors[i]))

    def encrypt(self, word):
        cipher = ''
        for i, char in enumerate(word.upper()):
            distance = self.rotors[i % 2].get_distance(char)
            cipher += self.rotors[2].rotate((i + 1) % 2, distance)
        return cipher
