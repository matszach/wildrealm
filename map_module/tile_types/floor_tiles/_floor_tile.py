
class FloorTileType:

    # floor tile's id number
    id: int = None

    # floor tile's name
    name: str = '[default  floor tile name]'

    # reference to pygame's Image, for actual in-game display
    image: object = None

    # RGB color, for exported mam / in-game mini-map
    color: tuple = (255, 255, 255)

    # speed modifier applied to a character
    speed_mod: float = 1.0

    # creatures that can swim are not slowed on this terrain
    # this includes swimming enemies and the player in a boat for example
    swimming: bool = False
