import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:

    def __init__(self, game: 'AlienInvasion'):

        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_width, self.settings.ship_height))
        
        #collision rectangle (hitbox) for ship
        self.rect = self.image.get_rect()
        #draw ship at bottom center of screen
        self.rect.midbottom = self.boundaries.midbottom

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.x_pos = float(self.rect.x)

    def update(self):
        #update ships position based on movement flags
        temp_speed = self.settings.ship_speed
        #if flag is true and ship is within boundaries, move in that direction
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x_pos += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x_pos -= temp_speed

        # Update the ships hitbox position
        self.rect.x = self.x_pos


    def draw(self):
        self.screen.blit(self.image, self.rect)