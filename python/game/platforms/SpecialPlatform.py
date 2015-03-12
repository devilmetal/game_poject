import constants
import pygame
from Platform import Platform

class SpecialPlatform(Platform):
    """ Platform with specific movements, i.e. for example its speed while moving up
    is faster than while moving down, or it can make a pause when it reach the bottom boundary
    or top boundary """
    change_x = 0
    change_y = 0


    change_x_r = 0
    change_x_l = 0
    change_y_u = 0
    change_y_d = 0
    pause_up = 0
    pause_down = 0
    pause_right = 0
    pause_left = 0

    pause = False
    time = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    player = None

    level = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)

        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right


        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)

        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        #check if the player is on top of the movingplatform and move it with it.

        #check if the player is on top of a lateral moving platform and make it move with it.
        self.player.rect.y += 2
        hit = pygame.sprite.collide_rect(self.player, self)
        self.player.rect.y -= 2

        if hit:
            if self.player.location == 'block' and (self.player.status == 'idle_l' or self.player.status == 'idle_r') :
                self.player.change_x = self.change_x
                self.player.mov_plat = True
            elif self.player.location == 'block' and self.player.status == 'move_r':
                self.player.change_x = self.change_x + 6
                self.player.mov_plat = False
            elif self.player.location == 'block' and self.player.status == 'move_l':
                self.player.change_x = self.change_x - 6
                self.player.mov_plat = False
            else :
                self.player.mov_plat = False

        if self.player.location == 'ground':
            self.player.mov_plat = False



        # Check the boundaries and see if we have a pause and if we need to reverse direction.

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
        if (cur_pos < self.boundary_left or cur_pos > self.boundary_right):
            self.change_x *= -1
