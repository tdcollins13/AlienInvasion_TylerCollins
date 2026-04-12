"""
File Name: ship.py
Author: Tyler D. Collins
Date: 4/11/2026

Purpose: The purpose of this file is to create the Ship class/module that 
defines how the ship/player object is generated, its position and its behavior
"""

# Import Necessary Modules w/ workaround for circular imports
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:
    """Represents the ship/player object in the AlienInvasion game

    Attributes:
        game (AlienInvasion): Refers to the AlienInvasion game
        settings (Settings): Predefined specifications used to create the Ship
        screen (Surface): The image/space of the game screen
        boundaries (Rect): Coordinates/dimensions of the game screen boundaries
        image (Surface): The on-screen image of the ship/player
        rect (Rect): Coordinates/dimensions of the ship/player image
        y_coord (float): 'y' coordinate on game screen of top left corner of ship
        moving_up (bool): Indicates whether or not the ship is moving up
        moving_down (bool): Indicates whether or not the ship is moving down
    """

    def __init__(self, game: 'AlienInvasion'):

        # Attributes pertaining to game/screen
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load, scale & orient Ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h)
            )
        self.image = pygame.transform.rotate(self.image, 270)
        
        # Ship position at game start
        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft
        self.y_coord = float(self.rect.y)

        # Ship movement, initialized as stationary
        self.moving_up: bool = False
        self.moving_down: bool = False
    
    def update(self):
        # Updating ship position, restricting movement to within screen bounds
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y_coord -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y_coord += temp_speed

        self.rect.y = self.y_coord

    def draw(self):
        self.screen.blit(self.image, self.rect)