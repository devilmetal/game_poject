import pygame
import constants

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game.
    platform_list = None
    mov_plat_list = None
    pnj_list = None
    back_world_list = None
    magma_list = None
    game = None
    # How far this world has been scrolled left/right
    world_shift = 0
    game_update=0

    start_x = 0
    start_y = 0

    next_level = 0
    end_level = False

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.mov_plat_list = pygame.sprite.Group()
        self.pnj_list = pygame.sprite.Group()
        self.back_world_list = pygame.sprite.Group()
        self.back_front_world_list = pygame.sprite.Group()
        self.magma_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        #self.magma_list.update()
        for elem in self.magma_list:
            if abs(elem.rect.x - self.player.rect.x) < constants.SCREEN_WIDTH * 3:
                elem.update()
        #self.platform_list.update()
        for elem in self.platform_list:
            if abs(elem.rect.x - self.player.rect.x) < constants.SCREEN_WIDTH * 2:
                elem.update()
        #self.pnj_list.update()
        for elem in self.pnj_list:
            if abs(elem.rect.x - self.player.rect.x) < constants.SCREEN_WIDTH * 2:
                elem.update()
        for elem in self.mov_plat_list:
            if abs(elem.rect.x - self.player.rect.x) < constants.SCREEN_WIDTH * 3:
                for block in elem.subblock:
                    block.update()
                elem.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        #screen.fill(constants.BLUE)

        # Draw all the sprite lists that we have
        #self.back_world_list.draw(screen)
        for elem in self.back_world_list:
            if not(screen.get_rect().collidelist([elem])):
                screen.blit(elem.image,elem.rect)
        #self.back_front_world_list.draw(screen)
        for elem in self.back_front_world_list:
            if not(screen.get_rect().collidelist([elem])):
                screen.blit(elem.image,elem.rect)
        #self.platform_list.draw(screen)
        for elem in self.platform_list:
            if not(screen.get_rect().collidelist([elem])):
                screen.blit(elem.image,elem.rect)
        #pygame.sprite.spritecollide(screen, self.platform_list, False).draw(screen)
        #self.magma_list.draw(screen)
        for elem in self.magma_list:
            if not(screen.get_rect().collidelist([elem])):
                screen.blit(elem.image,elem.rect)
        #self.pnj_list.draw(screen)
        for elem in self.pnj_list:
            if not(screen.get_rect().collidelist([elem])):
                screen.blit(elem.image,elem.rect)
        for elem in self.mov_plat_list:
            for block in elem.subblock:
                if not(screen.get_rect().collidelist([elem])) or not(screen.get_rect().collidelist([block])):
                    screen.blit(block.image,block.rect)
                    screen.blit(elem.image,elem.rect)
        self.player.interface.draw(screen, self.player.lives)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for plat in self.magma_list:
            plat.rect.x += shift_x

        for pnj in self.pnj_list:
            pnj.rect.x += shift_x

        for item in self.back_world_list:
            item.rect.x += shift_x*0.5

        for item in self.back_front_world_list:
            item.rect.x += shift_x

        for item in self.mov_plat_list:
            for block in item.subblock:
                    block.rect.x += shift_x
            item.rect.x += shift_x