import constants
import pygame
import PNJ_ressources

class Dragon(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Dragon, self).__init__()
        #init ressources
        PNJ_ressources.init_dragon_ressources()

        self.image = pygame.Surface([width, height])
        self.image.fill(constants.BLACK)
        self.rect = self.image.get_rect()
        self.head.x = 0
        self.head.y = 0
    def update(self):
        #TODO:
        a=0
        #Move
        #Throw something (instianciate + direction)

    def move(self):
        #TODO:
        a=0
