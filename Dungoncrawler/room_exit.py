from utils import prompt_exit


class Room_with_exit:
    '''Creates a room with an exit'''
    def __init__(self):
        self.exit = True

    def exit_command(self):
        '''Takes in command from player, exit or continue.'''
        prompt_exit()


room1 = Room_with_exit()
room1.exit_command()
