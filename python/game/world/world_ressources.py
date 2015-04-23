import routines

tree_ressources = {}
parallax_ressources = {}

def init_tree_ressources():
    if tree_ressources == {}:
        tree_ressources['tree1'] = routines.load_png('world/trees/tree1.png')

def init_parallax_ressources():
    if parallax_ressources == {}:
        parallax_ressources['back'] = routines.load_png('world/trees/far-background.png')
        parallax_ressources['front'] = routines.load_png('world/trees/near-background.png')
