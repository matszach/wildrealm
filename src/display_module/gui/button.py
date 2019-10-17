from src.display_module.gui._gui_node import GuiNode
import pygame
from src.display_module.view_info import ViewInfo


class Button(GuiNode):

    def display(self, pygame_surface):
        u = ViewInfo.unit
        off_x = ViewInfo.offset_x
        off_y = ViewInfo.offset_y

        if self.disabled:
            rect = (off_x + self.x_start * u, off_y + self.y_start * u,
                    self.width * u, self.height * u)
            color_button_bg = (80, 80, 100)
            color_button_border = (50, 50, 70)
            font_size = u / 1.2
            font_color = (30, 30, 30)
        elif self.pressed:
            rect = (off_x + (self.x_start + 0.05) * u, off_y + (self.y_start + 0.05) * u,
                    (self.width - 0.1) * u, (self.height - 0.1) * u)
            color_button_bg = (100, 100, 130)
            color_button_border = (70, 70, 100)
            font_size = u/1.22
            font_color = (0, 0, 10)
        elif self.hover:
            rect = (off_x + (self.x_start - 0.05) * u, off_y + (self.y_start - 0.05) * u,
                    (self.width + 0.1) * u, (self.height + 0.1) * u)
            color_button_bg = (100, 100, 170)
            color_button_border = (70, 70, 140)
            font_size = u/1.18
            font_color = (0, 0, 30)
        else:
            rect = (off_x + self.x_start * u, off_y + self.y_start * u,
                    self.width * u, self.height * u)
            color_button_bg = (100, 100, 150)
            color_button_border = (70, 70, 120)
            font_size = u/1.2
            font_color = (0, 0, 20)

        border_width = int(u/5)

        pygame.draw.rect(pygame_surface, color_button_bg, rect)
        pygame.draw.rect(pygame_surface, color_button_border, rect, border_width)

        font = pygame.font.Font('assets\\fonts\\menu_font.otf', int(font_size))
        txt_surf = font.render(self.text, True, font_color)
        txt_rect = txt_surf.get_rect()
        txt_rect.center = (off_x + (self.x_start + self.width / 2) * u, off_y + (self.y_start + self.height / 2) * u)
        pygame_surface.blit(txt_surf, txt_rect)

    def __init__(self, pos_x: float = 0, pos_y: float = 0, width: float = 1, height: float = 1,
                 text: str = 'Button', action=lambda: None):
        GuiNode.__init__(self, pos_x, pos_y, width, height)
        self.text: str = text
        self.on_released = action
