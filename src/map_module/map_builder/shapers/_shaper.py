from perlin import SimplexNoise


"""
Shapers use a Perlin noise generator to create smoothly transitioning areas.
"""


class Shaper:

    """
    :return message for the active world builder, describing the action of the shaper
    """
    @staticmethod
    def get_message() -> str:
        return '[default shaper message]'

    # constructor
    def __init__(self, noise_generator: SimplexNoise):
        self.noise_generator = noise_generator
