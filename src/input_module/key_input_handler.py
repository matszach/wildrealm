from src.game_core_module.app_states import AppStates
from src.game_core_module.game_state.game_state import GameState
from src.threading_module.thread_manager import ThreadManager
import time
import pygame


class KeyInputHandler:

    """
    this prevents unwanted rapid switching between views on button press
    """
    keyblock = False

    @staticmethod
    def _block_keys():
        ThreadManager.start_daemon(KeyInputHandler._block_keys_timer)

    @staticmethod
    def _block_keys_timer():
        KeyInputHandler.keyblock = True
        time.sleep(0.2)
        KeyInputHandler.keyblock = False

    @staticmethod
    def change_app_state(app_state: int):
        from src.game_core_module.game import Game
        Game.app_state = app_state
        KeyInputHandler._block_keys()

    """
    handles user input based on app state
    """
    @staticmethod
    def handle(app_state: int, game_state: GameState):

        if KeyInputHandler.keyblock:
            return

        keys = pygame.key.get_pressed()

        if app_state == AppStates.IN_GAME_PLAY:
            player = game_state.player
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                player.y -= 1
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                player.y += 1
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player.x -= 1
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player.x += 1
            elif keys[pygame.K_i]:
                KeyInputHandler.change_app_state(AppStates.IN_GAME_INVENTORY)
            elif keys[pygame.K_p]:
                KeyInputHandler.change_app_state(AppStates.IN_GAME_PAUSED)

        elif app_state == AppStates.IN_GAME_PAUSED:
            if keys[pygame.K_p]:
                KeyInputHandler.change_app_state(AppStates.IN_GAME_PLAY)

        elif app_state == AppStates.IN_GAME_INVENTORY:
            if keys[pygame.K_i]:
                KeyInputHandler.change_app_state(AppStates.IN_GAME_PLAY)
