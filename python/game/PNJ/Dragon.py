import constants
import pygame
import PNJ_ressources
from Dragon_Body import Dragon_Body
class Dragon(pygame.sprite.Sprite):
    def __init__(self):
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

        #Instanciation :
        # x = n*100 px for body + head len = 5*100px + 150px = 650px
        # y = n*1/2*100 px for body + hen size = 5*1/2*100px + 80+50 = 380px
        width = 650
        height = 380
        self.image = PNJ_ressources.dragon_ressources['cave'][0]

        self.rect = self.image.get_rect()

        #body array init
        self.body_array = []
        for i in range(self.body_len):
            self.body_array.append(Dragon_Body((i+1)*90+self.body_offset_x,self.body_offset_y,1,110,i*10))
            print self.body_array[i].get_x
            print self.body_array[i].get_y
            print self.body_array[i].direction
            print self.body_array[i].down_limit
            print self.body_array[i].up_limit
        self.head_down = [0+self.body_offset_x,50+self.body_offset_y]
        self.head_up = [0+self.body_offset_x,0+self.body_offset_y]
        self.hit()
        #self.hit()
        #self.hit()
        #self.hit()
        #self.hit()

        self.draw()

    def wave_motion(array):

        y_first = array[0][1]
        array[0][1] = array[0][1]


        return array
    def draw(self):
        self.image = PNJ_ressources.dragon_ressources['cave'][0].copy()
        for i in range(len(self.body_array)):
            self.image.blit(PNJ_ressources.dragon_ressources['body'][0],(int(self.body_array[i].get_x()),int(self.body_array[i].get_y())))
        self.image.blit(PNJ_ressources.dragon_ressources['head_down'][0],(self.head_down[0],self.head_down[1]))
        self.image.blit(PNJ_ressources.dragon_ressources['head_up'][0],(self.head_up[0],self.head_up[1]))

    def update(self):
        #TODO:
        a=0
        #Move
        #self.body_array = self.wave_motion(self.body_array)
        #Throw something (instianciate + direction)
        for i in range(len(self.body_array)):
            self.body_array[i].update()
        self.draw()

    def move(self):
        #TODO:
        a=0

    def hit(self):
        #remove last body part
        if len(self.body_array) > 0:
            elem = self.body_array.pop(0)
        #move offset
        for i in range(len(self.body_array)):
            self.body_array[i].x += 60
        self.head_down[0] += 60
        self.head_up[0] += 60
        if not elem.y == self.body_array[0].y:
            self.head_down[1] += 60
            self.head_up[1] += 60
