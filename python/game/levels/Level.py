import pygame
import constants

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game.
    platform_list = None
    pnj_list = None
    back_world_list = None
    # How far this world has been scrolled left/right
    world_shift = 0

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.pnj_list = pygame.sprite.Group()
        self.back_world_list = pygame.sprite.Group()

        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.back_world_list.update()
        self.platform_list.update()
        self.pnj_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(constants.BLUE)

        # Draw all the sprite lists that we have
        self.back_world_list.draw(screen)
        self.platform_list.draw(screen)
        self.pnj_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for pnj in self.pnj_list:
            pnj.rect.x += shift_x

        for item in self.back_world_list:
            item.rect.x += shift_x
