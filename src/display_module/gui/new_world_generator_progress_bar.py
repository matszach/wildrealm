from src.display_module.gui._gui_node import GuiNode
import pygame
from src.display_module.view_info import ViewInfo


class NewWorldGeneratorProgressBar(GuiNode):

    def display(self, pygame_surface):
        from src.game_core_module.game import Game

        u = ViewInfo.unit
        off_x = ViewInfo.offset_x
        off_y = ViewInfo.offset_y
        font_size = u/1.2
        font_color = (0, 0, 0)
        background_color = (30, 30, 60)
        bar_color = (50, 50, 130)

        progress = Game.new_game_starter.get_progress()

        pygame.draw.rect(pygame_surface, background_color, (off_x + self.x_start * u, off_y + self.y_start * u,
                                                            self.width * u, self.height * u))
        pygame.draw.rect(pygame_surface, bar_color, (off_x + self.x_start * u, off_y + self.y_start * u,
                                                     self.width * u * progress[1]/100, self.height * u))

        progress_text = f'{progress[1]}/100, {progress[0]}'

        font = pygame.font.Font('assets\\fonts\\menu_font.otf', int(font_size))
        txt_surf = font.render(progress_text, True, font_color)
        txt_rect = txt_surf.get_rect()
        txt_rect.center = (off_x + (self.x_start + self.width / 2) * u, off_y + (self.y_start + self.height / 2) * u)
        pygame_surface.blit(txt_surf, txt_rect)

    def __init__(self, pos_x: float = 0, pos_y: float = 0):
        GuiNode.__init__(self, pos_x, pos_y, 21, 3)
