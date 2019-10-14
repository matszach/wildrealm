import pygame
import time
from src.threading_module.thread_manager import ThreadManager
from src.display_module.view_info import ViewInfo


# parent class to all gui elements such as buttons or decorations
class GuiNode:

    """
    displays the node on pygame's surface
    """
    def display(self, pygame_surface):
        if not self.hidden:
            self._draw_on_surface(pygame_surface)

    def _draw_on_surface(self, pygame_surface):
        pass

    """
    starts/ends the listening thread
    """
    def activate(self):
        self.disabled = False
        ThreadManager.start_daemon(self._listen())

    def deactivate(self):
        self.disabled = True

    def _listen(self):
        while not self.disabled:
            time.sleep(0.05)
            if self._is_mouse_on():
                self.on_while_hover()
                if not self.hover:
                    self.on_mouse_in()
                    self.hover = True
                if self._is_mouse_pressed():
                    self.pressed = True
                    self.on_pressed()
                else:
                    self.pressed = False
                    self.on_released()
            else:
                self.hover = False
                self.pressed = False

    """
    mouse status checking
    """
    def _is_mouse_on(self):
        pos = pygame.mouse.get_pos()
        mouse_x = (pos[0] - ViewInfo.offset_x)/ViewInfo.unit
        mouse_y = (pos[1] - ViewInfo.offset_y)/ViewInfo.unit
        return self.x_start < mouse_x < self.x_end and self.y_start < mouse_y < self.y_end

    @staticmethod
    def _is_mouse_pressed():
        return pygame.mouse.get_pressed[0] == 1

    # constructor
    def __init__(self, pos_x: float = 0, pos_y: float = 0, width: float = 1, height: float = 1):

        # values in ViewInfo units
        self.x_start: float = pos_x
        self.y_start: float = pos_y
        self.x_end: float = pos_x + width
        self.y_end: float = pos_y + height

        # mouse states
        self.hidden: bool = False
        self.disabled: bool = False
        self.pressed: bool = False
        self.hover: bool = False

        # element actions
        self.on_mouse_in = lambda: None
        self.on_mouse_out = lambda: None
        self.on_while_hover = lambda: None
        self.on_pressed = lambda: None
        self.on_released = lambda: None
