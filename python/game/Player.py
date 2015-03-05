import pygame
import os
import constants

def load_png(name):
        """ Load image and return image object"""
        fullname = os.path.join('data', name)
        try:
                image = pygame.image.load(fullname)
                if image.get_alpha is None:
                        image = image.convert()
                else:
                        image = image.convert_alpha()
        except pygame.error, message:
                print 'Cannot load image:', fullname
                raise SystemExit, message
        return image, image.get_rect()


class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods
    def __init__(self):
        """ Constructor function """
        super(Player, self).__init__()

        #Load images and rectangles
        self.jump_l_image, self.jump_l_image_rect =  load_png('hero/jump_l.png')
        self.jump_r_image, self.jump_r_image_rect =  load_png('hero/jump_r.png')
        self.idle_l_image, self.idle_l_image_rect = load_png('hero/idle_l.png')
        self.idle_r_image, self.idle_r_image_rect = load_png('hero/idle_r.png')
        self.move_1_r_image, self.move_1_r_image_rect = load_png('hero/move_1_r.png')
        self.move_1_l_image, self.move_1_l_image_rect = load_png('hero/move_1_l.png')
        self.move_2_r_image, self.move_2_r_image_rect = load_png('hero/move_2_r.png')
        self.move_2_l_image, self.move_2_l_image_rect = load_png('hero/move_2_l.png')

        #load sounds
        self.sounds={}
        self.sounds['jump']=pygame.mixer.Sound('data/sound/jump.wav')


        self.image = self.idle_l_image
        self.rect = self.idle_l_image_rect
        # Set a referance to the image rect.
        #self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None

        self.status = 'idle_r' #idle,move,jump,
        self.location = 'ground' #ground,air,block


    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
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
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.location = 'block'
                if self.status == 'air':
                    if self.status == 'move_r':
                        self.status = 'idle_r'
                    else:
                        self.status = 'idle_l'
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

        #Finally calculate the image to display
        self.calc_image()

    def calc_image(self):
        if self.location == 'air':
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
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.location = 'air'
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.location = 'ground'
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            #Play sound jump
            self.sounds['jump'].play()
            self.change_y = -10
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
