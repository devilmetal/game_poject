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
        PNJ.update(self)
        self.calc_image()

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
