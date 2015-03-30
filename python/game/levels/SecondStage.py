from Level import Level
from platforms.Platform import Platform
from platforms.MovingPlatform import MovingPlatform
from platforms.BoostPlatform import BoostPlatform
from platforms.Spike import Spike
from platforms.MovingSpike import MovingSpike
from platforms.MagmaPlat import MagmaPlat
from platforms.MovingMagma import MovingMagma
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
				[3500, 20, 0, HEIGHT],
				#squares for spikes
				[30, 30, 800, HEIGHT-80],
				[30, 30, 1200, HEIGHT-120],
				#rectangle of spikes
				[150, 30, 1600, HEIGHT-100],
				#monster arena
				[100, 250, 2100, HEIGHT-250],
				[100, 250, 2800, HEIGHT-250],
				[150, 20, 2425, HEIGHT-300],
				#first platform in the air (after first round moving plat)
				[100, 20, 4750, HEIGHT-200],
				#square of spikes for the moving platform
				[30, 30, 5300, HEIGHT-350],
				[30, 30, 5700, HEIGHT-350],
				[20, 20, 5300, HEIGHT-220],
				[20, 20, 5700, HEIGHT-220],
				#2nd ground platform
				[5000, 20, 6200, HEIGHT],
				[50, 200, 6650, HEIGHT-200]
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
			[2, 2545, HEIGHT-281],
			#spikes for the first square in the air
			[0, 5300, HEIGHT-395],
			[1, 5329, HEIGHT-350],
			[2, 5300, HEIGHT-321],
			[3, 5253, HEIGHT-350],
			#spikes for the second square in the air
			[0, 5700, HEIGHT-395],
			[1, 5729, HEIGHT-350],
			[2, 5700, HEIGHT-321],
			[3, 5653, HEIGHT-350],
			]

		#[width, height, x, y, left bound, right bound, speed]
		horiz_plat = [
			[100, 20, 5000, HEIGHT-200, 5000, 6000, 2]
			]

		#array of special moving platforms
		#[width, height, x, y,
		#top bound, bottom bound, left bound, right bound,
		#speed up, speed down, speed left, speed right,
		#is moving round, clockwise movement]
		round_moving = [
			#first
			[100, 20, 3550, HEIGHT-20, 
			HEIGHT-220, HEIGHT, 3550, 3850,
			2, 2, 2, 2,
			True, True],
			#second
			[100, 20, 4000, HEIGHT-100,
			HEIGHT-300, HEIGHT-80, 4000, 4500,
			2, 2, 3, 3,
			True, False],
			#moving square of spike
			[30, 30, 6350, HEIGHT-130,
			HEIGHT-210, HEIGHT-100, 6350, 6550,
			1, 1, 3, 3,
			True, True]
			]

		#array of special moving platforms
		#[orientation, x, y, top bound, bottom bound, left bound, right bound,
		#speed up, speed down, speed left, speed right, is moving round, clockwise movement]
		round_spike=[
			[0, 6350, HEIGHT-175, HEIGHT-255, HEIGHT-129, 6350, 6550,
			1, 1, 3, 3, True, True],
			[1, 6378, HEIGHT-130, HEIGHT-210, HEIGHT-100, 6378, 6578,
			1, 1, 3, 3, True, True],
			[2, 6350, HEIGHT-101, HEIGHT-181, HEIGHT-55, 6350, 6550,
			1, 1, 3, 3, True, True],
			[3, 6304, HEIGHT-130, HEIGHT-210, HEIGHT-100, 6304, 6504,
			1, 1, 3, 3, True, True]
			]
		

		#magma platform
		magma = [
			[200, 50, 6700, HEIGHT-50]
			]

		#adding tree to background along the level
		x_trees=0
		back_trees=[]
		while x_trees < -self.level_limit:
			back_trees.append([0,x_trees,HEIGHT - 150])
			x_trees+=200



		"""Generation of the level design"""
		for tree in back_trees:
			block = Tree(tree[0])
			block.rect.x = tree[1]
			block.rect.y = tree[2]
			self.back_world_list.add(block)

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

		for plat in horiz_plat:
			block = MovingPlatform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.boundary_left = plat[4]
			block.boundary_right = plat[5]
			block.change_x = plat[6]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		#round moving platform.
		for plat in round_moving:
			block = SpecialPlatform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.boundary_top = plat[4]
			block.boundary_bottom = plat[5]
			block.boundary_left = plat[6]
			block.boundary_right = plat[7]
			block.change_y_u = -plat[8]
			block.change_y_d = plat[9]
			block.change_x_l = -plat[10]
			block.change_x_r = plat[11]
			block.round_mov = plat[12]
			block.clockwise = plat[13]
			if plat[13] == False:
				block.change_y = plat[9]
			else:
				block.change_y = -plat[8]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		#round moving spike.
		for spike in round_spike:
			block = SpecialSpike(spike[0])
			block.rect.x = spike[1]
			block.rect.y = spike[2]
			block.boundary_top = spike[3]
			block.boundary_bottom = spike[4]
			block.boundary_left = spike[5]
			block.boundary_right = spike[6]
			block.change_y_u = -spike[7]
			block.change_y_d = spike[8]
			block.change_x_l = -spike[9]
			block.change_x_r = spike[10]
			block.round_mov = spike[11]
			block.clockwise = spike[12]
			if plat[13] == False:
				block.change_y = spike[8]
			else:
				block.change_y = -spike[7]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		for plat in magma:
			block = MagmaPlat(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			block.image.fill(constants.RED)
			self.platform_list.add(block)