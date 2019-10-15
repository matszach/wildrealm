from src.display_module.gui._gui_node import GuiNode
import pygame
from src.display_module.view_info import ViewInfo


class Button(GuiNode):

    def display(self, pygame_surface):
        u = ViewInfo.unit
        off_x = ViewInfo.offset_x
        off_y = ViewInfo.offset_y
        if self.pressed:
            rect = (off_x + (self.x_start + 0.05) * u,
                    off_y + (self.y_start + 0.05) * u,
                    (self.width - 0.1) * u,
                    (self.height - 0.1) * u)
            color = (100, 100, 130)
            font_size = u/1.22
        elif self.hover:
            rect = (off_x + (self.x_start - 0.05) * u,
                    off_y + (self.y_start - 0.05) * u,
                    (self.width + 0.1) * u,
                    (self.height + 0.1) * u)
            color = (100, 100, 170)
            font_size = u/1.18
        else:
            rect = (off_x + self.x_start * u,
                    off_y + self.y_start * u,
                    self.width * u,
                    self.height * u)
            color = (100, 100, 150)
            font_size = u/1.2

        pygame.draw.rect(pygame_surface, color, rect)

        font = pygame.font.Font('assets\\fonts\\menu_font.otf', int(font_size))
        txt_surf = font.render(self.text, True, (0, 0, 0))
        txt_rect = txt_surf.get_rect()
        txt_rect.center = (off_x + (self.x_start + self.width / 2) * u, off_y + (self.y_start + self.height / 2) * u)
        pygame_surface.blit(txt_surf, txt_rect)

    def __init__(self, pos_x: float = 0, pos_y: float = 0, width: float = 1, height: float = 1,
                 text: str = 'Button', action=lambda: None):
        GuiNode.__init__(self, pos_x, pos_y, width, height)
        self.text: str = text
        self.on_released = action
