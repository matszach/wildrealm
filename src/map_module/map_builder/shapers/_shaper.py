from perlin import SimplexNoise


"""
Shapers use a Perlin noise generator to create smoothly transitioning areas.
"""


class Shaper:

    # constructor
    def __init__(self, noise_generator: SimplexNoise):
        self.noise_generator = noise_generator
