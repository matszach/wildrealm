from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.display_module.gui.panel import InGameMenuPanel
from src.game_core_module.app_states import AppStates
from src.display_module.gui.big_text import BigText


class InGamePausedView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        self.nodes.append(InGameMenuPanel(7, 13))

        self.nodes.append(BigText(13, 8, 9, 2, 'PAUSED'))

        # save button
        save_button = Button(12, 11, 11, 2, 'Save', lambda: Game.set_app_state(AppStates.IN_GAME_SAVE_GAME))
        save_button.activate()
        self.nodes.append(save_button)

        # unpause button
        unpause_button = Button(12, 14, 11, 2, 'Unpause', lambda: Game.set_app_state(AppStates.IN_GAME_PLAY))
        unpause_button.activate()
        self.nodes.append(unpause_button)

        # exit button
        exit_button = Button(12, 17, 11, 2, 'Exit', lambda: Game.set_app_state(AppStates.IN_GAME_CONFIRM_EXIT))
        exit_button.activate()
        self.nodes.append(exit_button)
