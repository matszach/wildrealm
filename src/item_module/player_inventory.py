

class PlayerInventory:

    def __init__(self):
        self.item_slots: list = [[None for i in range(12)] for j in range(4)]
