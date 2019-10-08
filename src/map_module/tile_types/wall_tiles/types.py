from src.map_module.tile_types.wall_tiles._wall_tile import WallTileType
from src.map_module.tile_types.wall_tiles.const import *
from src.map_module.tile_types.id_generator import IdGenerator

id_gen = IdGenerator()


# ===== AIR =====
class AirWallTile(WallTileType):
    id = id_gen.next()
    name = 'air'
    image = None
    color = None
    blocks_movement = False
    breakable = False
    drops_loot = False


# ===== TREES AND PLANTS =====
class TreeWallTile(WallTileType):
    id = id_gen.next()
    name = 'tree'
    image = None
    color = (0, 90, 0)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_1
    durability = WALL_DURABILITY_TIER_2
    drops_loot = True
    loot_table = ()  # TODO


class SeaweedWallTile(WallTileType):
    id = id_gen.next()
    name = 'seaweed'
    image = None
    color = (150, 250, 0)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_1
    durability = WALL_DURABILITY_TIER_1
    drops_loot = True
    loot_table = ()  # TODO


# ===== ROCK =====
class SurfaceRockWallTile(WallTileType):
    id = id_gen.next()
    name = 'surface rock'
    image = None
    color = (40, 40, 40)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_2
    durability = WALL_DURABILITY_TIER_2
    drops_loot = True
    loot_table = ()  # TODO


class DeepRockWallTile(WallTileType):
    id = id_gen.next()
    name = 'deep rock'
    image = None
    color = (20, 20, 20)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_3
    durability = WALL_DURABILITY_TIER_3
    drops_loot = True
    loot_table = ()  # TODO


# ===== ORES =====
class CopperVeinWallTile(WallTileType):
    id = id_gen.next()
    name = 'copper vein'
    image = None
    color = (250, 120, 0)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_2
    durability = WALL_DURABILITY_TIER_3
    drops_loot = True
    loot_table = ()  # TODO


class IronVeinWallTile(WallTileType):
    id = id_gen.next()
    name = 'iron vein'
    image = None
    color = (190, 120, 50)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_3
    durability = WALL_DURABILITY_TIER_3
    drops_loot = True
    loot_table = ()  # TODO


class SilverVeinWallTile(WallTileType):
    id = id_gen.next()
    name = 'silver vein'
    image = None
    color = (90, 90, 180)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_4
    durability = WALL_DURABILITY_TIER_3
    drops_loot = True
    loot_table = ()  # TODO


class GoldVeinWallTile(WallTileType):
    id = id_gen.next()
    name = 'gold vein'
    image = None
    color = (250, 180, 0)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_5
    durability = WALL_DURABILITY_TIER_4
    drops_loot = True
    loot_table = ()  # TODO


# ===== CHESTS AND TREASURES =====
class WoodenTreasureChestWallTile(WallTileType):
    id = id_gen.next()
    name = 'wooden treasure chest'
    image = None
    color = (60, 20, 0)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_1
    durability = WALL_DURABILITY_TIER_3
    drops_loot = True
    loot_table = ()  # TODO


class WaterTreasureChestWallTile(WallTileType):
    id = id_gen.next()
    name = 'water treasure chest'
    image = None
    color = (0, 250, 250)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_3
    durability = WALL_DURABILITY_TIER_3
    drops_loot = True
    loot_table = ()  # TODO


class MagicTreasureChestWallTile(WallTileType):
    id = id_gen.next()
    name = 'magic treasure chest'
    image = None
    color = (250, 0, 250)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_5
    durability = WALL_DURABILITY_TIER_5
    drops_loot = True
    loot_table = ()  # TODO


# ===== BUILDABLE =====
class PlankWallTile(WallTileType):
    id = id_gen.next()
    name = 'plank wall'
    image = None
    color = (100, 70, 0)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_2
    durability = WALL_DURABILITY_TIER_2
    drops_loot = True
    loot_table = ()  # TODO


class StoneBrickWallTile(WallTileType):
    id = id_gen.next()
    name = 'stone brick wall'
    image = None
    color = (30, 10, 10)
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_3
    durability = WALL_DURABILITY_TIER_4
    drops_loot = True
    loot_table = ()  # TODO
