import constants
import routines
import pygame
import platform_ressources

class Spike(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    def __init__(self,orientation):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super(Spike, self).__init__()
        self.orientation = orientation #0,1,2,3
        platform_ressources.init_spikes_ressources()
        self.image = None
        self.rect = None
        self.mask = 0
        if self.orientation == 0:
            self.image = platform_ressources.spikes_ressources['up'][0]
            self.rect = platform_ressources.spikes_ressources['up'][1].copy()
        elif self.orientation == 1:
            self.image = platform_ressources.spikes_ressources['right'][0]
            self.rect = platform_ressources.spikes_ressources['right'][1].copy()
        elif self.orientation == 2:
            self.image = platform_ressources.spikes_ressources['down'][0]
            self.rect = platform_ressources.spikes_ressources['down'][1].copy()
        else:
            self.image = platform_ressources.spikes_ressources['left'][0]
            self.rect = platform_ressources.spikes_ressources['left'][1].copy()
        

    def update(self):
        #check if the player is on top of the platform
        hit = False
        if self.orientation == 0:
            rect = pygame.Rect(self.rect.left + int(self.rect.width/2)-3, self.rect.top, 6, 6)
            self.player.rect.y += 1
            hit = not(self.player.rect.collidelist([rect]))
            self.player.rect.y -= 1
        if self.orientation == 2:
            rect = pygame.Rect(self.rect.left + int(self.rect.width/2)-3, self.rect.top + self.rect.height-6, 6, 6)
            self.player.rect.y -= 1
            hit = not(self.player.rect.collidelist([rect]))
            self.player.rect.y += 1
        if self.orientation == 1:
            rect = pygame.Rect(self.rect.left + self.rect.width-6, self.rect.top + int(self.rect.height/2)-3, 6, 6)
            self.player.rect.x -= 1
            hit = not(self.player.rect.collidelist([rect]))
            self.player.rect.x += 1
        if self.orientation == 3:
            rect = pygame.Rect(self.rect.left, self.rect.top + int(self.rect.height/2)-3, 6, 6)
            self.player.rect.x += 1
            hit = not(self.player.rect.collidelist([rect]))
            self.player.rect.x -= 1
        if hit and not self.player.hit:
            self.player.hit = True
            self.player.change_y = -10
