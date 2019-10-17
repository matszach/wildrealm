from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.game_core_module.app_states import AppStates


class LoadGameView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        # load state buttons
        load_button_1 = Button(12, 3, 11, 2, f'Save state 1',
                               lambda: Game.load_game(1))
        if Game.load_file_exists(1):
            load_button_1.activate()
        self.nodes.append(load_button_1)
        load_button_2 = Button(12, 6, 11, 2, f'Save state 2',
                               lambda: Game.load_game(2))
        if Game.load_file_exists(2):
            load_button_2.activate()
        self.nodes.append(load_button_2)
        load_button_3 = Button(12, 9, 11, 2, f'Save state 3',
                               lambda: Game.load_game(3))
        if Game.load_file_exists(3):
            load_button_3.activate()
        self.nodes.append(load_button_3)
        load_button_4 = Button(12, 12, 11, 2, f'Save state 4',
                               lambda: Game.load_game(4))
        if Game.load_file_exists(4):
            load_button_4.activate()
        self.nodes.append(load_button_4)
        load_button_5 = Button(12, 15, 11, 2, f'Save state 5',
                               lambda: Game.load_game(5))
        if Game.load_file_exists(5):
            load_button_5.activate()
        self.nodes.append(load_button_5)

        # return button
        return_button = Button(13, 18, 9, 2, 'Return',
                               lambda: Game.set_app_state(AppStates.MAIN_MENU))
        return_button.activate()
        self.nodes.append(return_button)

