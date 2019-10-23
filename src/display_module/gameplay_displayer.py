from src.game_core_module.app_states import AppStates
from src.game_core_module.game_state.game_state import GameState
from src.map_module.worldmap import WorldMap
from src.display_module.view_info import ViewInfo
from src.display_module.image_asset_loader.image_loader import ImageLoader
import pygame
from src.map_module.tile_types.floor_tiles.list import FLOOR_TILES_BY_ID
from src.map_module.tile_types.wall_tiles.list import WALL_TILES_BY_ID
from math import ceil
from src.input_module.mouse_handler import MouseHandler


class GameplayDisplayer:

    """
    :param surface - pygame's surface
    :param wmap - map of the drawn world
    :param x, y - actual position of the tile in the game
    :param draw - draw position of the tile o the surface
    """
    @staticmethod
    def _draw_floor_tile_as_color(surface, wmap: WorldMap, x: int, y: int, draw_x: int, draw_y: int):
        if 0 <= x < wmap.x_size and 0 <= y < wmap.y_size:
            color = FLOOR_TILES_BY_ID[wmap.floors[x, y]].color
            u = ViewInfo.unit
            pygame.draw.rect(surface, color,
                             (ViewInfo.offset_x + draw_x * u, ViewInfo.offset_y + draw_y * u, ceil(u), ceil(u)))

    @staticmethod
    def _draw_floor_tile_as_image(surface, wmap: WorldMap, x: int, y: int, draw_x: int, draw_y: int):
        if 0 <= x < wmap.x_size and 0 <= y < wmap.y_size:
            image = FLOOR_TILES_BY_ID[wmap.floors[x, y]].image
            u = ViewInfo.unit
            image = pygame.transform.scale(image, (ceil(u), ceil(u)))
            origin = (ViewInfo.offset_x + draw_x * u, ViewInfo.offset_y + draw_y * u)
            surface.blit(image, origin)

    @staticmethod
    def _draw_wall_tile_as_color(surface, wmap: WorldMap, x: int, y: int, draw_x: int, draw_y: int):
        if 0 <= x < wmap.x_size and 0 <= y < wmap.y_size:
            color = WALL_TILES_BY_ID[wmap.walls[x, y]].color
            u = ViewInfo.unit
            if color:
                pygame.draw.rect(surface, color,
                                 (ViewInfo.offset_x + (draw_x + 0.05) * u, ViewInfo.offset_y + (draw_y + 0.05) * u
                                  , ceil(u * 0.9), ceil(u * 0.9)))

    @staticmethod
    def _draw_wall_tile_as_image(surface, wmap: WorldMap, x: int, y: int, draw_x: int, draw_y: int):
        if 0 <= x < wmap.x_size and 0 <= y < wmap.y_size:
            image = WALL_TILES_BY_ID[wmap.walls[x, y]].image
            if image:
                u = ViewInfo.unit
                image = pygame.transform.scale(image, (ceil(u), ceil(u)))
                origin = (ViewInfo.offset_x + draw_x * u, ViewInfo.offset_y + draw_y * u)
                surface.blit(image, origin)

    @staticmethod
    def _draw_tiles(surface, game_state: GameState):
        x_offset = int((ViewInfo.SIZE_UNITS_X - 1) / 2)
        y_offset = int((ViewInfo.SIZE_UNITS_Y - 1) / 2)

        for draw_x in range(ViewInfo.SIZE_UNITS_X):
            for draw_y in range(ViewInfo.SIZE_UNITS_Y):
                x = game_state.player.x + draw_x - x_offset
                y = game_state.player.y + draw_y - y_offset

                GameplayDisplayer._draw_floor_tile_as_image(surface, game_state.world_map, x, y, draw_x, draw_y)
                GameplayDisplayer._draw_wall_tile_as_image(surface, game_state.world_map, x, y, draw_x, draw_y)

    @staticmethod
    def _draw_player(surface, game_state: GameState):
        image = ImageLoader.CREATURES['player']  # TEMP TODO image based on character field
        u = ViewInfo.unit
        image = pygame.transform.scale(image, (int(u), int(u)))
        origin = (ViewInfo.offset_x + 17 * u, ViewInfo.offset_y + 10 * u)
        surface.blit(image, origin)

    @staticmethod
    def _draw_mouse_highlight(surface, game_state: GameState):
        # TODO color based on selected item
        u = ViewInfo.unit
        x = MouseHandler.mouse_pos[0]
        x = x - (x - ViewInfo.offset_x) % u
        y = MouseHandler.mouse_pos[1]
        y = y - (y - ViewInfo.offset_y) % u
        color = (0, 0, 255)
        rect = (x, y, u, u)
        width = int(u/10)
        pygame.draw.rect(surface, color, rect, width)

    @staticmethod
    def _draw_shading(surface):
        shade = pygame.Surface(ViewInfo.window_size)
        shade.set_alpha(210)
        shade.fill((0, 0, 20))
        surface.blit(shade, (0, 0))

    """
    based on current game state displays the game-play
    """
    @staticmethod
    def display(surface, app_state: int, game_state: GameState):

        if app_state == AppStates.IN_GAME_PLAY:
            GameplayDisplayer._draw_tiles(surface, game_state)
            GameplayDisplayer._draw_player(surface, game_state)
            GameplayDisplayer._draw_mouse_highlight(surface, game_state)

        elif app_state in [AppStates.IN_GAME_PAUSED, AppStates.IN_GAME_SAVE_GAME, AppStates.IN_GAME_CONFIRM_EXIT,
                           AppStates.IN_GAME_INVENTORY]:
            GameplayDisplayer._draw_tiles(surface, game_state)
            GameplayDisplayer._draw_player(surface, game_state)
            GameplayDisplayer._draw_shading(surface)
