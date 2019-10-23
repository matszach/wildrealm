from src.threading_module.thread_manager import ThreadManager
from src.game_core_module.app_states import AppStates
import time


class Usable:

    use_range: int

    def use(self, x: int, y: int):
        pass

    def _calc_cooldown(self) -> int:
        pass

    def _start_cooldown(self):
        ThreadManager.start_daemon(self._cooldown_loop)

    def _cooldown_loop(self):
        self.curr_cooldown = self._calc_cooldown()
        while self.curr_cooldown > 0:
            time.sleep(0.01)
            if self._get_app_state() == AppStates.IN_GAME_PLAY:
                self.curr_cooldown -= 1

    """
    misc
    """
    @staticmethod
    def _get_game_state():
        from src.game_core_module.game import Game
        return Game.game_state

    @staticmethod
    def _get_app_state():
        from src.game_core_module.game import Game
        return Game.app_state

    def __init__(self):
        self.curr_cooldown: int = 0

