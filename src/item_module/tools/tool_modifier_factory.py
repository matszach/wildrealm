from src.item_module.tools.tool_modifier import ToolModifier
from random import choice, random


class ToolModifierFactory:

    modifier_chance = 0.4

    possible_modifiers = [
        ['Broken', -1, -1, 0.75, -2],
        ['Weak', -1, 0, 1, -1],
        ['Slow', 0, -1, 1, -1],
        ['Brittle', 0, 0, 0.5, -1],
        ['Powerful', 1, 0, 1, 1],
        ['Quick', 0, 1, 1, 1],
        ['Sturdy', 0, 0, 1.5, 1],
        ['Heavy', 2, -1, 1, 1],
        ['Light', -1, 2, 1, 1],
        ['Reckless', 1, 1, 0.75, 1],
        ['Mighty', 2, 0, 1, 2]
    ]

    @staticmethod
    def get_random() -> ToolModifier:
        if random() < ToolModifierFactory.modifier_chance:
            return None
        else:
            tm = choice(ToolModifierFactory.possible_modifiers)
            return ToolModifier(tm[0], tm[1], tm[2], tm[3], tm[4])
