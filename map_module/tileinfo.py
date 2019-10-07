
FLOOR_IDS = {
    # ID : (name, loaded image, map_color, speed_mod, requires_boat))
    0: ('deepWater', None, (0, 0, 80), 1.0,  True),
    1: ('shallowWater', None, (0, 0, 180), 0.5, False),
    2: ('sand', None, (180, 180, 0), 0.8, False),
    3: ('grass', None, (0, 180, 0), 1.0, False),
    4: ('surface_stone', None, (110, 110, 110), 1.0, False),
    5: ('deep_stone', None, (80, 80, 80), 1.0, False),

}

WALL_IDS = {
    # ID : (name, loaded image, map_color, TODO))
    0: ('air', None, False),
    1: ('tree', None, (0, 90, 0)),
    2: ('surface_rock', None, (40, 40, 40)),
    3: ('deep_rock', None, (20, 20, 20)),
    4: ('copper', None, (250, 120, 0)),
    5: ('iron', None, (190, 120, 50)),
    6: ('silver', None, (90, 90, 190)),
    7: ('gold', None, (250, 180, 0))
}
