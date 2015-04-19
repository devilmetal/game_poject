import pygame
import PNJ_ressources

class Fireball(pygame.sprite.Sprite):
    def __init__(self,x,y,speed,player):
        super(Fireball, self).__init__()
        PNJ_ressources.init_dragon_ressources()
        self.speed = speed
        #we go left
        self.image = PNJ_ressources.dragon_ressources['fireball'][0]
        #copy is important ! otherwise => same rect object per blob
        self.rect = PNJ_ressources.dragon_ressources['fireball'][1].copy()
        self.rect.x = x
        self.rect.y = y
        self.player = player
    def update(self):
        self.rect.x-=self.speed*1
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit and not(self.player.hit):
            self.player.hit = True
            self.player.change_y = -10
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
