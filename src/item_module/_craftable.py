

class Craftable:

    required_crafting_ingredients: list

    required_crafting_tools: list

    required_crafting_stations: list

    @staticmethod
    def are_crafting_requirements_met() -> bool:
        pass


