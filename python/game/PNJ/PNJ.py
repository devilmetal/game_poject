import pygame
import os
import routines
import constants

class PNJ(pygame.sprite.Sprite):

    def __init__(self,direction,speed):
        """ Constructor function """
        super(PNJ, self).__init__()

        self.direction = direction
        self.speed = speed
        # Set speed vector of PNJ
        self.change_x = direction*speed
        self.change_y = 0

        #Prepare rectangle
        self.rect = None

        # List of sprites PNJ can bump against + player
        self.level = None
        self.player = None


    def update(self):

        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        #Set basicly the same direction if no hit

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
                self.change_x *= -1
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                self.change_x *= -1

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
