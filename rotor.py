class Rotor:
    alphabets = {
        '50': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '51': 'ADCBEHFGILJKMPNOQTRSUXVWZY',
        '60': 'ACEDFHGIKJLNMOQPRTSUWVXZYB',
        '61': 'AZXVTRPNDJHFLBYWUSQOMKIGEC',
        '70': 'AZYXWVUTSRQPONMLKJIHGFEDCB',
        '71': 'AEBCDFJGHIKOLMNPTQRSUYVWXZ'
    }

    def __init__(self, key, number):
        self.key = key.upper()
        self.alphabet = Rotor.alphabets[number]
        for i in range(0, len(self.alphabet)):
            if self.alphabet[i] == self.key:
                self.alphabet = self.alphabet[i:] + self.alphabet[:i]

    def rotate(self, clockwise, distance):
        if not clockwise:
            distance = len(self.alphabet) - distance
        return self.alphabet[distance]

    def get_distance(self, to):
        for i in range(0, len(self.alphabet)):
            if self.alphabet[i] == to:
                return i
