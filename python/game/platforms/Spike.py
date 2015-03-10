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
            self.player.rect.y += 1
            hit = pygame.sprite.collide_rect(self.player, self)
            self.player.rect.y -= 1
        if self.orientation == 2:
            self.player.rect.y -= 1
            hit = pygame.sprite.collide_rect(self.player, self)
            self.player.rect.y += 1
        if self.orientation == 1:
            self.player.rect.x -= 1
            hit = pygame.sprite.collide_rect(self.player, self)
            self.player.rect.x += 1
        if self.orientation == 3:
            self.player.rect.x += 1
            hit = pygame.sprite.collide_rect(self.player, self)
            self.player.rect.x -= 1
        if hit:
            self.player.dead = True
