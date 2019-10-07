from map_module.map_builder.map_builder import MapBuilder
from map_module.map_painter import MapPainter

# example maps
mb = MapBuilder()
MapPainter.paint_map(mb.build(256, 256), 'map_module\\example_maps\\map256.png')
MapPainter.paint_map(mb.build(512, 512), 'map_module\\example_maps\\map512.png')
MapPainter.paint_map(mb.build(1024, 1024), 'map_module\\example_maps\\map1024.png')


