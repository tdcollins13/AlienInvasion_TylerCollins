"""
File Name: settings.py
Author: Tyler D. Collins
Date: 4/18/2026

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

        bullet_file (Path): Path of the image file used as the bullets/
        lasers fired by the ship/player
        laser_sound (Path): Path of the audio file used for ship laser fire
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
    """

    def __init__(self):

        # Game screen/window settings
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1000
        self.screen_h: int = 600
        self.FPS: int = 60
        self.bg_file: Path = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        # Ship settings
        self.ship_file: Path = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w: int = 40
        self.ship_h: int = 60
        self.ship_speed: int = 3

        # Bullet settings
        self.bullet_file: Path = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound: Path = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed: int = 7
        self.bullet_w: int = 25
        self.bullet_h: int = 80
        self.bullet_amount: int = 5

        # Alien settings
        self.alien_file: Path = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w: int = 30
        self.alien_h: int = 30
        self.fleet_speed: int = 2