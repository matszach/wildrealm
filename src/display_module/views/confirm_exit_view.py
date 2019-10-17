from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.display_module.gui.panel import InGameMenuPanel
from src.display_module.gui.big_text import BigText
from src.game_core_module.app_states import AppStates


class ConfirmExitView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        self.nodes.append(InGameMenuPanel(8.5, 11.5))

        self.nodes.append(BigText(13, 9.5, 9, 2, 'ARE YOU'))
        self.nodes.append(BigText(13, 11, 9, 2, 'SURE ?'))

        # yes button
        yes_button = Button(12, 14, 11, 2, 'Yes', lambda: Game.set_app_state(AppStates.MAIN_MENU))
        yes_button.activate()
        self.nodes.append(yes_button)

        # no button
        no_button = Button(12, 17, 11, 2, 'No', lambda: Game.set_app_state(AppStates.IN_GAME_PAUSED))
        no_button.activate()
        self.nodes.append(no_button)
