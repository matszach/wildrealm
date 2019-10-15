from src.display_module.views.view import View
from src.display_module.gui.new_world_generator_progress_bar import NewWorldGeneratorProgressBar


class GeneratingWorldView(View):

    def initiate(self):
        self.nodes.append(NewWorldGeneratorProgressBar(7, 8))
