import pygame
import os
import constants
import routines
from interfaces.PlayerInterface import PlayerInterface

class Character(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods
    def __init__(self):
        """ Constructor function """
        super(Character, self).__init__()

        self.interface = PlayerInterface()

        #personnal aptitudes
        self.jump_height = 10
        self.weight = 1
        self.id = 1 #this number is used to save game progress (determined when new char is unlocked)

        #Physics stuff
        self.gravity_a = .35


        self.image = None
        self.rect = None
        # Set a referance to the image rect.
        #self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

        self.status = None #idle,move,jump,
        self.location = None #ground,air,block

        self.mov_plat = False #is on a moving plateform
        self.dead = False #is dead

        self.mov_plat = False #is a moving plateform
        self.hit = False
        self.lives = 6 #the number of lives the player has TODO: this information will be retrieved from the player saved data!
        self.game_over = False

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        if not self.hit:

            # Move left/right
            self.rect.x += self.change_x

            # See if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False) + pygame.sprite.spritecollide(self, self.level.mov_plat_list, False)
            for block in block_hit_list:
                # If we are moving right,
                # set our right side to the left side of the item we hit
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.rect.left = block.rect.right

            # Move up/down
            self.rect.y += self.change_y


            # Check and see if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False) + pygame.sprite.spritecollide(self, self.level.mov_plat_list, False)
            for block in block_hit_list:

                # Reset our position based on the top/bottom of the object.
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom

                # Stop our vertical movement
                self.change_y = 0
        else:
            self.rect.y += self.change_y
            if self.mov_plat:
                self.change_x = 0


        #Finally calculate the image to display
        self.calc_image()

        self.lives_interface()

    def calc_image(self):
        if self.hit == True:
            self.image = self.dead_image
        elif self.location == 'air':
            if self.status == 'move_r' or self.status == 'idle_r' :
                self.image = self.jump_r_image
            else:
                self.image = self.jump_l_image
        else:
            if self.status == 'idle_l':
                self.image = self.idle_l_image
                constants.MOVING_FRAME = 0
            elif self.status == 'idle_r':
                self.image = self.idle_r_image
                constants.MOVING_FRAME = 0
            elif self.status == 'move_r':
                if (int(constants.MOVING_FRAME) % 2) == 0:
                    if constants.FRAME_INC < constants.STEP_SPEED:
                        self.image = self.move_1_r_image
                        constants.FRAME_INC += 1
                    else:
                        self.image = self.move_1_r_image
                        constants.FRAME_INC = 0
                        constants.MOVING_FRAME += 1
                else:
                    if constants.FRAME_INC < constants.STEP_SPEED:
                        self.image = self.move_2_r_image
                        constants.FRAME_INC += 1
                    else:
                        self.image = self.move_2_r_image
                        constants.FRAME_INC = 0
                        constants.MOVING_FRAME += 1
            elif self.status == 'move_l':
                if (int(constants.MOVING_FRAME) % 2) == 0:
                    if constants.FRAME_INC < constants.STEP_SPEED:
                        self.image = self.move_1_l_image
                        constants.FRAME_INC += 1
                    else:
                        self.image = self.move_1_l_image
                        constants.FRAME_INC = 0
                        constants.MOVING_FRAME += 1
                else:
                    if constants.FRAME_INC < constants.STEP_SPEED:
                        self.image = self.move_2_l_image
                        constants.FRAME_INC += 1
                    else:
                        self.image = self.move_2_l_image
                        constants.FRAME_INC = 0
                        constants.MOVING_FRAME += 1
            else:
                #FORBIDDEN
                self.image = self.idle_r_image


    def calc_grav(self):
        """ Calculate effect of gravity. """
        #In order to debug the image of the character that is displayed when he/she is
        #on en plateform that moves down we need to check whether or not we're on it and
        #make an special case
        self.rect.y += 4
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False) + pygame.sprite.spritecollide(self, self.level.mov_plat_list, False)
        self.rect.y -= 4


        if len(platform_hit_list) > 0 and self.rect.bottom < constants.SCREEN_HEIGHT - 20 and not self.hit:
            self.location = 'block'
        else:
            self.location = 'air'
            self.change_y += self.gravity_a * self.weight

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height - 20 and self.change_y >= 0:
            self.location = 'ground'

        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height + 100 and self.change_y >= 0:
            self.change_y = 0
            self.dead = True




    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False) + pygame.sprite.spritecollide(self, self.level.mov_plat_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        # If we're on a moving plateform and we jump, we don't keep the speed of the plateform
        # (it only works if we don't set the speed of the plateform same speed than the character)

        if len(platform_hit_list) > 0 and not self.hit:
            #Play sound jump
            #self.sounds['jump'].play()
            if self.mov_plat == True:
                self.change_x = 0

            if self.status == 'move_l':
                self.change_x = -6
            if self.status == 'move_r':
                self.change_x = 6

            self.change_y = -self.jump_height
            self.location = 'air'

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.status = 'move_l'
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.status = 'move_r'
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        if self.status == 'move_r':
            self.status = 'idle_r'
        else:
            self.status = 'idle_l'


    def set_options(self, jump_height, id, weight):
        self.jump_height = jump_height
        self.id = id #this number is used to save game progress (determined when new char is unlocked)
        self.weight = weight


    def lives_interface(self):
        if self.dead == True:
            if self.lives > 0:
                self.lives -= 1
            else:
                self.game_over = True
