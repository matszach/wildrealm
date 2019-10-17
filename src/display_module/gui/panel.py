from src.display_module.gui._gui_node import GuiNode
import pygame
from src.display_module.view_info import ViewInfo


class Panel(GuiNode):

    def display(self, pygame_surface):

        u = ViewInfo.unit
        off_x = ViewInfo.offset_x
        off_y = ViewInfo.offset_y
        background_color = (30, 30, 60)
        border_color = (20, 20, 50)
        border_width = int(u/5)

        pygame.draw.rect(pygame_surface, background_color, (off_x + self.x_start * u, off_y + self.y_start * u,
                                                            self.width * u, self.height * u))
        pygame.draw.rect(pygame_surface, border_color, (off_x + self.x_start * u, off_y + self.y_start * u,
                                                        self.width * u, self.height * u), border_width)


class InGameMenuPanel(Panel):

    def __init__(self, y: float, height: float):
        Panel.__init__(self, 10, y, 15, height)
