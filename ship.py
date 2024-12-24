import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Plaziert ein neues Schiff mittig am unteren Bildschirmrand
        self.rect.midbottom = self.screen_rect.midbottom

        #Speichert einen Fließkommawert für den exakten Schiffsmittelpunkt
        self.x = float(self.rect.x)

        #Movement flag; ; beginnen mit einem unbewegten schiff
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement flag"""
        #aktualisiert den wert für den Mittelpunkt des schiffes, nicht des Rechtecks
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Aktualisiert das rect-Onjekt auf der Grundlage von self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)