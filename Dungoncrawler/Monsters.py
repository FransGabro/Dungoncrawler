import random


class Monster():  # Class Monster and constructor.

    def __init__(self, namn, inititiv, tålighet, attack, smidighet, vanlighet):
        self.namn = namn
        self.klass = namn
        self.inititiv = inititiv
        self.tålighet = tålighet
        self.attack = attack
        self.smidighet = smidighet
        self.vanlighet = vanlighet

    def __repr__(self):
        return 'Namn: {}\nInititiv: {}\nTålighet: {}\nAttack: {}\nSmidighet: {}\nVanlighet: {}'.format(self.name, self.initative, self.endurance, self.attack, self.agility, self.special)


jättespindel = Monster("Jättespindel", 7, 1, 2, 3, 20)
skelett = Monster("Skelett", 4, 2, 3, 3, 15)
orc = Monster("Orc", 6, 3, 4, 4, 10)
troll = Monster("Troll", 2, 4, 7, 2, 5)


# myMonsters = [jättespindel, skelett, orc, troll]
# randomMonster = random.choices(Monster, k=1)
# print(randomMonster)
