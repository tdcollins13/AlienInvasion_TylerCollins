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

        # Calculate number of aliens to fit in each column and row of fleet
        fleet_h, fleet_w = self.calculate_fleet_size(alien_h, screen_h, 
            alien_w, screen_w)
        
        # Calculate spacing between places within fleet columns and rows
        y_offset, x_offset = self.calculate_offsets(alien_h, alien_w, screen_h, 
            screen_w, fleet_h, fleet_w)
        
        # Generate fleet structure
        self._create_rectangle_fleet(alien_h, alien_w, fleet_h, fleet_w, 
            y_offset, x_offset, screen_w)


    def _create_rectangle_fleet(self, alien_h, alien_w, fleet_h, fleet_w, 
        y_offset, x_offset, screen_w):
        # Create new aliens that form an array/fleet of aliens
        for col in range(fleet_w):
            for row in range(fleet_h):
                current_y = (alien_h * row) + y_offset
                current_x = screen_w - ((alien_w * col) + x_offset)

                # Remove aliens in even rows & columns, adding spaces between 
                # aliens of the same row or column
                if row % 2 == 0 or col % 2 == 0:
                    continue
                self._create_alien(current_y, current_x)


    def calculate_offsets(self, alien_h, alien_w, screen_h, screen_w, 
        fleet_h, fleet_w):
        # Calculate vertical and horizontal dimensions of space filled by fleet
        half_screen: int = (screen_w // 2)
        fleet_vertical_space: int = (fleet_h * alien_h)
        fleet_horizontal_space: int = (fleet_w * alien_w)

        # Determine spacing between aliens in fleet rows and columns
        y_offset = int((screen_h - fleet_vertical_space)//2)
        x_offset = int((half_screen - fleet_horizontal_space)//2)

        return y_offset, x_offset


    def calculate_fleet_size(self, alien_h, screen_h, alien_w, screen_w):
        # Ensure fleet columns and rows are filled with max number of aliens for
        # the allotted space for the alien fleet upon start of level
        fleet_h = (screen_h // alien_h)
        fleet_w = ((screen_w / 2)//alien_w)

        # Find max # of aliens to fit in fleet columns
        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        # Find max # of aliens to fit in fleet rows
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        return int(fleet_h), int(fleet_w)

    
    def _create_alien(self, current_y: int, current_x: int):
        # Add all newly created aliens to the fleet Sprite Group
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    
    def _check_fleet_edges(self):
        # Flip direction of alien movement when screen boundary is reached
        alien: 'Alien'
        for alien in self.fleet:
            if alien.check_edges() == True:
                self._shift_alien_fleet()
                self.fleet_direction *= -1
                break
    

    def _shift_alien_fleet(self):
        # Shift alien fleet closer to ship when screen boundary is reached
        for alien in self.fleet:
            alien.x_coord -= self.fleet_shift_speed


    def update_fleet(self):
        # Updating fleet position and movement
        self._check_fleet_edges()
        self.fleet.update()


    def draw(self):
        # Draw an alien object to game screen for each alien in the fleet
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()


    def check_collisions(self, other_group):
        # Checks for collisions between laser and alien sprites, removing 
        # those that have collided from their respective groups
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)


    def check_fleet_reach_end(self):
        # Checks whether alien fleet has reached the screen edge behind the ship
        alien: 'Alien'
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False
    

    def check_destroyed_status(self):
        # Checks if entire alien fleet has been destroyed
        return not self.fleet