import constants
import pygame


class Boss(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Boss, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        #TODO:
        a=0
        #Move
        #Throw something (instianciate + direction)

    def move(self):
        #TODO:
        a=0
