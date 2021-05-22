from random import randint
from char_handling import (Wizard, Thief, Knight)
from Monsters import Monster
from char_handling import Hero, load

# exempelvis jättespindel mot trollkarl
jättespindel = Monster("Jättespindel", 7, 1, 2, 3, 20)
orc = Monster("Orc", 6, 3, 4, 4, 10)
trollkarlen_pelle = Wizard('Pelle')
tjuven_anders = Thief('Anders')


class Strid():
    turn_count = 0
    hero_initiative = load_initiative()

    def __init__(self, monster):
        self.hero = hero_initiative
        self.monster = monster
        self.turordning_strid(self.hero.initiativ, self.monster.initiativ)

    def turordning_strid(hero_initiative, monster_initiative):
        '''Returnerar poängen efter dice toss'''
        hero_initiative_count = 0
        for i in range(hero_initiative):
            hero_die = randint(1, 6)
            hero_initiative_count += hero_die

        monster_initiative_count = 0
        for i in range(monster_initiative):
            monster_die = randint(1, 6)
            monster_initiative_count += monster_die

        turn_result = (hero_initiative - monster_initiative)
        return turn_result

    def hero_turn(attack, klass, smidighet):
        attack_points = 0
        for i in range(attack):
            die = randint(1, 6)
            attack_points += die
        if klass == 'tjuv':
            critical_hit = 25
            critical_hit_chance = randint(1, 100)
            if critical_hit_chance <= critical_hit:
                attack_points += attack_points
                print('Critical hit!')
            else:
                pass
        else:
            pass

        agility_points = 0
        for i in range(smidighet):
            die = randint(1, 6)
            agility_points += die

        result = (attack_points - agility_points)
        return result

    def monster_turn(attack, klass, smidighet):
        attack_points = 0
        for i in range(attack):
            die = randint(1, 6)
            attack_points += die

        agility_points = 0
        for i in range(smidighet):
            die = randint(1, 6)
            agility_points += die

        result = (attack_points - agility_points)
        return result

    def try_to_flee(smidighet, klass):
        if klass == 'trollkarl':
            smidighet = 80
        else:
            smidighet = (smidighet * 10)

        attempt = randint(1, 100)
        if attempt <= smidighet:
            result = True
        else:
            result = False
        return result

    def battle_order(turn_result):
        if turn_result >= 0:
            while True:
                hero_turn()
                monster_turn()
                if monster.endurance == 0:
                    break
                elif self.hero.endurance == 0:
                    break
        elif turn_result < 0:
            while True:
                monster_turn()
                hero_turn()
                if monster.endurance == 0:
                    break
                elif self.hero.endurance == 0:
                    break

    def load_initiative():
        hero = load('CurrentHero')
        attr_list = hero['Character']
        hero_initiative = attr_list[0]
        initiative = hero_initiative['initiative']
        return initiative
