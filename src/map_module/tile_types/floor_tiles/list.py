from src.map_module.tile_types.floor_tiles.types import *


# ===== reference list =====
_FLOOR_TILE_LIST = [
    DeepWaterFloorTile,
    ShallowWaterFloorTile,
    SandFloorTile,
    GrassFloorTile,
    SurfaceStoneFloorTile,
    DeepStoneFloorTile
]

# ===== allows for quicker reference by tiles id =====
FLOOR_TILES_BY_ID = {}
for ft in _FLOOR_TILE_LIST:
    FLOOR_TILES_BY_ID[ft.id] = ft
