import constants
import world_ressources
import pygame


class Parallax(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    def __init__(self, x,y,width,height,mode,level):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super(Parallax, self).__init__()
        world_ressources.init_parallax_ressources(width,height)
        self.level = level
        self.rect = None
        self.image = None
        if mode == "back":
            self.image = world_ressources.parallax_ressources['back']
            self.rect = self.image.get_rect().copy()
        elif mode == "front":
            self.image = world_ressources.parallax_ressources['front']
            self.rect = self.image.get_rect().copy()
        elif mode == "cave_p":
            self.image = world_ressources.parallax_ressources['cave']
            self.rect = self.image.get_rect().copy()
        self.rect.x = x
        self.rect.y = y
        #print "init parallax at "+str(x)+' '+str(y)+' mode : '+mode
