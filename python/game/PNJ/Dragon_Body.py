import pygame

class Dragon_Body(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,boundary,offset):
        super(Dragon_Body, self).__init__()
        self.x = x #x
        self.y = y+offset #y
        self.direction = direction # direction either -1 or 1 (up or down)
        self.down_limit = y+boundary # size of the array going down
        self.up_limit = y
    def update(self):
        self.y+=2*self.direction
        if self.y > self.down_limit:
            self.direction=self.direction * -1
        if self.y < self.up_limit:
            self.direction=self.direction * -1

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
