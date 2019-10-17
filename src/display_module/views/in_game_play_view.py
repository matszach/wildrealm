from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.game_core_module.app_states import AppStates


class InGamePlayView(View):

    def initiate(self):
        from src.game_core_module.game import Game


