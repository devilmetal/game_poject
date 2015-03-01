from Platform import Platform
import pygame

class BoostPlatform(Platform):
    """ Booster platform """
    player = None
    level = None
    direction = 1 #+1,-1
    boost = 0.1
    def update(self):
        #check if the player is on top of the platform
        self.player.rect.y += 1
        hit = pygame.sprite.collide_rect(self.player, self)
        self.player.rect.y -= 1

        if hit:
            self.player.change_x = 6*self.direction
