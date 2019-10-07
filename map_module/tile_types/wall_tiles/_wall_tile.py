
class WallTileType:

    # wall tile's id number
    id: int = None

    # wall tile's name
    name: str = '[default wall tile name]'

    # reference to pygame's Image, for actual in-game display
    image: object = None

    # RGB color, for exported mam / in-game mini-map
    color: tuple = (0, 0, 0)

    # states if the wall tile can be traveled through
    blocks_movement: bool = True

    # states if the wall tile can be broken
    breakable: bool = False

    # minimum power required to break
    resistance: int = 0

    # chance of breaking on hit
    durability: float = 1

    # states if breaking the wall has a chance to drop a piece of loot
    drops_loot: bool = False

    # lists possible items that can be dropped
    loot_table: tuple = ()
