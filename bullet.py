"""
File Name: bullet.py
Author: Tyler D. Collins
Date: 4/19/2026

Purpose: The purpose of this file is to create the Bullet class/module that 
defines how bullets fired from the ship/player are generated, their position
and their movement behavior.
"""

# Import Necessary Modules w/ workaround for circular imports
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Represents a bullet/laser fired by the ship/player in the AlienInvasion 
    game

    Args:
        Sprite (Sprite): Represents group of bullet objects

    Attributes:
        screen (Surface): The image/space of the game screen
        settings (Settings): Module of predefined specifications used to create
        bullet sprites and define their behavior
        image (Surface): The on-screen image of the bullet sprite
        rect (Rect): Coordinates/dimensions of the bullet image on game screen
        x_coord (int): 'x' coordinate on the game screen of the top left corner 
        of the bullet
    """
    def __init__(self, game: 'AlienInvasion'):
        
        # Initialize attributes from Arsenal and AlienInvasion
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load, scale and orient bullet image
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
            )
        self.image = pygame.transform.rotate(self.image, 270)
        
        # Bullet position, appearing initially at front of ship when fired
        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright
        self.x_coord = int(self.rect.x)


    def update(self):
        """Update position of fired bullet(s) as they move horizontally across
        the screen"""
        self.x_coord += self.settings.bullet_speed
        self.rect.x = self.x_coord


    def draw_bullet(self):
        """Draw bullet image to game screen"""
        self.screen.blit(self.image, self.rect)