from die import Strid
from Monsters import orc
from char_handling import load


def load_initiative():
    hero = load('CurrentHero')
    attr_list = hero['Character']
    hero_initiative = attr_list[0]
    initiative = hero_initiative['initiative']
    return initiative


print(load_initiative())