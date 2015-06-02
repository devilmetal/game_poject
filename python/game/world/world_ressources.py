import routines
import pygame

tree_ressources = {}
parallax_ressources = {}
sign_ressources = {}


def init_tree_ressources():
    if tree_ressources == {}:
        tree_ressources['tree1'] = routines.load_png('world/trees/tree1.png')

def init_parallax_ressources(width,height):
    if parallax_ressources == {}:
        parallax_ressources['back'] = pygame.transform.scale(routines.load_png('world/trees/far-background.png')[0],(width,height))
        parallax_ressources['front'] = pygame.transform.scale(routines.load_png('world/trees/near-background.png')[0],(width,height))
        parallax_ressources['cave'] = pygame.transform.scale(routines.load_png('world/cave/background_cave.png')[0],(width,height))

def init_sign_ressources():
    if sign_ressources == {}:
        sign_ressources['sign'] = routines.load_png('world/sign/sign.png')
        sign_ressources['sign_blue'] = routines.load_png('world/sign/sign_blue.png')
        sign_ressources['sign_yellow'] = routines.load_png('world/sign/sign_yellow.png')
        sign_ressources['sign_red'] = routines.load_png('world/sign/sign_red.png')
