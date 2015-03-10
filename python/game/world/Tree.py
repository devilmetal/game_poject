import constants
import world_ressources
import pygame


class Tree(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    def __init__(self, type):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        world_ressources.init_tree_ressources()
        super(Tree, self).__init__()
        self.image = world_ressources.tree_ressources['tree1'][0]
        self.rect = world_ressources.tree_ressources['tree1'][1]
