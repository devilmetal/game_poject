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
        #Load images and rectangles
        # self.lives_0_image, self.lives_0_image_rect =  routines.load_png('heart/0.png')
        # self.lives_1_image, self.lives_1_image_rect =  routines.load_png('heart/1.png')
        # self.lives_2_image, self.lives_2_image_rect =  routines.load_png('heart/2.png')
        # self.lives_3_image, self.lives_3_image_rect = routines.load_png('heart/3.png')
        # self.lives_4_image, self.lives_4_image_rect = routines.load_png('heart/4.png')
        # self.lives_5_image, self.lives_5_image_rect = routines.load_png('heart/5.png')
        # self.lives_6_image, self.lives_6_image_rect = routines.load_png('heart/6.png')
        self.heart_image, self.heart_image_rect = routines.load_png('heart/heart.png')

        # self.lives_arr = [  self.lives_0_image,
        #                     self.lives_1_image,
        #                     self.lives_2_image,
        #                     self.lives_3_image,
        #                     self.lives_4_image,
        #                     self.lives_5_image,
        #                     self.lives_6_image ]

        # self.image = self.lives_6_image #lives are full
        # self.rect = self.lives_6_image_rect
        self.image = self.heart_image
        self.rect = self.heart_image_rect



    def draw(self, screen, lives):
        # self.image = self.lives_arr[lives]
        hearts = pygame.transform.scale(self.image,(34,34))
        font_path = "data/coders_crux/coders_crux.ttf"
        txt = routines.draw_text("x" + str(lives), 0, 0, 44, font_path, constants.WHITE)
        screen.blit(hearts, [10, 10])
        screen.blit(txt[0], [50, 15])
