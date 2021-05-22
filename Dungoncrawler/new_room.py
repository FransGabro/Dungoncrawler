from Monsters import Monster
from treasures import (Lösa_slantar, Pengapung, Guldsmycken, Ädelsten, Liten_skattkista)
from utils import randomizer
from char_handling import load
# from die import Strid
# from Battle import *


class Room:
    '''Creates a room'''
    def __init__(self):
        # self.coordinates = int
        self.monsters = []
        self.treasures = []
        # self.visited = True
        self.fill_room()
        self.display_monsters()
        self.display_treasures()
        '''
        while self.number_of_monsters >= 1:
            for monster in self.monsters:
                Strid(monster)
        if self.number_of_treasures >= 1:
            self.pick_up_treasures()
        # self.defeated_room = False
        '''

    def fill_room(self):
        '''Adds random monsters and treasures to the room'''

        # initialize monsters
        '''
        jättespindel = Jättespindel()
        skelett = Skelett()
        orc = Orc()
        troll = Troll()
        '''
        jättespindel = Monster("Jättespindel", 7, 1, 2, 3, 20)
        skelett = Monster("Skelett", 4, 2, 3, 3, 15)
        orc = Monster("Orc", 6, 3, 4, 4, 10)
        troll = Monster("Troll", 2, 4, 7, 2, 5)

        # initialize treasures
        lösa_slantar = Lösa_slantar()
        pengapung = Pengapung()
        guldsmycken = Guldsmycken()
        ädelsten = Ädelsten()
        liten_skattkista = Liten_skattkista()

        # dictionary of monsters and their rarity
        monsters = {jättespindel: jättespindel.vanlighet, skelett: skelett.vanlighet,
                    orc: orc.vanlighet, troll: troll.vanlighet}

        # dictionary of treasures and their rarity
        treasures = {lösa_slantar: lösa_slantar.vanlighet, pengapung: pengapung.vanlighet,
                     guldsmycken: guldsmycken.vanlighet, ädelsten: ädelsten.vanlighet,
                     liten_skattkista: liten_skattkista.vanlighet}

        # randomize monsters and add to self.monsters
        for monster in monsters.keys():
            # print(monster)
            if randomizer(monsters[monster]):
                self.monsters.append(monster)

        # ramdomize treasures and add to self.treasures
        for treasure in treasures.keys():
            if randomizer(treasures[treasure]):
                self.treasures.append(treasure)

    def number_of_monsters(self):
        '''Returns a list of all monsters in the room'''
        return len(self.monsters)

    def number_of_treasures(self):
        '''Returns a list of all treasures in the room'''
        return len(self.treasures)

    def display_monsters(self):
        '''Displays all monsters in the room'''
        if len(self.monsters) > 0:
            print('\nDet finns monster i rummet!')
            for monster in self.monsters:
                print(f'!!!{monster.namn}!!!')

    def display_treasures(self):
        '''Displays all treasures in the room'''
        if len(self.treasures) > 0:
            print('\nDet finns skatter att hämta!')
            for treasure in self.treasures:
                print(f'>>>{treasure.namn}<<<')
                print( u"\u27E1", u"\u27E1", u"\u27E1", u"\u27E1", u"\u27E1", u"\u27E1", u"\u27E1", u"\u27E1", u"\u27E1")
                print(u"\U0001F4B0", u"\U0001F4B0", u"\U0001F4B0", u"\U0001F4B0", u"\U0001F4B0", u"\U0001F4B0")

    def remove_defeated_monster(self, monster):
        '''Removes a defeated monster from room (use after a defeat)'''
        self.monsters.remove(monster)

    def remove_treasures_from_room(self):
        '''Removes all treasures from room (use after they have been collected)'''
        self.treasures.clear()

    def pick_up_treasures(self):
        self.treasures.append(Lösa_slantar())

        coins = load("SavedHero")
        coin_list = coins['Character']
        coin_dict = coin_list[0]
        coins = coin_dict['coins']
        for treasure in self.treasures:
            coins += treasure.poäng
        return coins
