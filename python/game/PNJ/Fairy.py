from PNJ import PNJ

import constants
import routines
import pygame
import PNJ_ressources

class Fairy(pygame.sprite.Sprite):

    def __init__(self,x,y,player):

        # Call the parent constructor
        super(Fairy, self).__init__()

        #Loading images
        PNJ_ressources.init_fairy_ressources()

        self.dead = False
        self.player = player
        self.image = pygame.transform.scale(PNJ_ressources.fairy_ressource['full'][0],(30,45))
        self.rect = PNJ_ressources.fairy_ressource['full'][1].copy()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Call the parent update
        if not self.dead:
            hit = pygame.sprite.collide_rect(self, self.player)
            if hit:
                if self.player.lives < 6:
                    self.player.lives+=1
                    PNJ_ressources.fairy_ressource['broken_sound'].play()
                    PNJ_ressources.fairy_ressource['scream'].play()
                    self.image = pygame.transform.scale(PNJ_ressources.fairy_ressource['empty'][0],(30,25))
                    #image change adding pixels to height
                    self.rect.y+=20
                    self.dead = True
