"""
File Name: ship.py
Author: Tyler D. Collins
Date: 4/24/2026

Purpose: The purpose of this file is to create the Ship class/module that 
defines how the ship/player object is generated, its position and its 
movement behavior.
"""

# Import Necessary Modules w/ workaround for circular imports
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    """Represents the ship/player object in the AlienInvasion game

    Args:
        game (AlienInvasion): Refers to the AlienInvasion game
        arsenal (Arsenal): Represents the ship's ammo reserves

    Attributes:
        settings (Settings): Module of predefined specifications used to create 
            the Ship
        screen (Surface): The image/space of the game screen
        boundaries (Rect): Coordinates/dimensions of the game screen boundaries

        image (Surface): The on-screen image of the ship/player
        rect (Rect): Coordinates/dimensions of the ship/player image
        moving_up (bool): Indicates whether or not the ship is moving up
        moving_down (bool): Indicates whether or not the ship is moving down
        arsenal (Arsenal): Represents the ship's ammo reserves
    """
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
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
        
        # Ship positioning
        self.rect = self.image.get_rect()
        self._center_ship()

        # Ship movement, initialized as stationary
        self.moving_up: bool = False
        self.moving_down: bool = False

        # Ship arsenal
        self.arsenal = arsenal


    def _center_ship(self):
        """Position ship at middle of game screen's left edge at game 
        start/reset
        """
        self.rect.midleft = self.boundaries.midleft
        self.y_coord = int(self.rect.y)


    def update(self):
        """Updating ship movement and arsenal capacity"""
        self._update_ship_movement()
        self.arsenal.update_arsenal()


    def _update_ship_movement(self):
        """Updating ship position when ship is moved by player Movement is 
        restricted within screen bounds
        """
        # Flip movement direction based on which screen boundary is reached
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y_coord -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y_coord += temp_speed

        self.rect.y = self.y_coord


    def draw(self):
        """Draw ship image and arsenal capacity to game screen"""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)


    def fire(self):
        """Order new bullet to be fired when called"""
        return self.arsenal.fire_bullet()
    

    def check_collisions(self, other_group):
        """Resets ship position upon collision with an alien

        Args:
            other_group (Group): Alien fleet sprite group

        Returns:
            bool: Signals if/when a collision between an alien and the ship 
                occurs
        """
        # Resets ship position upon collision with an alien
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False