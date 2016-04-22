from enigma import Enigma

machine = Enigma('SEC', ['71', '60', '51'])
print(machine.encrypt('ICANDOTHAT'))  # has to be RBLSPTYYLP

machine2 = Enigma('AIN', ['61', '50', '70'])
print(machine2.decrypt('ZJWNFNFNJ'))  # YESIDIDIT ???



