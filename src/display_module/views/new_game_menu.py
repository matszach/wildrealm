from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.game_core_module.app_states import AppStates


class NewGameView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        # save state buttons
        for i, size in enumerate([('Small', 256), ('Medium', 512), ('Large', 1024)]):
            new_world_button = Button(12, 9 + i * 3, 11, 2, f'{size[0]} [{size[1]}x{size[1]}]',
                                      lambda: Game.start_new_game(size[1]))
            new_world_button.activate()
            self.nodes.append(new_world_button)

        # return button
        about_button = Button(13, 18, 9, 2, 'Return',
                              lambda: Game.set_app_state(AppStates.MAIN_MENU))
        about_button.activate()
        self.nodes.append(about_button)

