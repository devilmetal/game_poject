import constants
import pygame
import PNJ_ressources

class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        super(Dragon, self).__init__()
        #init ressources
        PNJ_ressources.init_dragon_ressources()
        self.head_x = 0
        self.head_y = 0
        self.body_len = 7
        #Instanciation :
        # x = n*100 px for body + head len = 5*100px + 150px = 650px
        # y = n*1/2*100 px for body + hen size = 5*1/2*100px + 80+50 = 380px
        width = 650
        height = 380
        offset_x = 500
        offset_y = 0
        self.image = PNJ_ressources.dragon_ressources['cave'][0]
        self.rect = self.image.get_rect()
        self.body_array = []
        self.body_array.append((90+offset_x,50+offset_y))
        self.body_array.append((150+offset_x,110+offset_y))
        self.body_array.append((210+offset_x,170+offset_y))
        self.body_array.append((270+offset_x,220+offset_y))
        self.body_array.append((330+offset_x,280+offset_y))
        self.body_array.append((410+offset_x,280+offset_y))
        self.body_array.append((490+offset_x,280+offset_y))

        self.head_down = (0+offset_x,50+offset_y)
        self.head_up = (0+offset_x,0+offset_y)
        self.draw()

    def draw(self):
        self.image = PNJ_ressources.dragon_ressources['cave'][0]

        for i in range(len(self.body_array)):
            self.image.blit(PNJ_ressources.dragon_ressources['body'][0],self.body_array[i])

        self.image.blit(PNJ_ressources.dragon_ressources['head_down'][0],self.head_down)
        self.image.blit(PNJ_ressources.dragon_ressources['head_up'][0],self.head_up)
    def update(self):
        #TODO:
        a=0
        #Move
        #Throw something (instianciate + direction)
        self.draw()
        
    def move(self):
        #TODO:
        a=0
