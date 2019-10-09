from src.game_core_module.game_state.game_state import GameState
from src.game_core_module.game_state.new_game_starter import NewGameStarter
from src.game_core_module.game_state.game_state_saver_loader import GameStateSaverLoader
from src.map_module.map_painter import MapPainter
from src.display_module.view_info import ViewInfo
import pygame
import sys


# represents the application proper
class Game:

    # current game state
    game_state: GameState = None

    # states whether the game is pause or not
    paused: bool = True

    # generates new game state
    new_game_starter: NewGameStarter = NewGameStarter()

    # saves / loads a game state into / from a file
    saver_loader: GameStateSaverLoader = GameStateSaverLoader()

    # outputs the map as a .png
    map_painter: MapPainter = MapPainter()

    """
    game state saving / loading
    """
    @staticmethod
    def save_game(slot_id: int):
        Game.saver_loader.save(Game.game_state, f'saved_games\\game{slot_id}.sav')
        Game.map_painter.paint_map(Game.game_state.world_map, f'saved_games\\map{slot_id}.png')

    @staticmethod
    def load_game(slot_id: int):
        Game.game_state = Game.saver_loader.load(f'saved_games\\game{slot_id}.sav')

    """
    initiates the game proper
    """
    @staticmethod
    def launch():

        pygame.font.init()
        pygame.display.set_caption('Wildrealm')
        # pygame.display.set_icon(GAME_ICON)

        flags = pygame.RESIZABLE | pygame.DOUBLEBUF
        surface = pygame.display.set_mode((500, 500), flags)
        clock = pygame.time.Clock()

        while True:

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.VIDEORESIZE:
                    # vi.adjust(event.w, event.h)
                    surface = pygame.display.set_mode((event.w, event.h), flags)

            surface.fill(ViewInfo.background)

            pygame.display.update()
