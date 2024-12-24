class Settings():
    """A class to store all stttings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings."""
        # Bildschrirmeinstellungen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Schiffseinstellungen
        self.ship_limit = 3

        #Geschosseinstellungen
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Invasionsschiffeinstellungen
        self.fleet_drop_speed = 10

        #stärke der Beschleunigung des spiels
        self.speedup_scale = 1.1

        #stärke der Punktebewertung bei Treffern
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 2
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        #der wert 1 für fleet_direction bedeutet "nach rechts", -1 "nach links"
        self.fleet_direction = 1

        #Punktewertung
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
