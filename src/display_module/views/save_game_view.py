from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.display_module.gui.panel import InGameMenuPanel
from src.game_core_module.app_states import AppStates
from src.display_module.gui.big_text import BigText


class SaveGameView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        self.nodes.append(InGameMenuPanel(1, 19))

        self.nodes.append(BigText(13, 2, 9, 2, 'SAVE YOUR'))
        self.nodes.append(BigText(13, 3.5, 9, 2, 'PROGRESS'))

        # save buttons
        save_button_1 = Button(13, 5, 9, 2, '[Empty]',
                               lambda: Game.save_game(1))
        if not Game.load_file_exists(1):
            save_button_1.text = f'Save state 1'
        save_button_1.activate()
        self.nodes.append(save_button_1)

        save_button_2 = Button(13, 8, 9, 2, '[Empty]',
                               lambda: Game.save_game(2))
        if not Game.load_file_exists(2):
            save_button_2.text = f'Save state 2'
        save_button_2.activate()
        self.nodes.append(save_button_2)

        save_button_3 = Button(13, 11, 9, 2, '[Empty]',
                               lambda: Game.save_game(3))
        if Game.load_file_exists(3):
            save_button_3.text = f'Save state 3'
        save_button_3.activate()
        self.nodes.append(save_button_3)

        save_button_4 = Button(13, 14, 9, 2, '[Empty]',
                               lambda: Game.save_game(4))
        if Game.load_file_exists(4):
            save_button_4.text = f'Save state 4'
        save_button_4.activate()
        self.nodes.append(save_button_4)
