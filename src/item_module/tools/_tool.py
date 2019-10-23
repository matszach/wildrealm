from src.item_module._item import Item
from src.item_module._usable import Usable
from src.item_module._craftable import Craftable
from src.item_module.tools.tool_modifier import ToolModifier


class Tool(Item, Usable, Craftable):

    base_power: float

    base_speed: float

    base_max_durability: int

    def _calc_cooldown(self):
        return int(100/self.speed)

    """
    proper effect of the tool (mining a wall tile / damaging an enemy ...)
    """
    def _effect(self, x: int, y: int):
        pass

    """
    fizzle effect of the tool (much weaker or none / only animation)
    """
    def _fizzle(self, x: int, y: int):
        pass

    def use(self, x: int, y: int):
        if self.curr_cooldown > 0:
            return
        elif self.curr_durability > 0:
            self._fizzle(x, y)
        else:
            self._effect(x, y)
            self.curr_durability -= 1
            self._start_cooldown()

    # type of item required to repair the tool
    repair_material_type = None

    def repair(self, repair_material: Item) -> bool:
        if isinstance(repair_material, self.repair_material_type):
            self.curr_durability = self.max_durability
            return True
        else:
            return False

    def __init__(self, tool_mod: ToolModifier):
        Item.__init__(self)
        Usable.__init__(self)
        Craftable.__init__(self)

        self.modifier = tool_mod

        if tool_mod:
            self.power: int = self.base_power + tool_mod.power_mod
            self.speed: int = self.base_speed + tool_mod.speed_mod
            self.max_durability: int = self.base_max_durability * tool_mod.durability_mod
        else:
            self.power: int = self.base_power
            self.speed: int = self.base_speed
            self.max_durability: int = self.base_max_durability

        self.curr_durability: int = self.max_durability
