from random import randint, choice
import os
from new_room import Room

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.start = (0, 0)
        self.end = (width-1, height-1)
        self.player = (0, 0)
    #    WIP - Check if player has visited room
        self.has_visited = []

    def player_move(self, p):
        x = self.player[0]
        y = self.player[1]
        pos = None

        # Set keys for movement
        # Down
        if p[0] == 'S':
            pos = (x, y + 1)
        # Up
        if p[0] == 'W':
            pos = (x, y - 1)
        # Right
        if p[0] == 'D':
            pos = (x + 1, y)
        # Left
        if p[0] == 'A':
            pos = (x - 1, y)

        if pos not in self.walls:
            self.player = pos
            if pos not in self.has_visited:
                Room()
                # debug only
                # print('Nytt rum')
            self.has_visited.append(pos)
            self.has_visited = list(dict.fromkeys(self.has_visited))
            # debug only
            # print(self.has_visited)



    #   WIP - Check if player has visited room
    #    if pos not in self.has_visited:
    #        self.has_visited.append((x, y))

        if pos == self.end:
            print("You made it to the end of the dungeon!")

# width increases the map size visually, map size is set in the game() function below
def draw_map(g, width=3):
    for y in range(g.height):
        for x in range(g.width):
            # Set custom symbols
            if (x, y) == g.start:
                symbol = '>'
            elif (x, y) == g.end:
                symbol = '<'
            elif (x, y) in g.walls:
                symbol = '#'
            elif (x, y) == g.player:
                symbol = 'P'
        #   WIP - Check if player has visited room
            elif (x, y) in g.has_visited:
                symbol = 'X'
            else:
                symbol = '.'
            print("%%-%ds" % width % symbol, end="")
        print()

# Wall density set in percentage with pct
def return_walls(g: Map, pct=.25) -> list:
    lst = []
    for _ in range(int(g.height*g.width*pct)//2):

        x = randint(1, g.width-2)
        y = randint(1, g.height-2)

        lst.append((x, y))
        lst.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
    return lst


# Clear the old output after input
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Putting it all together with this function
def game(w, h):
    # Map size (4x4, 5x5, 8x8 etc.)
    g = Map(w, h)
    g.walls = return_walls(g)

    while g.player != g.end:
        draw_map(g)
        p = input("Which way? (W A S D)").capitalize()
        g.player_move(p)
        # clear()
    print("You completed the dungeon, thanks for playing!")


if __name__ == '__main__':
    w = 5
    h = 5
    game(w, h)
