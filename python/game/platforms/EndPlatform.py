import constants
import pygame
from Platform import Platform

class EndPlatform(Platform):
    """ This is a fancier platform that can actually move. """

    player = None

    level = None

    level_pointer = 0

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """


        #check if the player is on top of a lateral moving platform and make it move with it.
        self.player.rect.y += 2
        hit = pygame.sprite.collide_rect(self.player, self) and not self.player.hit
        self.player.rect.y -= 2

        if hit:
            self.level.game.current_level_nbr = self.level_pointer
            self.level.game.checkpoint=False
            self.level.game.load_level(self.level_pointer, self.level.game.level_dif)
