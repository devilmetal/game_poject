import constants
import pygame
from Platform import Platform
import platform_ressources

class CheckPoint(Platform):
    """ This is a fancier platform that can actually move. """
    platform_ressources.init_checkpoint_ressources()
    player = None
    level = None
    checked = False
    img = platform_ressources.checkpoint_ressources['flag'][0]
    img2 = platform_ressources.checkpoint_ressources['bar'][0]
    img.blit(img2,(0,0))
    #img2 = pygame.Surface((50, 5))
    x = 2700
    y = 0
    #img = img.convert()
    #img2 = img2.convert()
    #img.fill((0, 0, 0))
    #img2.fill((255,255,0))
    speed = 4
    camp = False
    finished = False

    def draw_camp(self):

        #So the checkpoint is validate even if the player left the platform before the annimation end.
        if self.y == 0:
            self.y = self.rect.y
        HEIGHT = constants.SCREEN_HEIGHT-20
        if self.camp and self.finished == False:
            #just draw the camp (player already touch the checkpoint)
            self.y = self.rect.y-self.img.get_height()

        if self.checked:
            #make the camp appear when player touch checkpoint for the first time
            if self.y >= self.rect.y-self.img.get_height():
                self.y -= self.speed
            else:
                self.checked = False
            self.finished = True

        return self.img, (self.x,self.y)




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
            tmp_x = self.rect.x+int((self.rect.width-self.player.rect.width)/2)-self.level.world_shift
            tmp_y = self.rect.y-self.player.rect.height
            if self.level.game.start_x != tmp_x and self.level.game.start_y != tmp_y:
                #new checkpoint encountered!
                self.checked = True
                self.camp = False
                if self.finished:
                    self.level.game.start_x = tmp_x
                    self.level.game.start_y = tmp_y
                    self.level.game.checkpoint = True
                    self.finished = False

            else:
                self.camp = True
