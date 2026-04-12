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
from ship import Ship

class AlienInvasion:
    """Represents the AlienInvasion game

    Attributes:
        settings (Settings): Predefined specifications used to generate the game
        screen (Surface): The screen/window generated to display the game
        bg (Surface): The image used as the background of the game screen
        running (bool): Indicates whether or not the game is currently running
        clock (Clock): Tracks the progression of time while the game is running
        ship (Ship): The ship/player object being used in the game
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
        self.ship = Ship(self)
    
    def run_game(self):
        # Game Loop
        while self.running == True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        for event in pygame.event.get():
            # Ends game when game window is closed
            if event.type == pygame.QUIT:
                self.running: bool = False
                pygame.quit()
                sys.exit()
            # Check events for when a key is pressed
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Check events for when a key is released
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _update_screen(self):
        # Render updated frame/image of game state at desired FPS
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_keydown_events(self, event):
        # Ship moves up when up arrow key is pressed
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        # Ship moves down when down arrow key is pressed
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        # Ends game and closes game window when 'Q' key is pressed
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        # Ship stops moving up when up arrow key is released
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        # Ship stops moving down when down arrow key is released
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False



# AlienInvasion game initialized when program is run
if __name__ == '__main__':
    pass
    ai = AlienInvasion()
    ai.run_game()