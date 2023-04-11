import sys
import pygame
from pygame.sprite import Sprite
from star import Star


class StarGrid:
    """Overall class to manage star grid."""

    def __init__(self):
        """Initialize the screen and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Star Grid")

        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.stars = pygame.sprite.Group()

        self._create_grid()

    def _create_grid(self):
        """Create the grid of stars."""
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.screen_height - star_height * 2):
            while current_x < (self.screen_width - star_width):
                self._create_star(current_x, current_y)
                current_x += star_width

            current_x = star_width
            current_y += star_height

    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.y = y_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

        # def _create_star(self):

    def run_prog(self):
        """Start main loop for program."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.stars.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    sg = StarGrid()
    sg.run_prog()
