from src.map_module.map_builder.map_builder import MapBuilder
from src.map_module.map_painter import MapPainter

# example maps
mb = MapBuilder()
MapPainter.paint_map(mb.build(128, 128), 'out\\example_maps\\map128.png')
MapPainter.paint_map(mb.build(256, 256), 'out\\example_maps\\map256.png')
MapPainter.paint_map(mb.build(512, 512), 'out\\example_maps\\map512.png')
MapPainter.paint_map(mb.build(1024, 1024), 'out\\example_maps\\map1024.png')
MapPainter.paint_map(mb.build(2048, 2048), 'out\\example_maps\\map2048.png')


