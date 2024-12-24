import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__ (self, ai_game):
        """Create a bullet object at the ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #erstellt ein Geschossrechteck bei (0, 0) und legt es dann in die richtige Position fest
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #speichert die positione des geschosses al Fließkommawert
        self.y = float(self.rect.y)

    def update(self):
        """Move the Bullet up the screen"""
        #aktualisiert die Fließkommawerte des Geschosses
        self.y -= self.settings.bullet_speed
        #aktualisiert die position des Rechtecks 
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the Bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
