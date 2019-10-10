from src.game_core_module.game_state.game_state import GameState
from src.map_module.map_builder.map_builder import MapBuilder
from src.creature_module.player import Player


class NewGameStarter:

    def new_game(self) -> GameState:
        # todo args etc here
        p = Player()
        p.move_to(100, 100)
        gs: GameState = GameState(p, self.builder.build(1024, 1024))
        return gs

    # constructor
    def __inti__(self):
        self.builder = MapBuilder()
