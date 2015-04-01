import constants
import pygame
from Platform import Platform

class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0

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
        hit = pygame.sprite.collide_rect(self, self.player) and not self.player.hit

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
        hit = pygame.sprite.collide_rect(self, self.player) and not self.player.hit

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
        self.player.rect.y += 2 + self.change_y
        hit = pygame.sprite.collide_rect(self.player, self) and not self.player.hit
        self.player.rect.y -= 2 + self.change_y

        if hit:

            self.player.change_y = self.change_y
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

            if self.player.location == 'block':
                self.player.rect.bottom = self.rect.top
        #bug correction
        else:
            if self.player.mov_plat == True and self.player.location != 'block':
                self.player.mov_plat = False

        if self.player.location == 'ground':
            self.player.mov_plat = False

        self.boundaries()


    def boundaries(self):

        self.player.rect.y += 10 + self.change_y
        hit = pygame.sprite.collide_rect(self.player, self) and not self.player.hit
        self.player.rect.y -= 10 + self.change_y
        # Check the boundaries and see if we need to reverse direction
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
            if self.player.location == "block" and hit and (self.player.status == "idle_r" or self.player.status =="idle_l"):
                self.player.change_y = self.change_y

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
            if self.player.location == "block" and hit and (self.player.status == "idle_r" or self.player.status =="idle_l"):
                self.player.change_x = self.change_x
