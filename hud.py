"""
File Name: hud.py
Author: Tyler D. Collins
Date: 4/23/2026

Purpose:
"""

# Import Necessary Modules w/ workaround for circular imports
import pygame.font
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class HUD:
    """Facilitates the creation and maintenance of the AlienInvasion game HUD

    Attributes:

    """
    def __init__(self, game: 'AlienInvasion'):
        # Initialize Attributes from AlienInvasion
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats

        # Initialize HUD text font and boundary spacing
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.HUD_font_size)
        self.padding = 20

        # Update HUD
        self.update_scores()
        # self.setup_life_image()
        # self.update_level()

    def update_scores(self):
        """Updates the on-screen display of game score(s)"""
        self._update_score()
        self._update_hi_score()
        self._update_max_score()


    def _update_score(self):
        """Displays a live-updated score counter of the active game score"""
        # Format display of score text
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, 
            self.settings.text_color, None)
        
        # Place at top-middle of game screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = self.boundaries.midtop
        self.score_rect.top = self.padding
    

    def _update_hi_score(self):
        """Displays a live-updated score counter of the all-time local 
        hi-score"""
        # Format display of all-time local hi-score text
        hi_score_str = f'Hi-Score: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True, 
            self.settings.text_color, None)
        
        # Place in top-right corner of game screen
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.right = self.boundaries.right - self.padding
        self.hi_score_rect.top = self.padding


    def _update_max_score(self):
        """Displays a live-updated score counter of the hi-score of the current 
        game session"""
        # Format display of max current session score text
        max_score_str = f'PB Score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, 
            self.settings.text_color, None)
        
        # Place below hi-score
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.top = self.hi_score_rect.bottom + self.padding
        self.max_score_rect.right = self.boundaries.right - self.padding



    def draw(self):
        """Draws live score counters to HUD overlay on game screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.hi_score_image, self.hi_score_rect)