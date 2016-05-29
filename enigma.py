from rotor import Rotor
import sys
import getopt


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

    def decrypt(self, cipher):
        word = ''
        for i, char in enumerate(cipher.upper()):
            distance = self.rotors[2].get_distance(char)
            word += self.rotors[i % 2].rotate((i + 1) % 2, distance)
        return word


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
    try:
        opts, args = getopt.getopt(argv, "hk:p:d", ["help", "key=", "phrase", "decrypt", "r1=", "r2=", "r3="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    key = ''
    phrase = ''
    encrypt = True
    rotors = ['', '', '']
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-k", "--key"):
            key = arg
        elif opt in ("-p", "--phrase"):
            phrase = arg
        elif opt in ("-d", "--decrypt"):
            encrypt = False
        elif opt == "--r1":
            rotors[0] = arg
        elif opt == "--r2":
            rotors[1] = arg
        elif opt == "--r3":
            rotors[2] = arg

    if not key == '' and not phrase == '' and not rotors[0] == ''\
            and not rotors[1] == '' and not rotors[2] == '':
        machine = Enigma(key, rotors)
        if encrypt:
            print(machine.encrypt(phrase))
        else:
            print(machine.decrypt(phrase))
    else:
        print_help()

if __name__ == '__main__':
    main(sys.argv[1:])
