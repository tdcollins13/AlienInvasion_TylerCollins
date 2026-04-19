"""
File Name: game_stats.py
Author: Tyler D. Collins
Date: 4/18/2026

Purpose: The purpose of this file is to create the GameStats class/module that
tracks player statistics in the AlienInvasion game.
"""

class GameStats():
    """Tracks player statistics in the AlienInvasion game

    Attributes:
        ships_left (int): The number of lives/ships the player has left
    """
    def __init__(self, ship_limit: int):
        self.ships_left = ship_limit