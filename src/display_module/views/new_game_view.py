from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.game_core_module.app_states import AppStates


class NewGameView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        # new game buttons
        small_world_button = Button(12, 9, 11, 2, f'Small [256x256]',
                                    lambda: Game.start_new_game(256))
        small_world_button.activate()
        self.nodes.append(small_world_button)
        medium_world_button = Button(12, 12, 11, 2, f'Medium [512x512]',
                                     lambda: Game.start_new_game(512))
        medium_world_button.activate()
        self.nodes.append(medium_world_button)
        large_world_button = Button(12, 15, 11, 2, f'Large [1024x1024]',
                                    lambda: Game.start_new_game(1024))
        large_world_button.activate()
        self.nodes.append(large_world_button)

        # return button
        return_button = Button(13, 18, 9, 2, 'Return',
                               lambda: Game.set_app_state(AppStates.MAIN_MENU))
        return_button.activate()
        self.nodes.append(return_button)

