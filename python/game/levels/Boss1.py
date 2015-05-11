from Level import Level
from platforms.Platform import Platform
from platforms.MovingPlatform import MovingPlatform
from platforms.BoostPlatform import BoostPlatform
from platforms.Spike import Spike
from platforms.MovingSpike import MovingSpike
from platforms.EndPlatform import EndPlatform

from world.Parallax import Parallax
from platforms.SpecialPlatform import SpecialPlatform
from platforms.SpecialSpike import SpecialSpike
from PNJ.Blob import Blob
from PNJ.Dragon import Dragon

import constants
import pygame



class Boss1(Level):
    """Overview of the standard/easy way of the second stage"""

    def __init__(self, player, level_dif):

        Level.__init__(self, player)
        self.level_limit = -15000
        next_level = 0
        HEIGHT = constants.SCREEN_HEIGHT-20


        #array of platforms
        #[width, height, x, y]
        plats = [
                [300, HEIGHT, 0, 0],
                [5000, 20, 0, HEIGHT],
                #squares for spikes
                [30, 30, 800, HEIGHT-80],
                [30, 30, 1200, HEIGHT-120],
                #rectangle of spikes
                [150, 30, 1600, HEIGHT-100],
                #monster arena
                [100, 250, 2100, HEIGHT-250],
                [100, 250, 2800, HEIGHT-250],
                [150, 20, 2425, HEIGHT-300]
                ]

        #array of static spikes //considering spikes as image of 30x45 instead of 30x46
        #[x, y,width,height]

        bosses = [[1000, HEIGHT-400]]
        """Some background"""
        #adding parallax stuff to background along the level
        x_parallax=0
        back_p=[]
        front_p=[]
        while x_parallax < -self.level_limit + constants.SCREEN_WIDTH:
            back_p.append([x_parallax])
            front_p.append([x_parallax])
            x_parallax+=constants.SCREEN_WIDTH

        for boss in bosses:
            enemy = Dragon(self,player)
            enemy.rect.x = boss[0]
            enemy.rect.y = boss[1]
            self.pnj_list.add(enemy)


        for plat in plats:
            block = Platform(plat[0], plat[1])
            block.rect.x = plat[2]
            block.rect.y = plat[3]
            block.player = self.player
            block.level = self
            self.platform_list.add(block)

        end_plat = []
        end_plat.append([120, 20, 2000, HEIGHT-20, 0])

        #Parallax background
        for elem in back_p:
            x = elem[0]
            y = 0
            width = constants.SCREEN_WIDTH
            height = constants.SCREEN_HEIGHT
            mode = "back"
            level = self
            paral = Parallax(x,y,width,height,mode,level)
            self.back_world_list.add(paral)

        for elem in front_p:
            x = elem[0]
            y = 0
            width = constants.SCREEN_WIDTH
            height = constants.SCREEN_HEIGHT
            mode = "front"
            level = self
            paral = Parallax(x,y,width,height,mode,level)
            self.back_front_world_list.add(paral)

        #end platforms
        for plat in end_plat:
            block = EndPlatform(plat[0], plat[1])
            block.rect.x = plat[2]
            block.rect.y = plat[3]
            block.player = self.player
            block.level = self
            block.level_pointer = plat[4]
            next_player=None
            if player.name == 'hulk':
                next_player='bob'
            if player.name == 'bob':
                next_player='little_fat'
            if player.name == 'little_fat':
                next_player='hulk'
                block.change_difficulty = True
            block.character_pointer = next_player
            self.platform_list.add(block)
