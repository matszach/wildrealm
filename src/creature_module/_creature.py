

# base class
class Creature:

    def move_to(self, x: int, y: int):
        self.x = x
        self.y = y

    def take_damage(self, damage: float):
        damage = damage - self.defense
        damage = damage if damage > 1 else 1
        self.curr_health -= damage

    def heal(self, healing: float):
        self.curr_health += healing
        self.curr_health = self.max_health if self.curr_health > self.max_health else self.curr_health

    def is_dead(self) -> bool:
        return self.curr_health <= 0

    # constructor
    def __init__(self, max_health: float = 100, defense: int = 0):

        # health and defense
        self.max_health: float = max_health
        self.curr_health: float = max_health
        self.defense: int = defense

        # creatures location
        self.x: int = 0
        self.y: int = 0




