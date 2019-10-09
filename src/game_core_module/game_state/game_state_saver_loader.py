from src.game_core_module.game_state.game_state import GameState
import pickle


# saves / loads the game state
class GameStateSaverLoader:

    @staticmethod
    def save(gs: GameState, path: str):
        file = open(path, 'wb')
        pickle.dump(gs, file)

    @staticmethod
    def load(path: str) -> GameState:
        return pickle.load(path)
