

class FloorTileType:
    id: int
    name: str
    image: object  # todo pygame image reference
    color: tuple
    speed_mod: float
    requires_boat: bool


FloorTileType.id