class Treasure:
    '''Creates Treasures'''

    def __init__(self):
        self.type_of_treasure = 'Skatt'
        self.poäng = 0
        self.vanlighet = 0


class Lösa_slantar(Treasure):
    '''Creates an instance of lösa slantar'''

    def __init__(self):
        super().__init__()
        self.namn = 'Lösa slantar'
        self.poäng = 2
        self.vanlighet = 40


class Pengapung(Treasure):
    '''Creates an instance pengapung'''

    def __init__(self):
        super().__init__()
        self.namn = 'Pengapung'
        self.poäng = 6
        self.vanlighet = 20


class Guldsmycken(Treasure):
    '''Creates an instance of guldsmycken'''
    def __init__(self):
        super().__init__()
        self.namn = 'Guldsmycken'
        self.poäng = 10
        self.vanlighet = 15

class Ädelsten(Treasure):
    '''Creates an instance of ädelsten'''

    def __init__(self):
        super().__init__()
        self.namn = 'Ädelsten'
        self.poäng = 14
        self.vanlighet = 10


class Liten_skattkista(Treasure):
    '''Creates an instance of liten skattkista'''

    def __init__(self):
        super().__init__()
        self.namn = 'Liten skattkista'
        self.poäng = 20
        self.vanlighet = 5
