import pygame
import os
import constants
import routines

class PlayerInterface():
    """
    This class represents the bar at the top, displaying game status (lives, time, etc.).
    """

    # -- Methods
    def __init__(self):
        """ Constructor function """
        # super(PlayerInterface, self).__init__()

        #Load images and rectangles
        self.lives_0_image, self.lives_0_image_rect =  routines.load_png('heart/0.png')
        self.lives_1_image, self.lives_1_image_rect =  routines.load_png('heart/1.png')
        self.lives_2_image, self.lives_2_image_rect =  routines.load_png('heart/2.png')
        self.lives_3_image, self.lives_3_image_rect = routines.load_png('heart/3.png')
        self.lives_4_image, self.lives_4_image_rect = routines.load_png('heart/4.png')
        self.lives_5_image, self.lives_5_image_rect = routines.load_png('heart/5.png')
        self.lives_6_image, self.lives_6_image_rect = routines.load_png('heart/6.png')

        self.image = self.lives_6_image #lives are full
        self.rect = self.lives_6_image_rect

        # Set speed vector of the interface (must move like the player)
        self.change_x = 0
        self.change_y = 0

        self.lives = 6 #the number of lives the player has TODO: this information will be retrieved from the player saved data!

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        if not self.hit:

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
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom

                # Stop our vertical movement
                self.change_y = 0
        else:
            self.rect.y += self.change_y
            self.change_x = 0


        #Finally calculate the image to display
        self.calc_image()

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


    def draw(self,screen):
        # bg = routines.draw_rectangle(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.BLACK)
        # #Draw funky text
        # txt1 = routines.draw_text("Select your Badass", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/5 - 20, 52, "data/coders_crux/coders_crux.ttf", constants.WHITE)
        # txt2 = routines.draw_text("and go kick some asses !", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/5 + 20, 38, "data/coders_crux/coders_crux.ttf", constants.WHITE)
        # bg.blit(txt1[0], txt1[1])
        # bg.blit(txt2[0], txt2[1])

        heart = pygame.image.load("heart/6.png").convert()
        screen.blit(heart, [0, 0])

        # self.screen.blit(bg, (0,0))
