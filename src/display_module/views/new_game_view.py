from src.display_module.views.view import View
from src.display_module.gui.button import Button
from src.game_core_module.app_states import AppStates


class NewGameView(View):

    def initiate(self):
        from src.game_core_module.game import Game

        # new game buttons
        tiny_world_button = Button(12, 6, 11, 2, f'Tiny [256x256]',
                                   lambda: Game.start_new_game(256))
        tiny_world_button.activate()
        self.nodes.append(tiny_world_button)
        small_world_button = Button(12, 9, 11, 2, f'Small [512x512]',
                                    lambda: Game.start_new_game(512))
        small_world_button.activate()
        self.nodes.append(small_world_button)
        medium_world_button = Button(12, 12, 11, 2, f'Medium [1024x1024]',
                                     lambda: Game.start_new_game(1024))
        medium_world_button.activate()
        self.nodes.append(medium_world_button)
        large_world_button = Button(12, 15, 11, 2, f'Large [2048x2048]',
                                    lambda: Game.start_new_game(2048))
        large_world_button.activate()
        self.nodes.append(large_world_button)
        # huge_world_button = Button(12, 15, 11, 2, f'Huge [4096x4096]',
        #                            lambda: Game.start_new_game(4096))
        # huge_world_button.activate()
        # self.nodes.append(huge_world_button)

        # return button
        return_button = Button(13, 18, 9, 2, 'Return',
                               lambda: Game.set_app_state(AppStates.MAIN_MENU))
        return_button.activate()
        self.nodes.append(return_button)

