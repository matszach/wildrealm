from PIL import Image
from src.map_module.worldmap import WorldMap
from src.map_module.tile_types.floor_tiles.list import FLOOR_TILES_BY_ID
from src.map_module.tile_types.wall_tiles.list import WALL_TILES_BY_ID


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
                color = WALL_TILES_BY_ID[wmap.walls[x, y]].color
                if not color:
                    color = FLOOR_TILES_BY_ID[wmap.floors[x, y]].color
                pixels[x, y] = color
        image.save(path)
