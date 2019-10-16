from src.game_core_module.app_states import AppStates
from src.game_core_module.game_state.game_state import GameState
import pygame


class KeyInputHandler:

    """
    handles user input based on app state
    """
    @staticmethod
    def handle(app_state: int, game_state: GameState):

        if app_state == AppStates.IN_GAME_PLAY:
            keys = pygame.key.get_pressed()
            player = game_state.player
            if keys[pygame.K_w]:
                player.y -= 1
            elif keys[pygame.K_s]:
                player.y += 1
            elif keys[pygame.K_a]:
                player.x -= 1
            elif keys[pygame.K_d]:
                player.x += 1
