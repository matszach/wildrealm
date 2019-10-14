from src.game_core_module.game_state.game_state import GameState
from src.game_core_module.game_state.new_game_starter import NewGameStarter
from src.game_core_module.game_state.game_state_saver_loader import GameStateSaverLoader
from src.map_module.map_painter import MapPainter
from src.display_module.view_info import ViewInfo
from src.game_core_module.app_states import AppStates
import pygame
import sys
import time
from src.threading_module.thread_manager import ThreadManager
from src.display_module.view_displayer import ViewDisplayer


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

    # displays the view based on app state
    view_displayer: ViewDisplayer = ViewDisplayer()

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
        Game.game_state = Game.new_game_starter.prepare_new_game()
        Game.app_state = AppStates.GENERATING_MAP

    """
    handles the app shutdown
    """
    @staticmethod
    def handle_close():
        pass  # TODO

    """
    checks for app state switch conditions and applies changes if necessary
    """
    @staticmethod
    def _app_state_check():
        while True:
            time.sleep(0.1)
            if Game.app_state == AppStates.GENERATING_MAP:
                if Game.new_game_starter.is_ready():
                    Game.game_state = Game.new_game_starter.get_prepared_game_state()
                    Game.app_state = AppStates.IN_GAME_PLAY
            elif Game.app_state == AppStates.IN_GAME_PLAY:
                if Game.game_state.player.is_dead():
                    Game.app_state = AppStates.IN_GAME_GAME_OVER

    """
    initiates the app proper
    """
    @staticmethod
    def launch():
        ThreadManager.start_thread(Game._main_loop)
        ThreadManager.start_daemon(Game._app_state_check())

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
                    Game.handle_close()
                    sys.exit()
                if event.type == pygame.VIDEORESIZE:
                    ViewInfo.adjust(event)
                    surface = pygame.display.set_mode((event.w, event.h), flags)

            surface.fill(ViewInfo.BACKGROUND_COLOR)
            ViewInfo.display_usable_area(surface)
            Game.view_displayer.display(surface, Game.game_state, Game.app_state)

            pygame.display.update()
