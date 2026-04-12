"""
File Name: alien_invasion.py
Author: Tyler D. Collins
Date: 4/11/2026

Purpose: This program is the main file in the 'AlienInvasion_TylerCollins'
repository, which contains the code that runs a complete 2D game using Pygame. 
This 'Alien Invasion' game features custom game mechanics and was built using a 
set of assets provided by GitHub user RedBeard41.
"""

# Import Necessary Modules
import sys
import pygame


class AlienInvasion:
    """Represents the AlienInvasion game

    Attributes:
    """

    def __init__(self):
        # Initialize game screen
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.running: bool = True
    
    def run_game(self):
        # Game Loop
        while self.running:
            for event in pygame.event.get():
                # Ends game when game window is closed
                if event.type == pygame.QUIT:
                    self.running: bool = False
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

# AlienInvasion game initialized when program is run
if __name__ == '__main__':
    pass
    ai = AlienInvasion()
    ai.run_game()