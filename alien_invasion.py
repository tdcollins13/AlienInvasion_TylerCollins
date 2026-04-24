"""
File Name: alien_invasion.py
Author: Tyler D. Collins
Date: 4/23/2026

Purpose: This program is the main file in the 'AlienInvasion_TylerCollins'
repository, which contains the code that runs a complete 2D game using Pygame. 
This 'Alien Invasion' game features custom game mechanics and was built using a 
set of assets provided by GitHub user RedBeard41.
"""

# Import Necessary Modules
import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from button import Button
from hud import HUD
from time import sleep


class AlienInvasion:
    """Represents the AlienInvasion game

    Attributes:
        settings (Settings): Module of predefined specifications used to 
        generate the game
        screen (Surface): The screen/window generated to display the game
        bg (Surface): The image used as the background of the game screen
        running (bool): Indicates whether or not the game is currently running
        clock (Clock): Tracks the progression of time while the game is running
        game_stats (GameStats): Contains player game stats
        ship (Ship): The ship/player object being used in the game
        alien_fleet (AlienFleet): Represents the entire alien fleet
        game_active (bool): Represents whether game is active or has ended
        laser_sound (Sound): Sound that plays when a laser is fired
        impact_sound (Sound): Sound that plays when an alien is destroyed
    """

    def __init__(self):
        # Initialize game screen/window
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

        # Initialize game stats, HUD, and base difficulty
        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.settings.initialize_dynamic_settings()

        # Initialize ship/player object & alien
        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        # Set up sound for laser fire
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        # Set up sound for laser impact with alien
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        # Display 'play' button before game begins
        self.play_button = Button(self, 'PLAY')
        self.game_active = False


    def run_game(self):
        """Responsible for calling the methods that run the game"""
        # Game Loop
        while self.running == True:
            self._check_events()
            if self.game_active == True:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)


    def _check_collisions(self):
        """Checks for collisions between game objects"""
        # Check for collisions between aliens and ship
        if self.ship.check_collisions(self.alien_fleet.fleet) == True:
            self._check_game_status()
        
        # Check for collisions between alien and left edge of screen behind ship
        if self.alien_fleet.check_fleet_reach_end():
            self._check_game_status()

        # Check for collisions between lasers and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        # Check if entire alien fleet destroyed. Total destruction resets level
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.game_stats.update_level()
            self.settings.increase_difficulty(self.game_stats.level)
            self.HUD.update_level()

    
    def _check_game_status(self):
        """Checks for player lives remaining and either resets the level or 
        ends the game"""
        # Resets level if there are ships remaining, otherwise game ends
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False


    def _reset_level(self):
        """Reset game level"""
        # Reset ship arsenal and create new fleet upon level reset
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()


    def restart_game(self):
        """Begins new AlienInvasion game after play button is clicked"""
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)


    def _update_screen(self):
        """Updates game screen"""
        # Render updated frame/image of game state at desired FPS
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        # Overlay play button before/after game
        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()


    def _check_events(self):
        """Checks for keyboard input by player"""
        for event in pygame.event.get():
            # Ends game when game window is closed
            if event.type == pygame.QUIT:
                self.running: bool = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            # Check events for when a key is pressed (during gameplay)
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            # Check events for when a key is released
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()


    def _check_button_clicked(self):
        """Checks for user mouse input to click on the play button at the 
        beginning/end of the AlienInvasion game"""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()


    def _check_keydown_events(self, event):
        """Performs actions when player provides keyboard input to control game

        Args:
            event (Event): An instance of keyboard input
        """
        # Ship moves up when 'up' arrow key is pressed
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        # Ship moves down when 'down' arrow key is pressed
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        # Ship fires laser w/ sound when 'spacebar' is pressed
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        # Ends game and closes game window when 'Q' key is pressed
        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()


    def _check_keyup_events(self, event):
        """Ensures appropriate game actions stop when keyboard controls are 
        released

        Args:
            event (Event): An instance of keyboard input
        """
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