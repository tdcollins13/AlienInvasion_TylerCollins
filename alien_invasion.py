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
from settings import Settings

class AlienInvasion:
    """Represents the AlienInvasion game

    Attributes:
        settings (Settings): Predefined specifications used to generate the game
        screen : The screen/window generated to display the game
        bg : The image used as the background of the game screen
        running (bool): Indicates whether or not the game is currently running
        clock : Tracks the progression of time while the game is running
    """

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )
        self.running: bool = True
        self.clock = pygame.time.Clock()
    
    def run_game(self):
        # Game Loop
        while self.running == True:
            for event in pygame.event.get():

                # Ends game when game window is closed
                if event.type == pygame.QUIT:
                    self.running: bool = False
                    pygame.quit()
                    sys.exit()

            # Render updated frame/image at desired FPS
            self.screen.blit(self.bg, (0,0))
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)

# AlienInvasion game initialized when program is run
if __name__ == '__main__':
    pass
    ai = AlienInvasion()
    ai.run_game()