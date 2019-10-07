from map_module.worldmap import WorldMap
import pickle


# saves / loads the WorldMap
class MapSaverLoader:

    @staticmethod
    def save(wmap: WorldMap, path: str):
        file = open(path, 'wb')
        pickle.dump(wmap, file)

    @staticmethod
    def load(path: str) -> WorldMap:
        return pickle.load(path)
