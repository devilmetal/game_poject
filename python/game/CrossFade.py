# CREDIT: https://www.youtube.com/watch?v=vLYwl9MFvQQ
# Synthesizes a cross-fade effect by changing the transparency
# of a Surface over time
# python_bro
# 9/7/13

import pygame

class CrossFade(pygame.sprite.Sprite):
    """Synthesizes fades by incrementing the transparency
        of a black surface blitted on top of the screen"""
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        #make a Surface to be used as our fader
        #The size is dynamically based on the size of the screen
        self.image = pygame.Surface(screen.get_size())
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))

        #get the Rect dimensions
        self.rect = self.image.get_rect()

        #fade_dir determines whether to fade in our fade out
        self.fade_dir = 1

        #trans_value is the degree of transparency.
        #255 is opaque/0 is fully transparent
        self.trans_value = 255

        #fade_speed is the difference in transparency after each delay
        self.fade_speed = 25

        #delay helps to dynamically adjust the number of frames between fades
        self.delay = 1

        #increment increases each frame (each call to update)
        #until it is equal to our delay (see update() below)
        self.increment = 0

        #initialize our transparency (at opaque)
        self.image.set_alpha(self.trans_value)

        #set position of the black Surface
        # self.rect.centerx = 320
        # self.rect.centery = 240

    def update(self):
        self.image.set_alpha(self.trans_value)
        #increase increment
        self.increment += 1

        if self.increment >= self.delay:
            self.increment = 0

            #Fade in
            if self.fade_dir > 0:
                #make sure the transparent value doesn't go negative
                if self.trans_value - self.fade_speed < 0:
                    self.trans_value = 0
                #increase transparency of the black Surface by decreasing its alpha
                else:
                    self.trans_value -= self.fade_speed

            #Fade out
            elif self.fade_dir < 0:
                #make sure transparent value doesn't go above 255
                if self.trans_value + self.delay > 255:
                    self.trans_value = 255
                #increase opacity of black Surface
                else:
                    self.trans_value += self.fade_speed


    def fade(self, screen, speed=25):
        self.fade_dir = -1
        self.trans_value = 0
        self.fade_speed = speed
        fade_screen = screen.copy()
        all_Sprites = pygame.sprite.Group(self)
        while self.trans_value != 255:
            all_Sprites.clear(screen, fade_screen)
            all_Sprites.update()
            all_Sprites.draw(screen)
            #refresh the screen
            pygame.display.flip()
        self.fade_dir = 1
        self.trans_value = 255
        while self.trans_value != 0:
            all_Sprites.clear(screen, fade_screen)
            all_Sprites.update()
            all_Sprites.draw(screen)
            #refresh the screen
            pygame.display.flip()


    def fadein(self, screen, speed=25):
        self.fade_dir = 1
        self.trans_value = 255
        self.fade_speed = speed
        fade_screen = screen.copy()
        all_Sprites = pygame.sprite.Group(self)
        while self.trans_value != 0:
            all_Sprites.clear(screen, fade_screen)
            all_Sprites.update()
            all_Sprites.draw(screen)
            #refresh the screen
            pygame.display.flip()


    def fadeout(self, screen, speed=25):
        self.fade_dir = -1
        self.trans_value = 0
        self.fade_speed = speed
        fade_screen = screen.copy()
        all_Sprites = pygame.sprite.Group(self)
        while self.trans_value != 255:
            all_Sprites.clear(screen, fade_screen)
            all_Sprites.update()
            all_Sprites.draw(screen)
            #refresh the screen
            pygame.display.flip()
