
class ToolModifier:

    def __init__(self, name: str, power_mod: int, speed_mod: int, durability_mod: int, tier: int):
        self.name: str = name
        self.power_mod: int = power_mod
        self.speed_mod: int = speed_mod
        self.durability_mod: float = durability_mod
        self.tier: int = tier

