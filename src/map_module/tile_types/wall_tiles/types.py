from src.map_module.tile_types.wall_tiles._wall_tile import WallTileType
from src.map_module.tile_types.wall_tiles.const import *


# ===== AIR =====
class AirWallTile(WallTileType):
    id = 0
    name = 'air'
    image = None
    color = None
    blocks_movement = False
    breakable = False
    drops_loot = False


# ===== TREES =====
class TreeWallTile(WallTileType):
    id = 1
    name = 'tree'
    image = None
    color = (0, 90, 0)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_1
    durability = WALL_DURABILITY_TIER_2
    drops_loot = True
    loot_table = ()  # TODO


# ===== ROCK =====
class SurfaceRockWallTile(WallTileType):
    id: int = 2
    name: str = 'surface rock'
    image: object = None
    color: tuple = (40, 40, 40)
    blocks_movement: bool = True
    breakable: bool = True
    resistance: int = WALL_RESISTANCE_TIER_2
    durability: float = WALL_DURABILITY_TIER_2
    drops_loot = True
    loot_table = ()  # TODO


class DeepRockWallTile(WallTileType):
    id: int = 3
    name: str = 'deep rock'
    image: object = None
    color: tuple = (20, 20, 20)
    blocks_movement: bool = True
    breakable: bool = True
    resistance: int = WALL_RESISTANCE_TIER_3
    durability: float = WALL_DURABILITY_TIER_3
    drops_loot = True
    loot_table = ()  # TODO


# ===== ORES =====
class CopperVeinWallTile(WallTileType):
    id: int = 4
    name: str = 'copper vein'
    image: object = None
    color: tuple = (250, 120, 0)
    blocks_movement: bool = True
    breakable: bool = True
    resistance: int = WALL_RESISTANCE_TIER_2
    durability: float = WALL_DURABILITY_TIER_3
    drops_loot = True
    loot_table = ()  # TODO


class IronVeinWallTile(WallTileType):
    id: int = 5
    name: str = 'iron vein'
    image: object = None
    color: tuple = (190, 120, 50)
    blocks_movement: bool = True
    breakable: bool = True
    resistance: int = WALL_RESISTANCE_TIER_3
    durability: float = WALL_DURABILITY_TIER_3
    drops_loot = True
    loot_table = ()  # TODO


class SilverVeinWallTile(WallTileType):
    id: int = 6
    name: str = 'silver vein'
    image: object = None
    color: tuple = (90, 90, 180)
    blocks_movement: bool = True
    breakable: bool = True
    resistance: int = WALL_RESISTANCE_TIER_4
    durability: float = WALL_DURABILITY_TIER_3
    drops_loot = True
    loot_table = ()  # TODO


class GoldVeinWallTile(WallTileType):
    id: int = 7
    name: str = 'gold vein'
    image: object = None
    color: tuple = (250, 180, 0)
    blocks_movement: bool = True
    breakable: bool = True
    resistance: int = WALL_RESISTANCE_TIER_5
    durability: float = WALL_DURABILITY_TIER_4
    drops_loot = True
    loot_table = ()  # TODO
