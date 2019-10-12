from src.game_core_module.game_state.game_state import GameState
from src.game_core_module.game_state.new_game_starter import NewGameStarter
from src.game_core_module.game_state.game_state_saver_loader import GameStateSaverLoader
from src.map_module.map_painter import MapPainter
from src.display_module.view_info import ViewInfo
from src.display_module.view_display_handler import ViewDisplayHandler
from src.game_core_module.app_states import AppStates
from src.game_core_module.app_state_handler import AppStateHandler
from src.game_core_module.user_input_handler import UserInputHandler
import pygame
import sys
from src.threading_module.thread_manager import ThreadManager


# represents the application proper
class Game:

    # current game state
    game_state: GameState = None

    # app's current mode (in game / menu / paused)
    app_state: int = AppStates.MAIN_MENU

    # generates new game state
    new_game_starter: NewGameStarter = NewGameStarter()

    # saves / loads a game state into / from a file
    saver_loader: GameStateSaverLoader = GameStateSaverLoader()

    # outputs the map as a .png
    map_painter: MapPainter = MapPainter()

    # paints current state's view
    view_display_handler: ViewDisplayHandler = ViewDisplayHandler()

    # manages user input
    user_input_handler: UserInputHandler = UserInputHandler()

    # checks for conditions to switch between app states
    app_state_handler: AppStateHandler = AppStateHandler()

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
    starts a new game
    """
    @staticmethod
    def start_new_game():
        # todo args and loading state
        Game.game_state = Game.new_game_starter.new_game()
        Game.app_state = AppStates.IN_GAME_PLAY

    """
    initiates the app proper
    """
    @staticmethod
    def launch():
        ThreadManager.start_thread(Game._main_loop)

    @staticmethod
    def _main_loop():

        flags = pygame.RESIZABLE | pygame.DOUBLEBUF
        surface = pygame.display.set_mode(ViewInfo.DEFAULT_WINDOW_SIZE, flags)
        clock = pygame.time.Clock()

        pygame.font.init()
        pygame.display.set_caption('Wildrealm')
        # pygame.display.set_icon(GAME_ICON)

        while True:

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # todo on qut actions here (saves / forced thread shutdowns?)
                    sys.exit()
                if event.type == pygame.VIDEORESIZE:
                    ViewInfo.adjust(event)
                    surface = pygame.display.set_mode((event.w, event.h), flags)

            surface.fill(ViewInfo.BACKGROUND_COLOR)

            pygame.display.update()
