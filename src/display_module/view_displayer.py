from src.game_core_module.app_states import AppStates
from src.display_module.views.view import View
from src.display_module.views.main_menu_view import MainMenuView
from src.display_module.views.about_view import AboutView
from src.display_module.views.load_game_view import LoadGameView
from src.display_module.views.new_game_view import NewGameView
from src.display_module.views.generating_world_view import GeneratingWorldView


class ViewDisplayer:

    """
    checks if the app state has been changed before drawing the view
    """
    def _app_state_changed(self, app_state: int):
        return self.current_app_state != app_state

    """
    matches the displayer view to the one required by new app state
    """
    def _match_view_to_state(self, app_state: int):
        if self.current_view:
            self.current_view.close()
        self.current_app_state = app_state
        self.current_view = self._get_view_by_app_state(app_state)

    @staticmethod
    def _get_view_by_app_state(app_state: int) -> View:
        if app_state == AppStates.MAIN_MENU:
            return MainMenuView()
        elif app_state == AppStates.ABOUT:
            return AboutView()
        elif app_state == AppStates.LOAD_GAME_MENU:
            return LoadGameView()
        elif app_state == AppStates.NEW_GAME_MENU:
            return NewGameView()
        elif app_state == AppStates.GENERATING_MAP:
            return GeneratingWorldView()

    """
    based on current game state displays the correct view
    """
    def display(self, surface, app_state: int):
        if self._app_state_changed(app_state):
            self._match_view_to_state(app_state)
        for node in self.current_view.nodes:
            node.display(surface)

    def __init__(self):

        # default values to overridden
        self.current_view: View = None
        self.current_app_state = -1
