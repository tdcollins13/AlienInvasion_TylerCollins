"""
File Name: alien_fleet.py
Author: Tyler D. Collins
Date: 4/18/2026

Purpose: The purpose of this file is to create the AlienFleet class/module that
defines how the alien fleet structure is generated and ___
"""

# Import Necessary Modules w/ workaround for circular imports
import pygame
from typing import TYPE_CHECKING
from alien import Alien
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Represents the entire alien fleet in the AlienInvasion game

    Attributes
        game (AlienInvasion): Refers to the AlienInvasion game
        settings (Settings): Module of predefined specifications used to create 
        the aliens within the fleet
        fleet (Group): Manages group of alien sprites that make up the entire 
        alien fleet
        fleet_direction (int): Variable acting as the 'switch' that determines 
        whether the alien fleet is moving up or down on-screen
        fleet_shift_speed (int): The relative distance the alien fleet shifts
        towards the ship/player when the alien fleet hits a boundary and flips
        movement direction
    """
    def __init__(self, game: 'AlienInvasion'):

        # Initialize attributes from AlienInvasion
        self.game = game
        self.settings = game.settings

        # Create fleet Sprite Group
        self.fleet = pygame.sprite.Group()

        # Obtain fleet movement direction and shift speed from settings
        self.fleet_direction: int = self.settings.fleet_direction
        self.fleet_shift_speed: int = self.settings.fleet_shift_speed

        # Generate alien fleet by adding new alien objects to fleet Sprite Group
        self.create_fleet()

    def create_fleet(self):
        # Obtain screen and alien dimensions from settings
        alien_h: int = self.settings.alien_h
        alien_w: int = self.settings.alien_w
        screen_h: int = self.settings.screen_h
        screen_w: int = self.settings.screen_w

        # Calculate number of aliens that can fit in a single column of the 
        # fleet based on screen height, alien height and spacing between aliens
        fleet_h: int = self.calculate_fleet_size(alien_h, screen_h)
        fleet_vertical_space: int = (fleet_h * alien_h)
        y_offset = int((screen_h - fleet_vertical_space)//2)

        # Create new aliens below each other to form a column of aliens
        for row in range(fleet_h):
            current_y = (alien_h * row) + y_offset
            self._create_alien(current_y, (screen_w - alien_w - 10))

    def calculate_fleet_size(self, alien_h, screen_h):
        # Ensure fleet columns are filled with aliens but leaves space between 
        # fleet edges and screen edges for fleet to be able to move
        fleet_h = (screen_h // alien_h)
        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2
        return fleet_h
    
    def _create_alien(self, current_y: int, current_x: int):
        # Add all newly created aliens to the fleet Sprite Group
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def draw(self):
        # Draw an alien object to game screen for each alien in the fleet
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()