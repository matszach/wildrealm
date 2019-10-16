import pygame


class ViewInfo:

    # default background color
    BACKGROUND_COLOR: tuple = (0, 0, 30)

    # window size in unit
    SIZE_UNITS_X: int = 35
    SIZE_UNITS_Y: int = 21

    # on-startup unit size
    DEFAULT_UNIT: float = 32.0

    # unit size - display unit of measure
    unit: float = DEFAULT_UNIT

    # display offsets for disproportionately
    offset_x: float = 0
    offset_y: float = 0

    # on-startup window size
    DEFAULT_WINDOW_SIZE: tuple = (int(SIZE_UNITS_X * DEFAULT_UNIT), int(SIZE_UNITS_Y * DEFAULT_UNIT))

    # current window size
    window_size: tuple = DEFAULT_WINDOW_SIZE

    """
    adjust the stored variables to match the current screen
    those will be used to draw on the game canvas
    """
    @staticmethod
    def adjust(event):
        ViewInfo.window_size = (event.w, event.h)
        ViewInfo.unit = min(event.w/ViewInfo.SIZE_UNITS_X, event.h/ViewInfo.SIZE_UNITS_Y)
        ViewInfo.offset_x = (event.w - (ViewInfo.unit * ViewInfo.SIZE_UNITS_X)) / 2
        ViewInfo.offset_y = (event.h - (ViewInfo.unit * ViewInfo.SIZE_UNITS_Y)) / 2

    """
    displays the usable window area as a rectangle
    """
    @staticmethod
    def display_usable_area(surface):
        pygame.draw.rect(surface, (100, 100, 100), (ViewInfo.offset_x, ViewInfo.offset_y,
                         (ViewInfo.unit * ViewInfo.SIZE_UNITS_X), (ViewInfo.unit * ViewInfo.SIZE_UNITS_Y)), 2)
