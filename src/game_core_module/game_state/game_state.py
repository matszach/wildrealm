from src.map_module.worldmap import WorldMap
from src.creature_module.player import Player


class GameState:

    def __init__(self, player: Player, wmap: WorldMap):

        # player character data
        self.player: Player = player

        # creatures actively taking actions/moving
        self.active_creatures = []

        # creatures waiting to go active or to be despawned
        self.dormant_creatures = []

        # world map data
        self.world_map: WorldMap = wmap

