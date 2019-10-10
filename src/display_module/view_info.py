

class ViewInfo:

    # default background color
    BACKGROUND_COLOR: tuple = (0, 0, 0)

    # window size in unit
    SIZE_UNITS_X: int = 30
    SIZE_UNITS_Y: int = 20

    # on-startup unit size
    DEFAULT_UNIT: float = 32.0

    # unit size - display unit of measure
    unit: float = DEFAULT_UNIT

    # on-startup window size
    DEFAULT_WINDOW_SIZE: tuple = (int(SIZE_UNITS_X * DEFAULT_UNIT), int(SIZE_UNITS_Y * DEFAULT_UNIT))

    # current window size
    window_size: tuple = DEFAULT_WINDOW_SIZE

    @staticmethod
    def adjust(event):
        ViewInfo.window_size = (event.w, event.h)
        ViewInfo.unit = min(event.w/ViewInfo.SIZE_UNITS_X, event.h/ViewInfo.SIZE_UNITS_Y)

