from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.display_module.gui.panel import InGameMenuPanel
from src.game_core_module.app_states import AppStates
from src.display_module.gui.big_text import BigText


class SaveGameView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        self.nodes.append(InGameMenuPanel(1, 19))

        self.nodes.append(BigText(13, 2, 9, 2, 'SAVE YOUR GAME'))

        # save buttons
        save_button_1 = Button(12, 5, 11, 2, '[Empty]', lambda: Game.save_game(1))
        if Game.load_file_exists(1):
            save_button_1.text = f'Saved state 1'
        save_button_1.activate()
        self.nodes.append(save_button_1)

        save_button_2 = Button(12, 8, 11, 2, '[Empty]', lambda: Game.save_game(2))
        if Game.load_file_exists(2):
            save_button_2.text = f'Saved state 2'
        save_button_2.activate()
        self.nodes.append(save_button_2)

        save_button_3 = Button(12, 11, 11, 2, '[Empty]', lambda: Game.save_game(3))
        if Game.load_file_exists(3):
            save_button_3.text = f'Saved state 3'
        save_button_3.activate()
        self.nodes.append(save_button_3)

        save_button_4 = Button(12, 14, 11, 2, '[Empty]', lambda: Game.save_game(4))
        if Game.load_file_exists(4):
            save_button_4.text = f'Saved state 4'
        save_button_4.activate()
        self.nodes.append(save_button_4)

        # return button
        return_button = Button(13, 17, 9, 2, 'Return', lambda: Game.set_app_state(AppStates.IN_GAME_PAUSED))
        return_button.activate()
        self.nodes.append(return_button)
