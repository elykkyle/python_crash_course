import pygame
from pygame.sprite import Sprite


class Droplet(Sprite):
    """Class to manage single raindrop."""

    def __init__(self, rd_prog):
        super().__init__()

        self.screen = rd_prog.screen
        self.image = pygame.image.load("images/raindrop.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
