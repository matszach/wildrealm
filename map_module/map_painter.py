from PIL import Image
from map_module.worldmap import WorldMap
from map_module.tileinfo import FLOOR_IDS, WALL_IDS


class MapPainter:

    """
    Exports selected world map as a png file
    @:param wmap - exported world map
    @:param path - file output location
    """
    @staticmethod
    def paint_map(wmap: WorldMap, path: str):
        image = Image.new("RGB", (wmap.x_size, wmap.y_size), (0, 0, 0))
        pixels = image.load()
        for x in range(wmap.x_size):
            for y in range(wmap.y_size):
                color = WALL_IDS[wmap.walls[x, y]][2]
                if not color:
                    color = FLOOR_IDS[wmap.floors[x, y]][2]
                pixels[x, y] = color
        image.save(path)
