from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.game_core_module.app_states import AppStates


class LoadGameView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        # save state buttons
        for i in range(1, 5):
            load_button = Button(12, 3 + i * 3, 11, 2, f'Save state {i}',
                                 lambda: Game.load_game(i))
            if Game.load_file_exists(i):
                load_button.activate()
            self.nodes.append(load_button)

        # return button
        about_button = Button(13, 18, 9, 2, 'Return',
                              lambda: Game.set_app_state(AppStates.MAIN_MENU))
        about_button.activate()
        self.nodes.append(about_button)

