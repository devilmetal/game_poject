from PNJ import PNJ

import constants
import routines
import pygame

class Blob(PNJ):

    def __init__(self,direction,speed):

        # Call the parent constructor
        PNJ.__init__(self,direction,speed)

        #Loading images
        self.left_blob1, self.left_blob1_rect =  routines.load_png('pnj/enemy/blob/left_blob1.png')
        self.left_blob2, self.left_blob2_rect =  routines.load_png('pnj/enemy/blob/left_blob2.png')
        self.left_blob3, self.left_blob3_rect =  routines.load_png('pnj/enemy/blob/left_blob3.png')
        self.left_blob4, self.left_blob4_rect =  routines.load_png('pnj/enemy/blob/left_blob4.png')
        self.left_blob5, self.left_blob5_rect =  routines.load_png('pnj/enemy/blob/left_blob5.png')
        self.left_blob6, self.left_blob6_rect =  routines.load_png('pnj/enemy/blob/left_blob6.png')
        self.right_blob1, self.right_blob1_rect =  routines.load_png('pnj/enemy/blob/right_blob1.png')
        self.right_blob2, self.right_blob2_rect =  routines.load_png('pnj/enemy/blob/right_blob2.png')
        self.right_blob3, self.right_blob3_rect =  routines.load_png('pnj/enemy/blob/right_blob3.png')
        self.right_blob4, self.right_blob4_rect =  routines.load_png('pnj/enemy/blob/right_blob4.png')
        self.right_blob5, self.right_blob5_rect =  routines.load_png('pnj/enemy/blob/right_blob5.png')
        self.right_blob6, self.right_blob6_rect =  routines.load_png('pnj/enemy/blob/right_blob6.png')

        #Frame incr. + frame speed
        self.frame_inc=0
        self.speed_frame = 3

        if self.direction > 0:
            #we go left
            self.image = self.left_blob1
            self.rect = self.left_blob1_rect
        else:
            #we go right
            self.image = self.right_blob1
            self.rect = self.right_blob1_rect

    def update(self):
        # Call the parent update
        PNJ.update(self)
        self.calc_image()

    def calc_image(self):
        if self.change_x < 0:
            #we go left
            if self.frame_inc in range(0,self.speed_frame):
                self.image = self.left_blob1
                self.frame_inc+=1
            elif self.frame_inc in range(self.speed_frame,2*self.speed_frame):
                self.image = self.left_blob2
                self.frame_inc+=1
            elif self.frame_inc in range(2*self.speed_frame,3*self.speed_frame):
                self.image = self.left_blob3
                self.frame_inc+=1
            elif self.frame_inc in range(3*self.speed_frame,4*self.speed_frame):
                self.image = self.left_blob4
                self.frame_inc+=1
            elif self.frame_inc in range(4*self.speed_frame,5*self.speed_frame):
                self.image = self.left_blob5
                self.frame_inc+=1
            else:
                self.image = self.left_blob6
                self.frame_inc=0
        else:
            #we go right
            #we go left
            if self.frame_inc in range(0,self.speed_frame):
                self.image = self.right_blob1
                self.frame_inc+=1
            elif self.frame_inc in range(self.speed_frame,2*self.speed_frame):
                self.image = self.right_blob2
                self.frame_inc+=1
            elif self.frame_inc in range(2*self.speed_frame,3*self.speed_frame):
                self.image = self.right_blob3
                self.frame_inc+=1
            elif self.frame_inc in range(3*self.speed_frame,4*self.speed_frame):
                self.image = self.right_blob4
                self.frame_inc+=1
            elif self.frame_inc in range(4*self.speed_frame,5*self.speed_frame):
                self.image = self.right_blob5
                self.frame_inc+=1
            else:
                self.image = self.right_blob6
                self.frame_inc=0
