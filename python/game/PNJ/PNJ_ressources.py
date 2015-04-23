import routines
import pygame

blob_ressources = {}
dragon_ressources = {}
fairy_ressource = {}

def init_blob_ressources():
    if blob_ressources == {}:
        blob_ressources['left_blob1'] = routines.load_png('pnj/enemy/blob/left_blob1.png')
        blob_ressources['left_blob2'] =  routines.load_png('pnj/enemy/blob/left_blob2.png')
        blob_ressources['left_blob3'] =  routines.load_png('pnj/enemy/blob/left_blob3.png')
        blob_ressources['left_blob4'] =  routines.load_png('pnj/enemy/blob/left_blob4.png')
        blob_ressources['left_blob5'] =  routines.load_png('pnj/enemy/blob/left_blob5.png')
        blob_ressources['left_blob6'] =  routines.load_png('pnj/enemy/blob/left_blob6.png')
        blob_ressources['right_blob1'] =  routines.load_png('pnj/enemy/blob/right_blob1.png')
        blob_ressources['right_blob2'] =  routines.load_png('pnj/enemy/blob/right_blob2.png')
        blob_ressources['right_blob3'] =  routines.load_png('pnj/enemy/blob/right_blob3.png')
        blob_ressources['right_blob4'] =  routines.load_png('pnj/enemy/blob/right_blob4.png')
        blob_ressources['right_blob5'] =  routines.load_png('pnj/enemy/blob/right_blob5.png')
        blob_ressources['right_blob6'] =  routines.load_png('pnj/enemy/blob/right_blob6.png')
        blob_ressources['dead'] =  routines.load_png('pnj/enemy/blob/dead.png')
        blob_ressources['dead_sound'] = pygame.mixer.Sound('data/sound/blobdie.wav')

def init_dragon_ressources():
    if dragon_ressources == {}:
        dragon_ressources['body'] = routines.load_png('pnj/boss/dragon/body.png')
        dragon_ressources['fireball'] =  routines.load_png('pnj/boss/dragon/fireball.png')
        dragon_ressources['head_down'] =  routines.load_png('pnj/boss/dragon/head_down.png')
        dragon_ressources['head_up'] =  routines.load_png('pnj/boss/dragon/head_up.png')
        dragon_ressources['cave'] =  routines.load_png('pnj/boss/dragon/cave_entrance.png')

def init_fairy_ressources():
    if fairy_ressource == {}:
        fairy_ressource['full'] = routines.load_png('pnj/fairy/botteled_fairy.png')
        fairy_ressource['empty'] = routines.load_png('pnj/fairy/broken_glass.png')
        fairy_ressource['broken_sound'] = pygame.mixer.Sound('data/sound/glass.wav')
        fairy_ressource['scream'] = pygame.mixer.Sound('data/sound/scream.wav')
