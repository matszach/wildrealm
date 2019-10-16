from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.game_core_module.app_states import AppStates


class DefaultView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        # return button
        about_button = Button(13, 18, 9, 2, 'Return',
                              lambda: Game.set_app_state(AppStates.MAIN_MENU))
        about_button.activate()
        self.nodes.append(about_button)

