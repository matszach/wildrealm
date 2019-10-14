from src.game_core_module.game_state.game_state import GameState
from src.map_module.map_builder.map_builder import MapBuilder
from src.creature_module.player import Player


class NewGameStarter:

    def prepare_new_game(self):
        # TODO arguments here
        self.builder.build(256, 256)

    def is_ready(self):
        return self.builder.map_ready

    def get_prepared_game_state(self) -> GameState:
        # TODO player placing logic
        p: Player = Player()
        p.move_to(100, 100)
        return GameState(p, self.builder.wmap)

    def get_progress(self) -> tuple:
        return self.builder.message, self.builder.completion

    # constructor
    def __init__(self):
        self.builder = MapBuilder()

