"""
File Name: settings.py
Author: Tyler D. Collins
Date: 4/11/2026

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
        bg_file (Path): Path leading to the image file used as the background of
        the game window

        ship_file (Path): Path leading to the image file used as the ship/player
        ship_w (int): The relative width of the ship/player object on the game screen
        ship_h (int): The relative height of the ship/player object on the game screen
        ship_speed (int): The speed of the ship/player when moving up or down
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