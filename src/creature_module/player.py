from src.creature_module._creature import Creature


class Player(Creature):

    # constructor
    def __init__(self):
        Creature.__init__(self, 100, 5)
