from enigma import Enigma

machine = Enigma('SEC', ['71', '60', '51'])
print(machine.encrypt('ICANDOTHAT'))  # has to be RBLSPTYYLP
