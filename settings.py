"""
File Name: settings.py
Author: Tyler D. Collins
Date: 4/11/2026

Purpose: This file contains the 
"""
# Import Necessary Modules
from pathlib import Path


class Settings:
    """Represents the settings used in generating the AlienInvasion game

    Attributes:
        name (str): The name of the AlienInvasion game
        screen_w (int): The width of the game screen/window in __
        screen_h (int): The height of the game screen/window in ___
        FPS (int): The speed at which new frames for the game are drawn, in 
        frames per second
        bg_file (Path): Path leading to the image file used as the background of
        the game window
    """
    def __init__(self):
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1000
        self.screen_h: int = 600
        self.FPS: int = 60
        self.bg_file = Path.cwd() / 'Assets'/ 'images' / 'Starbasesnow.png'