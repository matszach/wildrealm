from PIL import Image
import pygame

TILE_SIZE = 16
BORDER_WIDTH = 1
FILE_EXTENSION = '.png'


class ImageLoader:

    @staticmethod
    def _get_image_at(image_set, x: int, y: int, img_size: int = TILE_SIZE):
        x = x * (img_size + BORDER_WIDTH)
        y = y * (img_size + BORDER_WIDTH)
        crop_area = (x, y, x + img_size, y + img_size)
        img = image_set.crop(crop_area)
        return pygame.image.fromstring(img.tobytes(), img.size, img.mode).convert_alpha()

    @staticmethod
    def _load_image_set(file_name):
        return Image.open(f'assets\\img\\{file_name}{FILE_EXTENSION}')

    ICON: object

    CREATURES: dict = {}

    FLOORS: dict = {}

    WALLS: dict = {}

    ITEMS: dict = {}

    @staticmethod
    def load():

        pygame.init()
        pygame.display.set_mode()

        # icon
        icon_image_set = ImageLoader._load_image_set('icon')
        ImageLoader.ICON = ImageLoader._get_image_at(icon_image_set, 0, 0)

        # creatures
        creatures_image_set = ImageLoader._load_image_set('creatures')
        ImageLoader.CREATURES['player'] = ImageLoader._get_image_at(creatures_image_set, 0, 0)

        # floors
        floors_image_set = ImageLoader._load_image_set('floor_tiles')
        ImageLoader.FLOORS['deep_water'] = ImageLoader._get_image_at(floors_image_set, 0, 0)
        ImageLoader.FLOORS['shallow_water'] = ImageLoader._get_image_at(floors_image_set, 1, 0)
        ImageLoader.FLOORS['sand'] = ImageLoader._get_image_at(floors_image_set, 2, 0)
        ImageLoader.FLOORS['grass'] = ImageLoader._get_image_at(floors_image_set, 3, 0)
        ImageLoader.FLOORS['surface_stone'] = ImageLoader._get_image_at(floors_image_set, 4, 0)
        ImageLoader.FLOORS['deep_stone'] = ImageLoader._get_image_at(floors_image_set, 5, 0)

        ImageLoader.FLOORS['stone_brick_floor'] = ImageLoader._get_image_at(floors_image_set, 0, 1)
        ImageLoader.FLOORS['plank_floor'] = ImageLoader._get_image_at(floors_image_set, 1, 1)

        # walls
        walls_image_set = ImageLoader._load_image_set('wall_tiles')
        ImageLoader.WALLS['tree'] = ImageLoader._get_image_at(walls_image_set, 0, 0)
        ImageLoader.WALLS['seaweed'] = ImageLoader._get_image_at(walls_image_set, 1, 0)
        ImageLoader.WALLS['berry_bush'] = ImageLoader._get_image_at(walls_image_set, 2, 0)

        ImageLoader.WALLS['surface_rock'] = ImageLoader._get_image_at(walls_image_set, 0, 1)
        ImageLoader.WALLS['deep_rock'] = ImageLoader._get_image_at(walls_image_set, 1, 1)
        ImageLoader.WALLS['copper_vein'] = ImageLoader._get_image_at(walls_image_set, 2, 1)
        ImageLoader.WALLS['iron_vein'] = ImageLoader._get_image_at(walls_image_set, 3, 1)
        ImageLoader.WALLS['silver_vein'] = ImageLoader._get_image_at(walls_image_set, 4, 1)
        ImageLoader.WALLS['gold_vein'] = ImageLoader._get_image_at(walls_image_set, 5, 1)

        ImageLoader.WALLS['wooden_chest'] = ImageLoader._get_image_at(walls_image_set, 0, 2)
        ImageLoader.WALLS['water_chest'] = ImageLoader._get_image_at(walls_image_set, 1, 2)
        ImageLoader.WALLS['magic_chest'] = ImageLoader._get_image_at(walls_image_set, 2, 2)

        ImageLoader.WALLS['stone_brick_wall'] = ImageLoader._get_image_at(walls_image_set, 0, 3)
        ImageLoader.WALLS['plank_wall'] = ImageLoader._get_image_at(walls_image_set, 1, 3)

        # items






