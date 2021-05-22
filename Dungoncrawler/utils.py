import random


def randomizer(procent):
    if random.randint(1, 100) <= procent:
        return True
    else:
        return False


def prompt_exit():
    while True:
        command = input('Du har hittat utgången!\n Välj: [1. Lämna kartan ] [2. Stanna kvar]\n> ')
        if command == '1':
            print('Du klarade dig ut med livet i behåll!')
            break
        elif command == '2':
            print('Fortsätt utforska kartan.')
            break
        else:
            print('Vänligen mata in en av siffrorn.\n')
