class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 16, 33)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (80, 80, 80)
        self.bullets_allowed = 5
