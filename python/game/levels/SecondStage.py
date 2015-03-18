from Level import Level
from platforms.Platform import Platform
from platforms.MovingPlatform import MovingPlatform
from platforms.BoostPlatform import BoostPlatform
from platforms.Spike import Spike
from platforms.MovingSpike import MovingSpike
from world.Tree import Tree
from platforms.SpecialPlatform import SpecialPlatform
from platforms.SpecialSpike import SpecialSpike
from PNJ.Blob import Blob

import constants
import pygame


start_x = 0
start_y = 0


class SecondStage(Level):
	"""Overview of the standard/easy way of the second stage"""

	def __init__(self, player):

		Level.__init__(self, player)

		self.level_limit = -14300

		HEIGHT = constants.SCREEN_HEIGHT-20

		#starting positions
		self.start_x = 350
		self.start_y = HEIGHT - player.rect.height

		#array of platforms
		level = [
				#just two little thingy to add a monster TODO:Remove
				[300, HEIGHT, 0, 0],
				[500, 20, 0, HEIGHT]
				]


		for plat in level:
			block = Platform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)