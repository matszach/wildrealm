from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.display_module.gui.panel import InGameMenuPanel
from src.display_module.gui.big_text import BigText
from src.game_core_module.app_states import AppStates


class ConfirmExitView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        self.nodes.append(InGameMenuPanel(10, 10))

        self.nodes.append(BigText(13, 11, 9, 2, 'ARE YOU SURE ?'))

        # yes button
        yes_button = Button(13, 14, 9, 2, 'Yes', lambda: Game.set_app_state(AppStates.MAIN_MENU))
        yes_button.activate()
        self.nodes.append(yes_button)

        # no button
        no_button = Button(13, 17, 9, 2, 'No', lambda: Game.set_app_state(AppStates.IN_GAME_PAUSED))
        no_button.activate()
        self.nodes.append(no_button)
