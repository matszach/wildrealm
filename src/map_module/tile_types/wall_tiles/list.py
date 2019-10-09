from src.map_module.tile_types.wall_tiles.types import *


# ===== reference list =====
_WALL_TILE_LIST = [
    AirWallTile,
    TreeWallTile,
    SeaweedWallTile,
    BerryBushWallTile,
    SurfaceRockWallTile,
    DeepRockWallTile,
    CopperVeinWallTile,
    IronVeinWallTile,
    SilverVeinWallTile,
    GoldVeinWallTile,
    WoodenTreasureChestWallTile,
    WaterTreasureChestWallTile,
    MagicTreasureChestWallTile,
    PlankWallTile,
    StoneBrickWallTile
]

# ===== allows for quicker reference by tiles id =====
WALL_TILES_BY_ID = {}
for wt in _WALL_TILE_LIST:
    WALL_TILES_BY_ID[wt.id] = wt
