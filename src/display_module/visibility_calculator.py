from src.game_core_module.game_state.game_state import GameState
from src.map_module.tile_types.wall_tiles.list import WALL_TILES_BY_ID
from math import sin, cos


class VisibilityCalculator:

    _visible_tiles = []
    _directions = [deg for deg in range(0, 360, 1)]

    @staticmethod
    def calculate(game_state: GameState) -> list:

        VisibilityCalculator._visible_tiles.clear()
        sight_range = 15
        player_x = game_state.player.x
        player_y = game_state.player.y

        walls = game_state.world_map.walls

        for d in VisibilityCalculator._directions:
            VisibilityCalculator._check_visibility_in_direction(player_x, player_y, sight_range, d, walls)

        return VisibilityCalculator._visible_tiles

    @staticmethod
    def _check_visibility_in_direction(x: int, y: int, sight_range: int, direction: float, walls):
        for s in range(0, sight_range):
            x_f = round(x + cos(direction) * s)
            y_f = round(y + sin(direction) * s)
            VisibilityCalculator._add_tile((x_f, y_f))
            if WALL_TILES_BY_ID[walls[x_f, y_f]].blocks_vision:
                return

    @staticmethod
    def _add_tile(tile: tuple):
        if tile not in VisibilityCalculator._visible_tiles:
            VisibilityCalculator._visible_tiles.append(tile)

