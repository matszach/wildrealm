
class WallTileType:

    # wall tile's id number
    id: int = None

    # wall tile's name
    name: str = '[default wall tile name]'

    # reference to pygame's Image, for actual in-game display
    image: object = None

    # RGB color, for exported mam / in-game mini-map
    color: tuple = (0, 0, 0)

    # block character's sight and light (if any)
    blocks_vision: bool = True

    # states if the wall tile can be traveled through
    blocks_movement: bool = True

    # states if the wall tile can be broken
    breakable: bool = False

    # minimum tool power required to break
    resistance: int = 0

    # chance of breaking on hit
    break_chance: float = 1

    # indicates that the wall should be harvested with a pick / axe,
    # to have its break chance doubled and resistance reduced by 1
    pick_harvested: bool = False
    axe_harvested: bool = False

    # states if breaking the wall has a chance to drop a piece of loot
    drops_loot: bool = False

    # lists possible items that can be dropped
    loot_table: tuple = ()
