import random
from char_handling import Wizard, Thief, Knight
from Monsters import *


# To put it in the Character class.
def displayCharacter(self):
    name_player = "Name : {}\n".format(self.name)
    attributes = "Initiative: {}\nAgility: {}\nSpecial: {}".format(self.initiative,self.agility,self.special)
    attack_endurance = "Attack  : {}\n Endurance: {}".format(self.attack,self.endurance)
    ShowAttributesCharacter = name_player + "\n" + attributes + "\n" + attack_endurance
    return ShowAttributesCharacter


# To put it in the Monster class.

def displayMonster(self):
    name_monster = "Name : {}".format(self.name)
    attributes = "Initiative: {}\nAgility: {}\n".format(self.initiative,self.agility)
    attack_endurance = "Attack  : {}\n Endurance: {}".format(self.attack,self.endurance)
    ShowAttributesMonster = name_monster + "\n" + attributes + "\n" + attack_endurance
    return ShowAttributesMonster


def randomizer(self, procent):
    if random.randint(1, 100) <= procent:
        return True
    else:
        return False


# Define the options that the user can use in battles.
attackOption = ["Attack", "attack"]
# specialOption = ["Special", "special"]
flyOption = ["Fly", "fly"]
show_Attributes = "| {} || {} |".format(attackOption[0], flyOption[0])


# Print the options that the user can use in battles.
def show_Attributes(a, f):
    show_Attributes = "| {} || {} || {} || {} |".format(attackOption[0], a, flyOption[0], f)
    return show_Attributes


# Options in battles.
# a = Attack
# s = Special
# f = fly
def BattleOptions(a, f):
    while True:
        option = input(" What do you want to do?\n" + show_Attributes(a, f))
        for a in attackOption:
            if option == a:
                return "Attack"
        '''
        for s in specialOption:
            if option == s:
                return "Special"
        '''
        for f in flyOption == f:
            if option == f:
                return "Fly"

# Every time a new battle starts
# Show that a battle has started.
# Show monster and character status


def ShowBattle(player, monster):
    print("--------------------")
    print("B  A  T  T  L  E  ")
    print("--------------------")
    print("A battle has started, get ready !!")
    while True:
        print("------------------------")
        print(player.displayCharacter())
        print("------------------------")
        print(monster.displayMonster())
        print("------------------------")
        if player.endurance <= 0:
            return "You have been defeated"

# Shows the actions that can happen in each battle
        action = BattleOptions(player.attack - monster.endurance)(player.attack + player.attack)
        if action == "Attack":
            monster.endurance -= player.attack - monster.endurance
            print("Player attack {} to monster {} ".format(player.name, monster.name, (player.attack - monster.endurance)))
        if action == "Special":
            if player == Wizard:
                Wizard = randomizer (50)
                if randomizer == True:
                    return flyOption
            if player == Knight:
                Knight = randomizer(100)
                if randomizer == True:
                    return player.endurance + player.endurance
            if player == Thief:
                Thief = randomizer()
                if randomizer == True:
                    return player.attack + player.attack - monster.endurance
                monster.endurance -= player.attack + ""
                print("Something {}".format(player.name,monster.name,(player.attack + player.attack)))
            else:
                print("Something")
        if monster.endurance > 0:
            player.endurance -= monster.attack - player.endurance
            print("Monster attack {} to player {} ".format(monster.name,player.name,(monster.attack - player.endurance)))
        else:
            print("The monster has died")
        if action == "Fly":
            return "Fly"
        if monster.endurance <= 0:
            return "YOU WIN THE BATTLE"
        player.endurance >= monster.attack - player.endurance
        input("Press any key to continue")

# Shows the events that happen after each battle, player and monster statuses
        BattleEvent = True
        if BattleEvent == True:
            s = (player, monster)
            if s == "Fly":
                print("You have escaped from the monster{}".format(monster.name))
            if s == "You have been defeated":
                print("You have been defeated by the monster {}".format(monster.name))
            if s == "YOU WIN THE BATTLE":
                print("You have defeated the monster{}".format(monster.name))

# After the battle, print the character's status
        BattleFinishCharacter = True
        if BattleFinishCharacter == True:
            if player.endurance > 0:
                return "You have survived, you can continue ..."
            elif player.endurance <= 0:
                return "You have not survived the battle, your character has died..."

# After the battle, print the monster's status
        BattleFinishMonster = True
        if BattleFinishMonster == True:
            if monster.endurance > 0:
                return BattleOptions
            elif monster.endurance <= 0:
                return "The monster is dead, you can continue"


# In progres :)
    """ BattleOptionFly = True
    if BattleOptionFly == True:
        return"""
