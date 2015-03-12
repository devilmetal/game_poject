import routines

tree_ressources = {}

def init_tree_ressources():
    if tree_ressources == {}:
        tree_ressources['tree1'] = routines.load_png('world/trees/tree1.png')
