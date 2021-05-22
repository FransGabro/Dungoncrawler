import json
import os
from char_handling import Hero, Knight, Thief, Wizard, save, load, create_json
from Map import Map, game


def clear_screen():

    os.system('clear')


def dificulty():

    print("  {∥V¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤V∥}")
    print("  {{================================}}")
    print("<<{{{     {  Svårighetsgrad }     }}}>>")
    print("  {{================================}}")
    print("  {∥V¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤V∥}")

    print("\n {< Liten >}   {< Mellan >}  {< Stor >} \n")


def main_menu():
    def print_choices():

        print(" ==-==============--=============-====================--===========--==")
        print("∥-=======-==============-=================-================-===========-∥")
        print("∥                              ____________                             ∥")
        print("∥______________________________∥  WIZZARDS ∥____________________________∥")
        print("∥-¤¤¤¤¤¤-¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤-------∥           ∥-------¤¤¤¤¤¤¤¤¤¤¤¤¤-¤¤¤¤¤¤-∥")
        print("∥                              ∥  SPELMENY ∥                            ∥")
        print("∥-____________===               ‾‾‾‾‾‾‾‾‾‾‾             ===____________-∥")
        print("∥¤---------------------------------------------------------------------¤∥")
        print("∥¤-=======-=============-===================--=============-==========-¤∥")
        print(" ==========--==================-====================--================== ")
        print("\n[1] Skapa Ny karaktär  \n \n[2] Ladda sparat äventyr & fortsätt spela")

    loop = True

    while loop:

        print_choices()

        print("\nDu kan endast navigera med siffror!")

        choice = int(input("\nAnge ett alternativ:\n >"))

        clear_screen()

        while choice == 1:

            while True:

                print("\nTillgliga klasser : [ Riddare ]   [ Trollkarl  ]   [ Tjuv ]")

                player_class = input("\nVar god välj en klass:  >\n").lower()

                if player_class in ("tjuv", 'trollkarl', 'riddare'):
                    name = input("Var god välj ett namn \n >\n")
                    create_json('CurrentHero')

                    if player_class == 'tjuv':
                        current_character = (Thief(name))
                        save("CurrentHero", (current_character))

                    if player_class == 'trollkarl':
                        current_character = (Wizard(name))
                        save("CurrentHero", (current_character))

                    if player_class == 'riddare':
                        current_character = (Knight(name))
                        save("CurrentHero", (current_character))

                    clear_screen()

                    while True:
                        dificulty()

                        game_mode = input("vilken svårighetsgrad du vill spela på? \n:").lower()

                        if game_mode == "liten":
                            game(4, 4)
                            break
                            # Load small map

                        elif game_mode == "mellan":
                            game(5, 5)
                            break
                            # load medium map

                        elif game_mode == "stor":
                            game(8, 8)
                            break
                            # load big map

                # start game

                        else:

                            if game_mode != ("liten", "mellan", "stor"):

                                clear_screen()
                                print("Felaktig inmatning. försök igen:")
                                loop = False

        if choice == 2:
            print("≪ <=--=========---===---=========-=> ≫")
            print("≪ -=======-==-====--======--=======- ≫")
            print("≪∥                                   >>")
            print("≪ -=-∥ ≫ Laddar  information  ≪ ∥-=- ≫")
            print("≪--===-                        -====--≫")
            print("≪ <-======-=======---=======--=====-> ≫")

            user = input("Tryck y för att ladda din karaktär\n >").lower()

            if user == 'y':

                current_character = load("SavedHero")
                print(current_character)

            user = input(" \n Tryck [1] för att återvända till meny\n >").lower()
            clear_screen()

            # Load game


main_menu()
