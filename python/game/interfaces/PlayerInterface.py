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
        self.heart_image, self.heart_image_rect = routines.load_png('heart/heart.png')
        self.image = self.heart_image
        self.rect = self.heart_image_rect



    def draw(self, screen, lives):
        hearts = pygame.transform.scale(self.image,(34,34))
        font_path = "data/coders_crux/coders_crux.ttf"
        txt = routines.draw_text("x" + str(lives), 0, 0, 44, font_path, constants.WHITE)
        screen.blit(hearts, [10, 10])
        screen.blit(txt[0], [50, 15])
