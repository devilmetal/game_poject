from Character import Character

import pygame
import os
import constants
import routines

#Bob is a standard character that reflet the Character object as standard.
#Bob is playable and should be used to create new character as code-reference

class LittleFat(Character):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods
    def __init__(self):
        """ Constructor function """
        Character.__init__(self)
        self.jump_l_image, self.jump_l_image_rect =  routines.load_png('hero_2/jump_l.png')
        self.jump_r_image, self.jump_r_image_rect =  routines.load_png('hero_2/jump_r.png')
        self.idle_l_image, self.idle_l_image_rect = routines.load_png('hero_2/idle_l.png')
        self.idle_r_image, self.idle_r_image_rect = routines.load_png('hero_2/idle_r.png')
        self.move_1_r_image, self.move_1_r_image_rect = routines.load_png('hero_2/move_1_r.png')
        self.move_1_l_image, self.move_1_l_image_rect = routines.load_png('hero_2/move_1_l.png')
        self.move_2_r_image, self.move_2_r_image_rect = routines.load_png('hero_2/move_2_r.png')
        self.move_2_l_image, self.move_2_l_image_rect = routines.load_png('hero_2/move_2_l.png')
        self.dead_image, self.dead_image_rect = routines.load_png('hero_2/death.png')

        #load sounds
        self.sounds={}
        self.sounds['jump']=pygame.mixer.Sound('data/sound/jump.wav')


        self.image = self.idle_l_image
        self.rect = self.idle_l_image_rect
        # Set a referance to the image rect.

        #Setup status
        self.status = 'idle_r' #idle,move,jump,
        self.location = 'ground' #ground,air,block

        Character.set_options(self, 10, False, 1)
