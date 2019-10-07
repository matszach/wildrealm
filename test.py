from map_module.map_builder.map_builder import MapBuilder
from map_module.map_painter import MapPainter

mb = MapBuilder()
wm = mb.build()
MapPainter.paint_map(wm, 'map.png')


