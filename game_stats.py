"""
File Name: game_stats.py
Author: Tyler D. Collins
Date: 4/23/2026

Purpose: The purpose of this file is to create the GameStats class/module that
tracks player statistics in the AlienInvasion game.
"""

# Import Necessary Modules w/ workaround for circular imports
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """Tracks player statistics in the AlienInvasion game

    Attributes:
        game (AlienInvasion):
        settings (Settings):
        max_score (int): Highest single game score during active game session, 
        resets when game window/program is closed


    """
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.max_score: int = 0
        

    def reset_stats(self):
        """Resets the score and game level when a new game begins"""
        self.ships_left = self.settings.starting_ship_count
        self.score: int = 0
        self.level: int = 1


    def update(self, collisions):
        """Updates score of active game. Also updates maximum score of the 
        active game session and all time high score when applicable.

        Args:
            collisions (dict): _description_
        """
        self._update_score(collisions)
        self._update_max_score()
    

    def _update_score(self, collisions: dict):
        """Updates the score of the active AlienInvasion game when aliens are
        destroyed

        Args:
            collisions (dict): 
        """
        for alien in collisions.values():
            self.score += self.settings.alien_points


    def _update_max_score(self):
        """Updates the maximum game score of the current session when the score
        of the active game surpasses the previous maximum game score"""
        if self.score > self.max_score:
            self.max_score = self.score


    def update_level(self):
        """Increases the level of the active game"""
        self.level += 1