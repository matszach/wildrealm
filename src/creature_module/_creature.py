from src.map_module.worldmap import WorldMap
from src.map_module.tile_types.wall_tiles.list import WALL_TILES_BY_ID
from src.map_module.tile_types.floor_tiles.list import FLOOR_TILES_BY_ID
from src.threading_module.thread_manager import ThreadManager
import time
from src.game_core_module.app_states import AppStates


# base class
class Creature:

    MOVE_DIR_UP = 0
    MOVE_DIR_DOWN = 1
    MOVE_DIR_LEFT = 2
    MOVE_DIR_RIGHT = 3

    """
    movement handling
    """
    def move(self, direction: int):
        if self.movement_cooldown > 0:
            return
        if direction == Creature.MOVE_DIR_UP:
            if not Creature._can_move_to_tile(self.x, self.y - 1):
                return
            self.y -= 1
        elif direction == Creature.MOVE_DIR_DOWN:
            if not Creature._can_move_to_tile(self.x, self.y + 1):
                return
            self.y += 1
        elif direction == Creature.MOVE_DIR_LEFT:
            if not Creature._can_move_to_tile(self.x - 1, self.y):
                return
            self.x -= 1
        elif direction == Creature.MOVE_DIR_RIGHT:
            if not Creature._can_move_to_tile(self.x + 1, self.y):
                return
            self.x += 1
        self._start_movement_cooldown()

    @staticmethod
    def _can_move_to_tile(x: int, y: int) -> bool:
        wmap: WorldMap = Creature._get_game_state().world_map
        if 0 > x or 0 > y or x >= wmap.x_size or y >= wmap.y_size:
            return False
        return not WALL_TILES_BY_ID[wmap.walls[x, y]].blocks_movement

    def _get_speed_mod_for_floor(self, x: int, y: int) -> int:
        wmap: WorldMap = Creature._get_game_state().world_map
        floor_tile = FLOOR_TILES_BY_ID[wmap.floors[x, y]]
        if self.is_swimming and floor_tile.swimming:
            return 1
        return floor_tile.speed_mod

    def _calc_movement_cooldown(self, floods_speed_mod: float) -> int:
        return int(100/self.speed/floods_speed_mod)

    def _start_movement_cooldown(self):
        ThreadManager.start_daemon(self._movement_cooldown_thread)

    def _movement_cooldown_thread(self):
        mod = self._get_speed_mod_for_floor(self.x, self.y)
        self.movement_cooldown = self._calc_movement_cooldown(mod)
        while self.movement_cooldown > 0:
            time.sleep(0.01)
            if self._get_app_state() == AppStates.IN_GAME_PLAY:
                self.movement_cooldown -= 1

    def place_at(self, x: int, y: int):
        self.x = x
        self.y = y

    """
    health handling
    """
    def take_damage(self, damage: float):
        damage = damage - self.defense
        damage = damage if damage > 1 else 1
        self.curr_health -= damage

    def heal(self, healing: float):
        self.curr_health += healing
        self.curr_health = self.max_health if self.curr_health > self.max_health else self.curr_health

    def is_dead(self) -> bool:
        return self.curr_health <= 0

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

    # constructor
    def __init__(self, max_health: float = 100, defense: int = 0):

        # health and defense
        self.max_health: float = max_health
        self.curr_health: float = max_health
        self.defense: int = defense

        # movement
        self.speed: float = 10.0
        self.movement_cooldown: int = 0
        self.is_swimming: bool = False

        # creature's location
        self.x: int = 0
        self.y: int = 0


