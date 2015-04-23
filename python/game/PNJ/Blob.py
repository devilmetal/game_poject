from PNJ import PNJ

import constants
import routines
import pygame
import PNJ_ressources

class Blob(PNJ):

    def __init__(self,direction,speed):

        # Call the parent constructor
        PNJ.__init__(self,direction,speed)

        #Loading images
        PNJ_ressources.init_blob_ressources()

        #Frame incr. + frame speed
        self.frame_inc=0
        self.speed_frame = 3

        if self.direction > 0:
            #we go left
            self.image = PNJ_ressources.blob_ressources['left_blob1'][0]
            #copy is important ! otherwise => same rect object per blob
            self.rect = PNJ_ressources.blob_ressources['left_blob1'][1].copy()

        else:
            #we go right
            self.image = PNJ_ressources.blob_ressources['right_blob1'][0]
            self.rect = PNJ_ressources.blob_ressources['right_blob1'][1].copy()

    def update(self):
        # Call the parent update
        if not self.dead:
            PNJ.update(self)
            self.calc_image()
            self.check_hit()

    def calc_image(self):
        if self.change_x < 0:
            #we go left
            if self.frame_inc in range(0,self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['left_blob1'][0]
                self.frame_inc+=1
            elif self.frame_inc in range(self.speed_frame,2*self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['left_blob2'][0]
                self.frame_inc+=1
            elif self.frame_inc in range(2*self.speed_frame,3*self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['left_blob3'][0]
                self.frame_inc+=1
            elif self.frame_inc in range(3*self.speed_frame,4*self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['left_blob4'][0]
                self.frame_inc+=1
            elif self.frame_inc in range(4*self.speed_frame,5*self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['left_blob5'][0]
                self.frame_inc+=1
            elif self.frame_inc in range(5*self.speed_frame,6*self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['left_blob6'][0]
                self.frame_inc+=1
            else:
                self.image = PNJ_ressources.blob_ressources['left_blob1'][0]
                self.frame_inc=0


        else:
            #we go right
            #we go left
            if self.frame_inc in range(0,self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['right_blob1'][0]
                self.frame_inc+=1
            elif self.frame_inc in range(self.speed_frame,2*self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['right_blob2'][0]
                self.frame_inc+=1
            elif self.frame_inc in range(2*self.speed_frame,3*self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['right_blob3'][0]
                self.frame_inc+=1
            elif self.frame_inc in range(3*self.speed_frame,4*self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['right_blob4'][0]
                self.frame_inc+=1
            elif self.frame_inc in range(4*self.speed_frame,5*self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['right_blob5'][0]
                self.frame_inc+=1
            elif self.frame_inc in range(5*self.speed_frame,6*self.speed_frame):
                self.image = PNJ_ressources.blob_ressources['right_blob6'][0]
                self.frame_inc+=1
            else:
                self.image = PNJ_ressources.blob_ressources['right_blob1'][0]
                self.frame_inc=0
    def check_hit(self):
        self.rect.x += 5
        hit_right = pygame.sprite.collide_rect(self, self.player)
        self.rect.x -= 5

        self.rect.x -= 5
        hit_left = pygame.sprite.collide_rect(self, self.player)
        self.rect.x += 5

        self.rect.y -= 1
        hit_up = pygame.sprite.collide_rect(self, self.player)
        self.rect.y += 1

        self.rect.y += 1
        hit_down = pygame.sprite.collide_rect(self, self.player)
        self.rect.y -= 1

        if hit_up and not self.player.hit:
            self.dead = True
            self.kill_annimation()

        if (hit_down or hit_left or hit_right) and not self.player.hit and not self.dead:
            self.player.hit = True
            self.player.change_y = -10

    def kill_annimation(self):
        self.change_x = 0
        self.change_y = 0
        self.rect.y += 17
        PNJ_ressources.blob_ressources['dead_sound'].play()
        self.image = PNJ_ressources.blob_ressources['dead'][0]
        #pygame.time.wait(1000) #wait 1 second
        #self.kill() #destroy the object
