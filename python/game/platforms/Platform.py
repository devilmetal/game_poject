import constants
import pygame
import platform_ressources

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    subblock = None
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super(Platform, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.PLAT_COL)
        platform_ressources.init_platform_ressources()
        texture1 = platform_ressources.platform_ressources['scratch'][0]
        texture2 = platform_ressources.platform_ressources['grass'][0]
        #Apply scratchy texture
        new_texture1 = pygame.transform.scale(texture1,(width, height))
        self.image.blit(new_texture1, (0, 0))
        #Compute and apply grass texture
        grass_width, grass_height = texture2.get_size()
        
        self.subblock = pygame.sprite.Group()

        '''
        #TODO: Correct this part
        if width <= grass_width:
            self.image.blit(texture2, (0, 0))
        else:
            #blit n-1 times
            nbr = int(width/grass_width)-1
            for i in range(nbr):
                self.image.blit(texture2, (0, grass_width*(i+1)))
            #blit last grass tile
            new_len = width-nbr*grass_width
            print new_len
            new_texture2 = pygame.transform.scale(texture2,(new_len, grass_height))
            self.image.blit(new_texture2, (nbr*grass_width, 0))
        '''
        #TODO: Remove this part
        new_texture2 = pygame.transform.scale(texture2,(width, grass_height))
        self.image.blit(new_texture2, (0, 0))

        self.rect = self.image.get_rect()
