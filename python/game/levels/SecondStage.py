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



class SecondStage(Level):
	"""Overview of the standard/easy way of the second stage"""

	def __init__(self, player, level_dif):

		Level.__init__(self, player)

		self.level_limit = -15000
		next_level = 1
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
		#[orientation, x, y]
		spikes = [
			#1st square's spikes
			[0, 800, HEIGHT-125],
			[1, 829, HEIGHT-80],
			[2, 800, HEIGHT-51],
			[3, 753, HEIGHT-80],
			#2nd square's spikes
			[0, 1200, HEIGHT-165],
			[1, 1229, HEIGHT-120],
			[2, 1200, HEIGHT-91],
			[3, 1153, HEIGHT-120],
			#rectangle of spikes
			[0, 1600, HEIGHT-145],
			[0, 1630, HEIGHT-145],
			[0, 1660, HEIGHT-145],
			[0, 1690, HEIGHT-145],
			[0, 1720, HEIGHT-145],
			[1, 1749, HEIGHT-100],
			[2, 1600, HEIGHT-71],
			[2, 1630, HEIGHT-71],
			[2, 1660, HEIGHT-71],
			[2, 1690, HEIGHT-71],
			[2, 1720, HEIGHT-71],
			[3, 1553, HEIGHT-100],
			#spikes of th arena
			[0, 2425, HEIGHT-345],
			[0, 2455, HEIGHT-345],
			[0, 2485, HEIGHT-345],
			[0, 2515, HEIGHT-345],
			[0, 2545, HEIGHT-345],
			[2, 2425, HEIGHT-281],
			[2, 2455, HEIGHT-281],
			[2, 2485, HEIGHT-281],
			[2, 2515, HEIGHT-281],
			[2, 2545, HEIGHT-281]
			]



		for plat in plats:
			block = Platform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		for spike in spikes:
			block = Spike(spike[0])
			block.rect.x = spike[1]
			block.rect.y = spike[2]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)
