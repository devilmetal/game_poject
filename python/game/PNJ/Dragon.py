import constants
import pygame
import PNJ_ressources
from Dragon_Body import Dragon_Body
class Dragon(pygame.sprite.Sprite):
    def __init__(self,level,player):
        super(Dragon, self).__init__()
        #init ressources
        PNJ_ressources.init_dragon_ressources()
        self.anchor_x = 1000
        self.anchor_y = 250
        self.head_x = 0
        self.head_y = 0
        self.body_len = 10
        self.body_offset_x = 150
        self.body_offset_y = 150
        self.level=level
        self.player=player
        #Instanciation :
        self.image = PNJ_ressources.dragon_ressources['cave'][0]
        self.rect = self.image.get_rect()
        #body array init
        self.body_array = []
        for i in range(self.body_len):
            self.body_array.append(Dragon_Body((i+1)*90+self.body_offset_x,self.body_offset_y,1,110,i*10))
        self.head_down = [0+self.body_offset_x,50+self.body_offset_y]
        self.head_up = [0+self.body_offset_x,0+self.body_offset_y]
        self.draw()

    def draw(self):
        self.image = PNJ_ressources.dragon_ressources['cave'][0].copy()
        for i in range(len(self.body_array)):
            self.image.blit(PNJ_ressources.dragon_ressources['body'][0],(int(self.body_array[i].get_x()),int(self.body_array[i].get_y())))
        self.image.blit(PNJ_ressources.dragon_ressources['head_down'][0],(self.head_down[0],self.head_down[1]))
        self.image.blit(PNJ_ressources.dragon_ressources['head_up'][0],(self.head_up[0],self.head_up[1]))

    def update(self):
        #TODO: Throw fireball if needed (timer) (instianciate + direction)
        #TODO: Check if colision player/Dragon
        #Check dragon hit player
        self.draw()
        hit = False
        #print self.player.rect
        for i in range(len(self.body_array)):
            rect = pygame.Rect(self.body_array[i].get_x()+self.rect.x, self.body_array[i].get_y()+self.rect.y, 95, 95)
            hit = hit or not(self.player.rect.collidelist([rect]))
        rect = pygame.Rect(self.head_down[0]+self.rect.x, self.head_down[1]+self.rect.y, 100, 39)
        hit = hit or not(self.player.rect.collidelist([rect]))
        if hit and not(self.player.hit):
            self.player.hit = True
            self.player.change_y = -10

        #Check player hit dragon
        hit_dragon = False
        rect = pygame.Rect(self.head_up[0]+self.rect.x, self.head_up[1]+self.rect.y, 141, 80)
        self.player.rect.x-=1
        hit_dragon = not(self.player.rect.collidelist([rect]))
        self.player.rect.x+=1
        if hit_dragon and not(self.player.hit) :
            self.hit()
            self.player.change_y = -10
            self.player.change_x = -10
        #Move the dragon
        for i in range(len(self.body_array)):
            self.body_array[i].update()
        head_x = self.body_array[0].get_x()
        head_y = self.body_array[0].get_y()

        self.head_down = [head_x-105,30+head_y]
        self.head_up = [head_x-105,head_y-20]


    def hit(self):
        #remove last body part
        if len(self.body_array) > 0:
            elem = self.body_array.pop(0)
            print "pop"
        #move offset
        #for i in range(len(self.body_array)):
        #    self.body_array[i].x += 20
        #self.head_down[0] += 20
        #self.head_up[0] += 20
        #if not elem.y == self.body_array[0].y:
        #    self.head_down[1] += 20
        #    self.head_up[1] += 20
