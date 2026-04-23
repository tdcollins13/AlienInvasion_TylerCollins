"""
File Name: settings.py
Author: Tyler D. Collins
Date: 4/23/2026

Purpose: The purpose of this file is to create the Settings class/module that 
contains a set of specifications to be used in the creation of the 
AlienInvasion game.
"""

# Import Necessary Modules
from pathlib import Path


class Settings:
    """Represents the settings used in generating the AlienInvasion game

    Attributes:
        name (str): The name of the AlienInvasion game
        screen_w (int): The relative width of the game screen/window
        screen_h (int): The relative height of the game screen/window
        FPS (int): The speed at which new frames for the game are drawn, in 
        frames per second
        bg_file (Path): Path of the image file used as the background of the 
        game window

        ship_file (Path): Path of to the image file used as the ship/player
        ship_w (int): The relative width of the ship/player object on the game 
        screen
        ship_h (int): The relative height of the ship/player object on the game 
        screen
        ship_speed (int): The speed of the ship/player when moving up or down
        starting_ship_count (int): The number of lives/ships the player has left

        bullet_file (Path): Path of the image file used as the bullets/
        lasers fired by the ship/player
        laser_sound (Path): Path of the audio file used for ship laser fire
        impact_sound (Path): Path of the audio file used for laser collisions 
        with aliens
        bullet_speed (int): The speed of a bullet/laser when moving across the 
        screen
        bullet_w (int): The relative width of the bullet/laser object on the 
        game screen
        bullet_h (int): The relative height of the bullet/laser object on the 
        game screen
        bullet_amount (int): The maximum number of bullets/lasers the 
        ship/player can have in their arsenal at any time

        alien_file (Path): Path of the image file used to depict an alien object
        alien_w (int): Refers to the relative width of an individual alien 
        object
        alien_h (int): Refers to the relative height of an individual alien 
        object
        fleet_speed (int): The speed of the alien fleet when moving on-screen
        fleet_direction (int): Variable acting as the 'switch' that determines 
        whether the alien fleet is moving up or down on-screen
        fleet_shift_speed (int): The relative distance the alien fleet shifts
        towards the ship/player when the alien fleet hits a boundary and flips
        movement direction

        *****FINISH/EDIT ATTRIBUTES*****

    """

    def __init__(self):

        # Game screen/window settings
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1000
        self.screen_h: int = 600
        self.FPS: int = 60
        self.bg_file: Path = (Path.cwd() / 'Assets' / 'images' / 
            'Starbasesnow.png')

        # Ship settings
        self.ship_file: Path = (Path.cwd() / 'Assets' / 'images' / 
            'ship2(no bg).png')
        self.ship_w: int = 40
        self.ship_h: int = 60
        self.starting_ship_count: int = 3

        # Bullet settings
        self.bullet_file: Path = (Path.cwd() / 'Assets' / 'images' / 
            'laserBlast.png')
        self.laser_sound: Path = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound: Path = (Path.cwd() / 'Assets' / 'sound' / 
            'impactSound.mp3')
        self.bullet_w: int = 25
        self.bullet_h: int = 80
        self.bullet_amount: int = 5

        # Alien settings
        self.alien_file: Path = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w: int = 30
        self.alien_h: int = 30
        self.fleet_direction: int = 1
        self.fleet_shift_speed: int = 30

        # Button settings
        self.button_w: int = 200
        self.button_h: int = 60
        self.button_color: tuple = (194,2,2)

        # Font settings
        self.text_color: tuple = (255,255,255)
        self.button_font_size: int = 40
        self.HUD_font_size: int = 15
        self.font_file: Path = (Path.cwd() / 'Assets' / 'Fonts' / 
            'Silkscreen' / 'Silkscreen-Bold.ttf')
        

    def initialize_dynamic_settings(self):
        """Initializes settings corresponding to the speed of the player and 
        enemies that determine the difficulty of gameplay"""
        self.difficulty_scale: float = 1.2
        self.ship_speed: int = 5
        self.bullet_speed: int = 7
        self.fleet_speed: int = 1
        self.fleet_drop_speed: int = 30
        self.alien_points: int = 100

    
    def increase_difficulty(self):
        """Increases the game's difficulty by changing the sizes and/or speeds 
        of objects during gameplay

        Args:
            level (int): The current level of the active AlienInvasion game
        """
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale

        #BOSS LEVELS: Changes to gameplay ocurring every 5 levels
        #if level % 5 == 0: