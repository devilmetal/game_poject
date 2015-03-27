import constants
import pygame
import platform_ressources

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super(Platform, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.GREEN)
        platform_ressources.init_platform_ressources()
        texture1 = platform_ressources.platform_ressources['scratch'][0]
        pygame.transform.scale(texture1,(width, height))
        self.image.blit(texture1, (0, 0))
        self.rect = self.image.get_rect()
