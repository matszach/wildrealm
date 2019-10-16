from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.game_core_module.app_states import AppStates


class MainMenuView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        # new world button
        start_new_game_button = Button(12, 9, 11, 2, 'Create new world',
                                       lambda: Game.set_app_state(AppStates.NEW_GAME_MENU))
        start_new_game_button.activate()
        self.nodes.append(start_new_game_button)

        # load game button
        load_game_button = Button(12, 12, 11, 2, 'Load game',
                                  lambda: Game.set_app_state(AppStates.LOAD_GAME_MENU))
        load_game_button.activate()
        self.nodes.append(load_game_button)
        
        # controls button
        controls_button = Button(12, 15, 11, 2, 'Controls',
                                 lambda: Game.set_app_state(AppStates.CONTROLS))
        controls_button.activate()
        self.nodes.append(controls_button)

        # about button
        about_button = Button(12, 18, 11, 2, 'About',
                              lambda: Game.set_app_state(AppStates.ABOUT))
        about_button.activate()
        self.nodes.append(about_button)
