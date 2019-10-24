from src.map_module.tile_types.wall_tiles._wall_tile import WallTileType
from src.map_module.tile_types.wall_tiles.const import *
from util.id_generator import IdGenerator
from src.display_module.image_asset_loader.image_loader import ImageLoader


id_gen = IdGenerator()


# ===== AIR =====
class AirWallTile(WallTileType):
    id = id_gen.next()
    name = 'air'
    image = None
    color = None
    blocks_vision = False
    blocks_movement = False
    breakable = False
    drops_loot = False


# ===== TREES AND PLANTS =====
class TreeWallTile(WallTileType):
    id = id_gen.next()
    name = 'tree'
    image = ImageLoader.WALLS['tree']
    color = (0, 90, 0)
    blocks_vision = False
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_1
    break_chance = WALL_DURABILITY_TIER_2
    pick_harvested = False
    axe_harvested = True
    drops_loot = True
    loot_table = ()  # TODO


class SeaweedWallTile(WallTileType):
    id = id_gen.next()
    name = 'seaweed'
    image = ImageLoader.WALLS['seaweed']
    color = (150, 250, 0)
    blocks_vision = False
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_1
    break_chance = WALL_DURABILITY_TIER_1
    pick_harvested = False
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


class BerryBushWallTile(WallTileType):
    id = id_gen.next()
    name = 'berry bush'
    image = ImageLoader.WALLS['berry_bush']
    color = (250, 0, 0)
    blocks_vision = False
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_1
    break_chance = WALL_DURABILITY_TIER_2
    pick_harvested = False
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


# ===== ROCK =====
class SurfaceRockWallTile(WallTileType):
    id = id_gen.next()
    name = 'surface rock'
    image = ImageLoader.WALLS['surface_rock']
    color = (40, 40, 40)
    blocks_vision = True
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_2
    break_chance = WALL_DURABILITY_TIER_2
    pick_harvested = True
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


class DeepRockWallTile(WallTileType):
    id = id_gen.next()
    name = 'deep rock'
    image = ImageLoader.WALLS['deep_rock']
    color = (20, 20, 20)
    blocks_vision = True
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_3
    break_chance = WALL_DURABILITY_TIER_3
    pick_harvested = True
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


# ===== ORES =====
class CopperVeinWallTile(WallTileType):
    id = id_gen.next()
    name = 'copper vein'
    image = ImageLoader.WALLS['copper_vein']
    color = (250, 120, 0)
    blocks_vision = True
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_2
    break_chance = WALL_DURABILITY_TIER_3
    pick_harvested = True
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


class IronVeinWallTile(WallTileType):
    id = id_gen.next()
    name = 'iron vein'
    image = ImageLoader.WALLS['iron_vein']
    color = (190, 120, 50)
    blocks_vision = True
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_3
    break_chance = WALL_DURABILITY_TIER_3
    pick_harvested = True
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


class SilverVeinWallTile(WallTileType):
    id = id_gen.next()
    name = 'silver vein'
    image = ImageLoader.WALLS['silver_vein']
    color = (90, 90, 180)
    blocks_vision = True
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_4
    break_chance = WALL_DURABILITY_TIER_3
    pick_harvested = True
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


class GoldVeinWallTile(WallTileType):
    id = id_gen.next()
    name = 'gold vein'
    image = ImageLoader.WALLS['gold_vein']
    color = (250, 180, 0)
    blocks_vision = True
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_5
    break_chance = WALL_DURABILITY_TIER_4
    pick_harvested = True
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


# ===== CHESTS AND TREASURES =====
class WoodenTreasureChestWallTile(WallTileType):
    id = id_gen.next()
    name = 'wooden treasure chest'
    image = ImageLoader.WALLS['wooden_chest']
    color = (60, 20, 0)
    blocks_vision = False
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_1
    break_chance = WALL_DURABILITY_TIER_3
    pick_harvested = False
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


class WaterTreasureChestWallTile(WallTileType):
    id = id_gen.next()
    name = 'water treasure chest'
    image = ImageLoader.WALLS['water_chest']
    color = (0, 250, 250)
    blocks_vision = False
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_3
    break_chance = WALL_DURABILITY_TIER_3
    pick_harvested = False
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


class MagicTreasureChestWallTile(WallTileType):
    id = id_gen.next()
    name = 'magic treasure chest'
    image = ImageLoader.WALLS['magic_chest']
    color = (250, 0, 250)
    blocks_vision = False
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_5
    break_chance = WALL_DURABILITY_TIER_5
    pick_harvested = False
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO


# ===== BUILDABLE =====
class PlankWallTile(WallTileType):
    id = id_gen.next()
    name = 'plank wall'
    image = ImageLoader.WALLS['plank_wall']
    color = (100, 70, 0)
    blocks_vision = True
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_2
    break_chance = WALL_DURABILITY_TIER_2
    pick_harvested = False
    axe_harvested = True
    drops_loot = True
    loot_table = ()  # TODO


class StoneBrickWallTile(WallTileType):
    id = id_gen.next()
    name = 'stone brick wall'
    image = ImageLoader.WALLS['stone_brick_wall']
    color = (30, 10, 10)
    blocks_vision = True
    blocks_movement = True
    breakable = True
    resistance = WALL_RESISTANCE_TIER_3
    break_chance = WALL_DURABILITY_TIER_4
    pick_harvested = True
    axe_harvested = False
    drops_loot = True
    loot_table = ()  # TODO
