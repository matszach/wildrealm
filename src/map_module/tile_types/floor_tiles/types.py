from src.map_module.tile_types.floor_tiles._floor_tile import FloorTileType
from src.map_module.tile_types.floor_tiles.const import *


# ===== WATER =====
class DeepWaterFloorTile(FloorTileType):
    id = 0
    name = 'deep water'
    image = None
    color = (0, 0, 80)
    speed_mod = FLOOR_SPEED_HALT
    swimming = True


class ShallowWaterFloorTile(FloorTileType):
    id = 1
    name = 'shallow water'
    image = None
    color = (0, 0, 180)
    speed_mod = FLOOR_SPEED_HEAVY_SLOW
    swimming = True


# ===== SAND ====
class SandFloorTile(FloorTileType):
    id = 2
    name = 'sand'
    image = None
    color = (180, 180, 0)
    speed_mod = FLOOR_SPEED_LIGHT_SLOW
    swimming = False


# ===== GRASS =====
class GrassFloorTile(FloorTileType):
    id = 3
    name = 'grass'
    image = None
    color = (0, 180, 0)
    speed_mod = FLOOR_SPEED_DEFAULT
    swimming = False


# ===== STONE =====
class SurfaceStoneFloorTile(FloorTileType):
    id = 4
    name = 'surface stone'
    image = None
    color = (110, 110, 110)
    speed_mod = FLOOR_SPEED_DEFAULT
    swimming = False


class DeepStoneFloorTile(FloorTileType):
    id = 5
    name = 'deep stone'
    image = None
    color = (80, 80, 80)
    speed_mod = FLOOR_SPEED_DEFAULT
    swimming = False

