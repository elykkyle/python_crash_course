import sys
import pygame
from random import randint
from droplet import Droplet


class Raindrops:
    """Class to manage overall program."""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Raindrops")
        self.droplets = pygame.sprite.Group()

        self._create_grid()

    def _create_grid(self):
        """Create the grid of raindrops."""
        droplet = Droplet(self)
        droplet_width, droplet_height = droplet.rect.size

        current_x, current_y = droplet_width / 2, droplet_height / 2
        while current_y < self.screen.get_height():
            while current_x < self.screen.get_width():
                self._create_drop(current_x, current_y)
                current_x += droplet_width * 1.5
            current_x = droplet_width / 2
            current_y += droplet_height * 1.5

    def _create_drop(self, x_position, y_position):
        rand = 0  # randint(-30, 30)
        new_droplet = Droplet(self)
        new_droplet.x = x_position + rand
        new_droplet.y = y_position + rand
        new_droplet.rect.x = x_position + rand
        new_droplet.rect.y = y_position + rand
        self.droplets.add(new_droplet)

    def _lower_drops(self):
        for droplet in self.droplets.sprites():
            droplet.rect.y += 1

    def run_prog(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 0, 0))
            self.droplets.draw(self.screen)
            self._lower_drops()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    rd = Raindrops()
    rd.run_prog()
