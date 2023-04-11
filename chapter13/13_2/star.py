import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Class to represent a single star."""

    def __init__(self, sg_prog):
        super().__init__()
        self.screen = sg_prog.screen

        self.image = pygame.image.load("images/star.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
