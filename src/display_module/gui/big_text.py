from src.display_module.gui._gui_node import GuiNode
import pygame
from src.display_module.view_info import ViewInfo


class BigText(GuiNode):

    def display(self, pygame_surface):

        u = ViewInfo.unit
        off_x = ViewInfo.offset_x
        off_y = ViewInfo.offset_y

        font_size = u / 0.7
        font_color = (235, 235, 255)

        font = pygame.font.Font('assets\\fonts\\menu_font.otf', int(font_size))
        txt_surf = font.render(self.text, True, font_color)
        txt_rect = txt_surf.get_rect()
        txt_rect.center = (off_x + (self.x_start + self.width / 2) * u, off_y + (self.y_start + self.height / 2) * u)
        pygame_surface.blit(txt_surf, txt_rect)

    def __init__(self, pos_x: float = 0, pos_y: float = 0, width: float = 1, height: float = 1, text: str = 'Text'):
        GuiNode.__init__(self, pos_x, pos_y, width, height)
        self.text: str = text
