from src.map_module.tile_types.floor_tiles._floor_tile import FloorTileType
from src.map_module.tile_types.floor_tiles.const import *
from util.id_generator import IdGenerator


id_gen = IdGenerator()


# ===== WATER =====
class DeepWaterFloorTile(FloorTileType):
    id = id_gen.next()
    name = 'deep water'
    image = None
    color = (0, 0, 80)
    speed_mod = FLOOR_SPEED_HALT
    swimming = True
    wallable = False


class ShallowWaterFloorTile(FloorTileType):
    id = id_gen.next()
    name = 'shallow water'
    image = None
    color = (0, 0, 180)
    speed_mod = FLOOR_SPEED_HEAVY_SLOW
    swimming = True
    wallable = False


# ===== SAND ====
class SandFloorTile(FloorTileType):
    id = id_gen.next()
    name = 'sand'
    image = None
    color = (180, 180, 0)
    speed_mod = FLOOR_SPEED_LIGHT_SLOW
    swimming = False
    wallable = False


# ===== GRASS =====
class GrassFloorTile(FloorTileType):
    id = id_gen.next()
    name = 'grass'
    image = None
    color = (0, 180, 0)
    speed_mod = FLOOR_SPEED_DEFAULT
    swimming = False
    wallable = True


# ===== STONE =====
class SurfaceStoneFloorTile(FloorTileType):
    id = id_gen.next()
    name = 'surface stone'
    image = None
    color = (110, 110, 110)
    speed_mod = FLOOR_SPEED_DEFAULT
    swimming = False
    wallable = True


class DeepStoneFloorTile(FloorTileType):
    id = id_gen.next()
    name = 'deep stone'
    image = None
    color = (80, 80, 80)
    speed_mod = FLOOR_SPEED_DEFAULT
    swimming = False
    wallable = True


# ===== BUILDABLE =====
class PlankFloorTile(FloorTileType):
    id = id_gen.next()
    name = 'plank floor'
    image = None
    color = (150, 120, 0)
    speed_mod = FLOOR_SPEED_DEFAULT
    swimming = False
    wallable = True


class StoneBrickFloorTile(FloorTileType):
    id = id_gen.next()
    name = 'stone brick floor'
    image = None
    color = (90, 60, 60)
    speed_mod = FLOOR_SPEED_DEFAULT
    swimming = False
    wallable = True
