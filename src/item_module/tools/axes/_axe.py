from src.item_module.tools._tool import Tool
from src.map_module.tile_types.wall_tiles.list import WALL_TILES_BY_ID


class Axe(Tool):

    def _effect(self, x: int, y: int):
        map_walls = self._get_game_state().world_map.walls
        wall_tile = WALL_TILES_BY_ID[map_walls[x, y]]
        if wall_tile.axe_harvested:
            pass
            # TODO
