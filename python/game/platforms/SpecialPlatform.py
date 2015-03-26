import constants
import pygame
from Platform import Platform
from MovingPlatform import MovingPlatform

class SpecialPlatform(MovingPlatform):
    """ Platform with specific movements, i.e. for example its speed while moving up
    is faster than while moving down, or it can make a pause when it reach the bottom boundary
    or top boundary """

    change_x_r = 0
    change_x_l = 0
    change_y_u = 0
    change_y_d = 0
    pause_up = 0
    pause_down = 0
    pause_right = 0
    pause_left = 0
    pause = False

    round_mov = False
    clockwise = False
    time = 0
    vert = False

    def update(self):
        """ Special case of the moving platforms"""

        MovingPlatform.update(self)


    def boundaries(self):


        #cur_pos = self.rect.x - self.level.world_shift
        # Check the boundaries and see if we have a pause and if we need to reverse direction.
        if self.round_mov:
            cur_pos = self.rect.x - self.level.world_shift
            self.player.rect.y += 2 + self.change_y
            hit = pygame.sprite.collide_rect(self.player, self) and not self.player.hit
            self.player.rect.y -= 2 + self.change_y

            #clockwise movement
            if self.rect.top < self.boundary_top and self.clockwise and self.change_y != 0:
                if hit:
                    self.player.change_x = self.change_x_r
                self.change_x = self.change_x_r
                self.change_y = 0
            elif cur_pos > self.boundary_right and self.clockwise and self.change_x != 0:
                if hit:
                    self.player.change_x = 0
                self.change_x = 0
                self.change_y = self.change_y_d
            elif self.rect.bottom > self.boundary_bottom and self.clockwise and self.change_y != 0:
                if hit:
                    self.player.change_x = self.change_x_l
                self.change_x = self.change_x_l
                self.change_y = 0
            elif cur_pos < self.boundary_left and self.clockwise and self.change_x != 0:
                if hit:
                    self.player.change_x = 0
                self.change_x = 0
                self.change_y = self.change_y_u

            #counter clockwise
            elif self.rect.top < self.boundary_top and not self.clockwise and self.change_y != 0:
                self.player.change_x = self.change_x_l
                self.change_x = self.change_x_l
                self.change_y = 0
            elif cur_pos > self.boundary_right and not self.clockwise and self.change_x != 0:
                self.player.change_x = 0
                self.change_x = 0
                self.change_y = self.change_y_u
            elif self.rect.bottom > self.boundary_bottom and not self.clockwise and self.change_y != 0:
                self.player.change_x = self.change_x_r
                self.change_x = self.change_x_r
                self.change_y = 0
            elif cur_pos < self.boundary_left and not self.clockwise and self.change_x != 0:
                self.player.change_x = 0
                self.change_x = 0
                self.change_y = self.change_y_d
            

        else:
            """
            up/down plateforms
            """
            #case where we have a pause down
            if self.rect.bottom > self.boundary_bottom and not self.pause:
                self.change_y = 0
                self.pause = True
                self.time = self.pause_down

            #if we have to wait, i.e. pause == True
            if self.rect.bottom > self.boundary_bottom and self.pause:
                if self.time > 0:
                    self.time -= 1
                else:
                    self.change_y = self.change_y_u #set the speed from bottom to top
                    self.pause = False


            #case where we have a pause up
            if self.rect.top < self.boundary_top and not self.pause:
                self.change_y = 0
                self.pause = True
                self.time = self.pause_up

            #if we have to wait, i.e. pause == True
            if self.rect.top < self.boundary_top and self.pause:
                if self.time > 0:
                    self.time -= 1
                else:
                    self.change_y = self.change_y_d #set the speed from top to bottom
                    self.pause = False




            """
            left/right plateforms
            """
            cur_pos = self.rect.x - self.level.world_shift

            #case where we have a pause on the left
            if cur_pos < self.boundary_left and not self.pause:
                self.change_x = 0
                self.pause = True
                self.time = self.pause_left

            if cur_pos < self.boundary_left and self.pause:
                if self.time > 0:
                    self.time -= 1
                else:
                    self.change_x = self.change_x_r
                    self.pause = False

            
            #case where we have a pause on the left
            if cur_pos > self.boundary_right and not self.pause:
                self.change_x = 0
                self.pause = True
                self.time = self.pause_right

            if cur_pos > self.boundary_right and self.pause:
                if self.time > 0:
                    self.time -= 1
                else:
                    self.change_x = self.change_x_l
                    self.pause = False
