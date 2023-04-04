import sys
import pygame


class SidewaysShooter():
    """Class to manage Sideways Shooter game assets and behavior"""

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")
