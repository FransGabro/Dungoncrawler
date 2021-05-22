import pickle
import json


class Hero():
    def __init__(self, name, klass, initiative, endurance, attack, agility, special, coins): #position ska oxå in här
        self.name = name
        self.klass = klass
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.special = special
        self.coins = coins
        # self.position = self.player


# skapar jsonfil där karaktärer med attributer sparas i dicts

def create_json(filename):
    try:
        load('CurrentHero.json')
    except:
        char_dict = {"Character": []}
        with open(filename + ".json", "w") as s:
            json.dump(char_dict, s, indent=4)

# def highscore_json(filename):
#   score_dict = {"Highscore": []}
#   with open(filename+ ".json", "w") as s:
#       json.dump(score_dict, s, indent=4)


# sparar karaktärer plus attributer i jsonfilen
def save(filename, hero):
    char_dict = hero.__dict__
    with open(filename + ".json", "r+") as s:
        loaded_file = json.load(s)
        loaded_file["Character"].append(char_dict)

    with open(filename + ".json", "w") as s:
        json.dump(loaded_file, s, indent=4)

def highscore():
    # laddar gamla highscore om det finns
    try:
        with open('score.json', 'r') as hs:
            coins = json.load(hs)
    except:
        coins = 0

    with open('score.json', 'w') as hs:
        json.dump(coins, hs)
      
    print(f'Highscore: {coins}')


#laddar upp sparade jsonfiler
def load(filename):
        with open(filename + ".json", "r+") as s:
            loaded_file = json.load(s)
        return loaded_file

class Wizard(Hero):
    def __init__(self, name):
        super().__init__(name, 'trollkarl', 6, 4, 9, 5, "Flash", 0) #position ska oxå in här


class Knight(Hero):
    def __init__(self, name):
        super().__init__(name, 'riddare', 5, 9, 6, 4, "Block first attack", 0)#position ska oxå in här


class Thief(Hero):
    def __init__(self, name):
        super().__init__(name, 'tjuv', 7, 5, 5, 7, "Critical hit", 0)#position ska oxå in här


#testar olika prints

#position = pos
#name1 = input("Namn: ")
#name2 = input("Namn: ")
#create_json("SavedHero")
#highscore_json("Highscore")
#save("SavedHero", (Knight(name1)))
#save("SavedHero", (Thief(name2)))
#load("SavedHero")
#highscore()