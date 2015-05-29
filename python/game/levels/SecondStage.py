from Level import Level
from platforms.Platform import Platform
from platforms.MovingPlatform import MovingPlatform
from platforms.BoostPlatform import BoostPlatform
from platforms.Spike import Spike
from platforms.MovingSpike import MovingSpike
from platforms.MagmaPlat import MagmaPlat
from world.Parallax import Parallax
from platforms.SpecialPlatform import SpecialPlatform
from platforms.SpecialSpike import SpecialSpike
from platforms.EndPlatform import EndPlatform
from PNJ.Blob import Blob
from world.Sign import Sign
from PNJ.Fairy import Fairy
from platforms.CheckPoint import CheckPoint

import constants
import pygame
import routines



class SecondStage(Level):
	"""Overview of the standard/easy way of the second stage"""

	def __init__(self, player, level_dif):

		Level.__init__(self, player)

		self.level_limit = -16000
		self.level_name = "Stage 2"
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
			#little square for the moving platform
			[20, 20, 5300, HEIGHT-220],
			[20, 20, 5700, HEIGHT-220],
			#2nd ground platform
			[1900, 20, 6200, HEIGHT],
			#wall containing some magma
			[50, 200, 6650, HEIGHT-200],
			[50, 70, 7150, HEIGHT-70],
			[50, 150, 7500, HEIGHT-150],
			[50, 150, 8000, HEIGHT-150],
			[50, 300, 8050, HEIGHT-300],
			#platform in the long magma moving flour
			[100, 20, 8300, HEIGHT-200],
			[800, 20, 8600, HEIGHT-100],
			[100, 20, 9600, HEIGHT-200],
			[50, 300, 10000, HEIGHT-300],
			#third ground
			[2500, 20, 10000, HEIGHT],
			[30, 30, 11900, HEIGHT-30],
			[100, 220, 12500, HEIGHT-200],
			[100, 220, 13800, HEIGHT-200],
			#last square of spikes
			[30, 30, 14400, HEIGHT-370],
			[1500, 20, 15200, HEIGHT],
			#platform for fairy
			[50, 10, 6450, HEIGHT-370],
			[50, 10, 6450, HEIGHT-290]
		]

		# checkpoints
		#[top-left x, top-left , width, height]
		checkpoints = [
			[50, 20, 7600, HEIGHT-20]
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
			#spikes of the arena
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
			#last spikes for squares
			[0, 14400, HEIGHT-414],
			[1, 14428, HEIGHT-370],
			[2, 14400, HEIGHT-342],
			[3, 14354, HEIGHT-370]
		]


		#array of special moving platforms
		#[width, height, x, y,
		#top bound, bottom bound, left bound, right bound,
		#speed up, speed down, speed left, speed right,
		#is moving round, clockwise movement]
		round_moving = [
			#first
			[100, 20, 3550, HEIGHT-20,
			HEIGHT-220, HEIGHT, 3550, 3800,
			2, 2, 2, 2,
			True, True],
			#second
			[100, 20, 4100, HEIGHT-100,
			HEIGHT-300, HEIGHT-80, 4100, 4500,
			2, 2, 3, 3,
			True, False]
		]


		#array of special moving platforms
		#[width, height, x, y,
		#top bound, bottom bound, left bound, right bound,
		#speed up, speed down, speed left, speed right,
		#is moving round, clockwise movement
		#[[array of subblock]]]
		block_round_moving = [
			#moving square of spike
			#last moving squares on the ground & last moving spikes
			#1st
			[30, 30, 10400, HEIGHT-100,
			HEIGHT-180, HEIGHT-70, 10400, 10700,
			2, 2, 3, 3,
			True, True,
				[
				#1st square
				[0, 10400, HEIGHT-145, HEIGHT-225, HEIGHT-99, 10400, 10700,
				2, 2, 3, 3, True, True],
				[1, 10428, HEIGHT-100, HEIGHT-180, HEIGHT-70, 10428, 10728,
				2, 2, 3, 3, True, True],
				[2, 10400, HEIGHT-71, HEIGHT-151, HEIGHT-25, 10400, 10700,
				2, 2, 3, 3, True, True],
				[3, 10354, HEIGHT-100, HEIGHT-180, HEIGHT-70, 10354, 10654,
				2, 2, 3, 3, True, True],
				]
			],


			#3rd (2nd if easy)
			[30, 30, 11000, HEIGHT-100,
			HEIGHT-180, HEIGHT-70, 11000, 11300,
			2, 2, 3, 3,
			True, True,
				[
				#3rd square (2nd if easy)
				[0, 11000, HEIGHT-145, HEIGHT-225, HEIGHT-99, 11000, 11300,
				2, 2, 3, 3, True, True],
				[1, 11028, HEIGHT-100, HEIGHT-180, HEIGHT-70, 11028, 11328,
				2, 2, 3, 3, True, True],
				[2, 11000, HEIGHT-71, HEIGHT-151, HEIGHT-25, 11000, 11300,
				2, 2, 3, 3, True, True],
				[3, 10954, HEIGHT-100, HEIGHT-180, HEIGHT-70, 10954, 11254,
				2, 2, 3, 3, True, True]
				]
			]
		]


		#array of special moving platforms
		#[orientation, x, y, top bound, bottom bound, left bound, right bound,
		#speed up, speed down, speed left, speed right, is moving round, clockwise movement]
		round_spike=[
			#moved into block_round_moving : [array of subblock]
		]

		#magma platform
		#[width, height, x, y]
		magma = [
			[300, 50, 7200, HEIGHT-50],
			[1200, 120, 12600, HEIGHT-100]
		]


		#if we are on a platform that should make us go to the next level
		#[width, height, top-left x, top-left y, next level]
		end_plat = []
		end_plat.append([120, 20, 16100, HEIGHT, 3, 'bob'])

		signs = [
			[15800, HEIGHT,"Boss ==>"],
		]


		#adding parallax stuff to background along the level
		x_parallax=0
		back_p=[]
		front_p=[]
		while x_parallax < -self.level_limit + constants.SCREEN_WIDTH:
			back_p.append([x_parallax])
			front_p.append([x_parallax])
			x_parallax+=constants.SCREEN_WIDTH

		"""Some foes"""
		blobs = [
			#between star spikes
			[1500, HEIGHT-30, 1, 2],
			[1500, HEIGHT-30, 1, 3],
			[1400, HEIGHT-30, 1, 2],
			[1800, HEIGHT-30, 1, 1],
			#spikes arena
			[2300, HEIGHT-30, 1, 2],
			[2300, HEIGHT-30, 1, 3],
			#middle checkpoint
			[7650, HEIGHT-30, 1, 2],
			[7650, HEIGHT-30, 1, 3],
			#between star spikes before last checkpoint
			[11700, HEIGHT-30, -1, 4],
			[11500, HEIGHT-30, -1, 3],
			[11300, HEIGHT-30, 1, 2],
			#just after last checkpoint
			[11950, HEIGHT-30, 1, 4],
			[11950, HEIGHT-30, 1, 2]
		]

		fairy = [
			# [520,HEIGHT-95, player],
			[6460, HEIGHT-335, player]
		]



		###################################################################################
		###################################################################################

		"""Generation of the standard level's elements"""

		#static platforms
		for plat in plats:
			block = Platform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		#static spikes
		for spike in spikes:
			block = Spike(spike[0])
			block.rect.x = spike[1]
			block.rect.y = spike[2]
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

		#block round moving platform.
		for plat in block_round_moving:
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
			#subblock
			for sub in plat[14]:
				subblock = SpecialSpike(sub[0])
				subblock.rect.x = sub[1]
				subblock.rect.y = sub[2]
				subblock.boundary_top = sub[3]
				subblock.boundary_bottom = sub[4]
				subblock.boundary_left = sub[5]
				subblock.boundary_right = sub[6]
				subblock.change_y_u = -sub[7]
				subblock.change_y_d = sub[8]
				subblock.change_x_l = -sub[9]
				subblock.change_x_r = sub[10]
				subblock.round_mov = sub[11]
				subblock.clockwise = sub[12]
				if sub[12] == False:
					subblock.change_y = sub[8]
				else:
					subblock.change_y = -sub[7]
				subblock.player = self.player
				subblock.level = self
				block.subblock.add(subblock)

			self.mov_plat_list.add(block)


		#static magma
		for plat in magma:
			block = MagmaPlat(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			self.magma_list.add(block)

		for plat in checkpoints:
			block = CheckPoint(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			#CheckPoint is white!
			block.image.fill(constants.WHITE)
			self.platform_list.add(block)

		for plat in end_plat:
			block = EndPlatform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			block.level_pointer = plat[4]
			block.character_pointer = plat[5]
			self.platform_list.add(block)


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

		for elem in signs:
			sign = Sign(elem[0],elem[1],elem[2])
			self.pnj_list.add(sign)

		for pnj in blobs:
			enemy = Blob(pnj[2],pnj[3])
			enemy.rect.x = pnj[0]
			enemy.rect.y = pnj[1]
			enemy.player=self.player
			enemy.level=self
			self.pnj_list.add(enemy)

		for pnj in fairy:
			pixie = Fairy(pnj[0],pnj[1],pnj[2])
			self.pnj_list.add(pixie)


		###################################################################################
		###################################################################################


		"""Specific platform for the difficulty level"""

		#easy

		#[width, height, x, y]
		easy_plats = [
			#platform between the round moving platform
			[100, 20, 3950, HEIGHT-200],
			#platform in the first magma arena
			[50, 100, 6900, HEIGHT-100],
			[100, 20, 13000, HEIGHT-250],
			[100, 20, 14800, HEIGHT-250]
		]

		#[width, height, x, y]
		easy_magma = [
			[200, 50, 6700, HEIGHT-50],
			[200, 50, 6950, HEIGHT-50],
		]

		#[widht, height, x, y, left bound, right bound, speed]
		easy_horiz_plat = [
			[150, 20, 4850, HEIGHT-200, 4850, 6000, 3],
			[150, 20, 13900, HEIGHT-250, 13900, 14600, 2]
		]


		#[width, height, x, y, top bound, bottom bound, speed]
		easy_vert_plat = [
			[100, 20, 12800, HEIGHT-250, HEIGHT-250, HEIGHT-50, 1],
			[100, 20, 13200, HEIGHT-100, HEIGHT-250, HEIGHT-50, 1],
			[50, 20, 13500, HEIGHT-70, HEIGHT-250, HEIGHT-50, 1]
		]


		easy_block_round_moving = [
			[30, 30, 6350, HEIGHT-130,
			HEIGHT-210, HEIGHT-100, 6350, 6550,
			1, 1, 3, 3,
			True, True,
				[
				#array of special moving platforms
				#[orientation, x, y, top bound, bottom bound, left bound, right bound,
				#speed up, speed down, speed left, speed right, is moving round, clockwise movement]
				[0, 6350, HEIGHT-175, HEIGHT-255, HEIGHT-129, 6350, 6550,
				1, 1, 3, 3, True, True],
				[1, 6378, HEIGHT-130, HEIGHT-210, HEIGHT-100, 6378, 6578,
				1, 1, 3, 3, True, True],
				[2, 6350, HEIGHT-101, HEIGHT-181, HEIGHT-55, 6350, 6550,
				1, 1, 3, 3, True, True],
				[3, 6304, HEIGHT-130, HEIGHT-210, HEIGHT-100, 6304, 6504,
				1, 1, 3, 3, True, True]
				]
			]
		]


		#[width, height, x, y, top bound, bottom bound, speed, pause]
		easy_moving_magma = [
			[1900, 270, 8100, HEIGHT, HEIGHT-250, HEIGHT+270, 1, 240]
		]

		easy_checkpoints = [
			[50, 20, 3300, HEIGHT-20],
			[50, 20, 11800, HEIGHT-20]
		]




		###################################################################################

		#medium

		#[width, height, x, y]
		medium_plats = [
			[50, 20, 3950, HEIGHT-200],
			#square of spikes for the moving platform
			[30, 30, 5300, HEIGHT-350],
			[30, 30, 5700, HEIGHT-350],
			#platform in the first magma arena
			[50, 100, 6900, HEIGHT-100],
			#square for spikes in the middle of the platform where moving magma stands
			[30, 30, 9000, HEIGHT-200]
		]

		#[orientation, x, y]
		medium_spikes = [
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
			#spikes in the middle of the platform where moving magma stands
			[0, 9000, HEIGHT-244],
			[1, 9028, HEIGHT-200],
			[2, 9000, HEIGHT-172],
			[3, 8954, HEIGHT-200]
		]

		medium_horiz_plat = [
			[100, 20, 4850, HEIGHT-200, 4850, 5900, 2],
			[100, 20, 13950, HEIGHT-250, 13950, 15000, 3]
		]

		#[orientation, top-left x, top-left y, left bound, right bound, speed,
		#[array of subblock]]
		medium_horiz_spikes = [
			[3, 6800, HEIGHT-130, 6800, 7300, 5,
				[
				[1, 6845, HEIGHT-130, 6845, 7345, 5]
				]
			]
		]

		#[width, height, x, y, top bound, bottom bound, speed]
		medium_vert_plat = [
			[100, 20, 12800, HEIGHT-250, HEIGHT-250, HEIGHT-50, 2],
			[100, 20, 13200, HEIGHT-100, HEIGHT-250, HEIGHT-50, 2],
			[50, 20, 13500, HEIGHT-70, HEIGHT-250, HEIGHT-50, 1]
		]

		#[orientation, top-left x, top-left y, top bound, bottom bound, speed,
		#[[array of subblock]]]
		medium_vert_spikes = [
			#stalagtite spikes at the end
			[2, 15400, HEIGHT-46, HEIGHT-200, HEIGHT, 4,
				[
				[2, 15430, HEIGHT-66, HEIGHT-200, HEIGHT, 4],
				[2, 15460, HEIGHT-86, HEIGHT-200, HEIGHT, 4],
				[2, 15490, HEIGHT-106, HEIGHT-200, HEIGHT, 4],
				[2, 15520, HEIGHT-126, HEIGHT-200, HEIGHT, 4],
				[2, 15550, HEIGHT-146, HEIGHT-200, HEIGHT, 4],
				[2, 15580, HEIGHT-166, HEIGHT-200, HEIGHT, 4],
				[2, 15610, HEIGHT-186, HEIGHT-200, HEIGHT, 4],
				[2, 15640, HEIGHT-194, HEIGHT-200, HEIGHT, -4],
				[2, 15670, HEIGHT-174, HEIGHT-200, HEIGHT, -4],
				[2, 15700, HEIGHT-154, HEIGHT-200, HEIGHT, -4],
				[2, 15730, HEIGHT-134, HEIGHT-200, HEIGHT, -4],
				[2, 15760, HEIGHT-114, HEIGHT-200, HEIGHT, -4],
				[2, 15790, HEIGHT-94, HEIGHT-200, HEIGHT, -4],
				[2, 15820, HEIGHT-74, HEIGHT-200, HEIGHT, -4],
				[2, 15850, HEIGHT-54, HEIGHT-200, HEIGHT, -4],
				#stalagmite spikes at the end
				[0, 15400, HEIGHT-90, HEIGHT-244, HEIGHT-44, 4],
				[0, 15430, HEIGHT-110, HEIGHT-244, HEIGHT-44, 4],
				[0, 15460, HEIGHT-130, HEIGHT-244, HEIGHT-44, 4],
				[0, 15490, HEIGHT-150, HEIGHT-244, HEIGHT-44, 4],
				[0, 15520, HEIGHT-170, HEIGHT-244, HEIGHT-44, 4],
				[0, 15550, HEIGHT-190, HEIGHT-244, HEIGHT-44, 4],
				[0, 15580, HEIGHT-210, HEIGHT-244, HEIGHT-44, 4],
				[0, 15610, HEIGHT-230, HEIGHT-244, HEIGHT-44, 4],
				[0, 15640, HEIGHT-238, HEIGHT-244, HEIGHT-44, -4],
				[0, 15670, HEIGHT-218, HEIGHT-244, HEIGHT-44, -4],
				[0, 15700, HEIGHT-198, HEIGHT-244, HEIGHT-44, -4],
				[0, 15730, HEIGHT-178, HEIGHT-244, HEIGHT-44, -4],
				[0, 15760, HEIGHT-158, HEIGHT-244, HEIGHT-44, -4],
				[0, 15790, HEIGHT-138, HEIGHT-244, HEIGHT-44, -4],
				[0, 15820, HEIGHT-118, HEIGHT-244, HEIGHT-44, -4],
				[0, 15850, HEIGHT-98, HEIGHT-244, HEIGHT-44, -4],
				]
			]
		]


		#array of special moving platforms
		#[width, height, x, y,
		#top bound, bottom bound, left bound, right bound,
		#speed up, speed down, speed left, speed right,
		#is moving round, clockwise movement,
		#[[array of subblock, see medium_round_spikes]]]
		medium_block_round_moving = [
			[30, 30, 6350, HEIGHT-130,
			HEIGHT-210, HEIGHT-100, 6350, 6550,
			1, 1, 3, 3,
			True, True,
				[
				#array of special moving spikes
				#[orientation, x, y, top bound, bottom bound, left bound, right bound,
				#speed up, speed down, speed left, speed right, is moving round, clockwise movement]
				[0, 6350, HEIGHT-175, HEIGHT-255, HEIGHT-129, 6350, 6550,
				1, 1, 3, 3, True, True],
				[1, 6378, HEIGHT-130, HEIGHT-210, HEIGHT-100, 6378, 6578,
				1, 1, 3, 3, True, True],
				[2, 6350, HEIGHT-101, HEIGHT-181, HEIGHT-55, 6350, 6550,
				1, 1, 3, 3, True, True],
				[3, 6304, HEIGHT-130, HEIGHT-210, HEIGHT-100, 6304, 6504,
				1, 1, 3, 3, True, True]
				]
			],

			#last moving squares on the ground
			#2nd
			[30, 30, 10700, HEIGHT-100,
			HEIGHT-180, HEIGHT-70, 10700, 11000,
			2, 2, 3, 3,
			True, True,
				[
				#2nd square
				[0, 10700, HEIGHT-145, HEIGHT-225, HEIGHT-99, 10700, 11000,
				2, 2, 3, 3, True, True],
				[1, 10728, HEIGHT-100, HEIGHT-180, HEIGHT-70, 10728, 11028,
				2, 2, 3, 3, True, True],
				[2, 10700, HEIGHT-71, HEIGHT-151, HEIGHT-25, 10700, 11000,
				2, 2, 3, 3, True, True],
				[3, 10654, HEIGHT-100, HEIGHT-180, HEIGHT-70, 10654, 10954,
				2, 2, 3, 3, True, True]
				]
			],

			#4th
			[30, 30, 11300, HEIGHT-100,
			HEIGHT-180, HEIGHT-70, 11300, 11600,
			2, 2, 3, 3,
			True, True,
				[
				#4th square
				[0, 11300, HEIGHT-145, HEIGHT-225, HEIGHT-99, 11300, 11600,
				2, 2, 3, 3, True, True],
				[1, 11328, HEIGHT-100, HEIGHT-180, HEIGHT-70, 11328, 11628,
				2, 2, 3, 3, True, True],
				[2, 11300, HEIGHT-71, HEIGHT-151, HEIGHT-25, 11300, 11600,
				2, 2, 3, 3, True, True],
				[3, 11254, HEIGHT-100, HEIGHT-180, HEIGHT-70, 11254, 11554,
				2, 2, 3, 3, True, True],
				]
			],

			#last moving square of spike
			[30, 30, 14600, HEIGHT-360,
			HEIGHT-450, HEIGHT-330, 14600, 15000,
			3, 3, 3, 3,
			True, True,
				[
				#last spikes
				[0, 14600, HEIGHT-404, HEIGHT-494, HEIGHT-358, 14600, 15000,
				3, 3, 3, 3, True, True],
				[1, 14628, HEIGHT-360, HEIGHT-450, HEIGHT-330, 14628, 15028,
				3, 3, 3, 3, True, True],
				[2, 14600, HEIGHT-332, HEIGHT-422, HEIGHT-286, 14600, 15000,
				3, 3, 3, 3, True, True],
				[3, 14554, HEIGHT-360, HEIGHT-450, HEIGHT-330, 14554, 14954,
				3, 3, 3, 3, True, True]
				]
			]
		]

		#array of special moving platforms
		#[orientation, x, y, top bound, bottom bound, left bound, right bound,
		#speed up, speed down, speed left, speed right, is moving round, clockwise movement]
		medium_round_spikes = [
			#see medium_block_round_moving [array of subblock]
		]

		#[width, height, x, y, top bound, bottom bound, speed, pause]
		medium_moving_magma = [
			[1900, 270, 8100, HEIGHT, HEIGHT-250, HEIGHT+270, 1, 120]
		]





		###################################################################################

		#Hard

		#[widht, height, x, y]
		hard_plats = [
			[20, 20, 3950, HEIGHT-200],
			#square of spikes for the moving platform
			[30, 30, 5300, HEIGHT-350],
			[30, 30, 5700, HEIGHT-350],
			#square for spikes in the middle of the platform where moving magma stands
			[30, 30, 9000, HEIGHT-200]
		]

		#[width, height, x, y]
		hard_magma = [
			[450, 50, 6700, HEIGHT-50],
		]

		#[width, height, x, y, left bound, right bound, speed]
		hard_horiz_plat = [
			[80, 20, 4850, HEIGHT-200, 4850, 5900, 3],
			[80, 20, 13950, HEIGHT-250, 13950, 15000, 3]
		]

		#[orientation, top-left x, top-left y, left bound, right bound, speed,
		#[[array of subblock]]]
		hard_horiz_spikes = [
			[3, 900, HEIGHT-30, 900, 1450, 8,
				[
				[1, 945, HEIGHT-30, 945, 1495, 8]
				]
			],
			[3, 2200, HEIGHT-100, 2200, 2700, 8,
				[
				[1, 2245, HEIGHT-100, 2245, 2745, 8]
				]
			],
			[3, 6800, HEIGHT-130, 6800, 7300, 6,
				[
				[1, 6845, HEIGHT-130, 6845, 7345, 6]
				]
			]
		]

		#[width, height, x, y, top bound, bottom bound, speed]
		hard_vert_plat = [
			[100, 20, 12800, HEIGHT-250, HEIGHT-250, HEIGHT-50, 3],
			[100, 20, 13200, HEIGHT-100, HEIGHT-250, HEIGHT-50, 2],
			[50, 20, 13500, HEIGHT-70, HEIGHT-250, HEIGHT-50, 1]
		]

		#[orientation, top-left x, top-left y, top bound, bottom bound, speed
		#[[array of subblock]]]
		hard_vert_spikes = [
			#stalagtite spikes at the end
			[2, 15400, HEIGHT-46, HEIGHT-200, HEIGHT, 6,
				[
				[2, 15430, HEIGHT-76, HEIGHT-200, HEIGHT, 6],
				[2, 15460, HEIGHT-106, HEIGHT-200, HEIGHT, 6],
				[2, 15490, HEIGHT-136, HEIGHT-200, HEIGHT, 6],
				[2, 15520, HEIGHT-166, HEIGHT-200, HEIGHT, 6],
				[2, 15550, HEIGHT-196, HEIGHT-200, HEIGHT, 6],
				[2, 15580, HEIGHT-174, HEIGHT-200, HEIGHT, -6],
				[2, 15610, HEIGHT-144, HEIGHT-200, HEIGHT, -6],
				[2, 15640, HEIGHT-114, HEIGHT-200, HEIGHT, -6],
				[2, 15670, HEIGHT-84, HEIGHT-200, HEIGHT, -6],
				[2, 15700, HEIGHT-54, HEIGHT-200, HEIGHT, -6],
				[2, 15730, HEIGHT-68, HEIGHT-200, HEIGHT, 6],
				[2, 15760, HEIGHT-98, HEIGHT-200, HEIGHT, 6],
				[2, 15790, HEIGHT-128, HEIGHT-200, HEIGHT, 6],
				[2, 15820, HEIGHT-158, HEIGHT-200, HEIGHT, 6],
				[2, 15850, HEIGHT-188, HEIGHT-200, HEIGHT, 6],
				#stalagmite spikes at the end
				[0, 15400, HEIGHT-90, HEIGHT-244, HEIGHT-44, 6],
				[0, 15430, HEIGHT-120, HEIGHT-244, HEIGHT-44, 6],
				[0, 15460, HEIGHT-150, HEIGHT-244, HEIGHT-44, 6],
				[0, 15490, HEIGHT-180, HEIGHT-244, HEIGHT-44, 6],
				[0, 15520, HEIGHT-210, HEIGHT-244, HEIGHT-44, 6],
				[0, 15550, HEIGHT-240, HEIGHT-244, HEIGHT-44, 6],
				[0, 15580, HEIGHT-218, HEIGHT-244, HEIGHT-44, -6],
				[0, 15610, HEIGHT-188, HEIGHT-244, HEIGHT-44, -6],
				[0, 15640, HEIGHT-158, HEIGHT-244, HEIGHT-44, -6],
				[0, 15670, HEIGHT-128, HEIGHT-244, HEIGHT-44, -6],
				[0, 15700, HEIGHT-98, HEIGHT-244, HEIGHT-44, -6],
				[0, 15730, HEIGHT-112, HEIGHT-244, HEIGHT-44, 6],
				[0, 15760, HEIGHT-142, HEIGHT-244, HEIGHT-44, 6],
				[0, 15790, HEIGHT-172, HEIGHT-244, HEIGHT-44, 6],
				[0, 15820, HEIGHT-202, HEIGHT-244, HEIGHT-44, 6],
				[0, 15850, HEIGHT-232, HEIGHT-244, HEIGHT-44, 6]
				]
			]
		]


		hard_block_round_moving = [
			[30, 30, 6350, HEIGHT-130,
			HEIGHT-210, HEIGHT-100, 6350, 6550,
			1, 1, 3, 3,
			True, True,
				[
				#array of special moving platforms
				#[type of spike, orientation, x, y, top bound, bottom bound, left bound, right bound,
				#speed up, speed down, speed left, speed right, is moving round, clockwise movement]
				['standard', 0, 6350, HEIGHT-175, HEIGHT-255, HEIGHT-129, 6350, 6550,
				1, 1, 3, 3, True, True],
				['standard', 1, 6378, HEIGHT-130, HEIGHT-210, HEIGHT-100, 6378, 6578,
				1, 1, 3, 3, True, True],
				['standard', 2, 6350, HEIGHT-101, HEIGHT-181, HEIGHT-55, 6350, 6550,
				1, 1, 3, 3, True, True],
				['standard', 3, 6304, HEIGHT-130, HEIGHT-210, HEIGHT-100, 6304, 6504,
				1, 1, 3, 3, True, True],
				['special', 3, 6322, HEIGHT-30, 6322, 6522, 3, 164],
				['special', 1, 6367, HEIGHT-30, 6367, 6567, 3, 164]
				]
			]
		]

		#[orientation, x, y, left bound, right bound, speed, pause]
		hard_spec_horiz_spikes = [
			#see just above as 'special'
		]

		#[width, height, x, y,
		#top bound, bottom bound, left bound, right bound,
		#speed up, speed down, speed left, speed right,
		#is moving round, clockwise movement]
		hard_round_moving = [
			#last moving squares on the ground
			#2nd
			[30, 30, 10700, HEIGHT-100,
			HEIGHT-180, HEIGHT-70, 10700, 11000,
			3, 3, 4, 4,
			True, False,
				[
				#2nd square
				[0, 10700, HEIGHT-145, HEIGHT-225, HEIGHT-99, 10700, 11000,
				3, 3, 4, 4, True, False],
				[1, 10728, HEIGHT-100, HEIGHT-180, HEIGHT-70, 10728, 11028,
				3, 3, 4, 4, True, False],
				[2, 10700, HEIGHT-71, HEIGHT-151, HEIGHT-25, 10700, 11000,
				3, 3, 4, 4, True, False],
				[3, 10654, HEIGHT-100, HEIGHT-180, HEIGHT-70, 10654, 10954,
				3, 3, 4, 4, True, False],
				]
			],
			#4th
			[30, 30, 11300, HEIGHT-100,
			HEIGHT-180, HEIGHT-70, 11300, 11600,
			3, 3, 4, 4,
			True, False,
				[
				#4th square
				[0, 11300, HEIGHT-145, HEIGHT-225, HEIGHT-99, 11300, 11600,
				3, 3, 4, 4, True, False],
				[1, 11328, HEIGHT-100, HEIGHT-180, HEIGHT-70, 11328, 11628,
				3, 3, 4, 4, True, False],
				[2, 11300, HEIGHT-71, HEIGHT-151, HEIGHT-25, 11300, 11600,
				3, 3, 4, 4, True, False],
				[3, 11254, HEIGHT-100, HEIGHT-180, HEIGHT-70, 11254, 11554,
				3, 3, 4, 4, True, False],
				]
			],
			#last moving square of spike
			[30, 30, 14600, HEIGHT-360,
			HEIGHT-450, HEIGHT-330, 14600, 15000,
			4, 4, 5, 5,
			True, True,
				[
				#last spikes
				[0, 14600, HEIGHT-404, HEIGHT-494, HEIGHT-358, 14600, 15000,
				4, 4, 5, 5, True, True],
				[1, 14628, HEIGHT-360, HEIGHT-450, HEIGHT-330, 14628, 15028,
				4, 4, 5, 5, True, True],
				[2, 14600, HEIGHT-332, HEIGHT-422, HEIGHT-286, 14600, 15000,
				4, 4, 5, 5, True, True],
				[3, 14554, HEIGHT-360, HEIGHT-450, HEIGHT-330, 14554, 14954,
				4, 4, 5, 5, True, True],
				]
			],
		]

		#[orientation, x, y, top bound, bottom bound, left bound, right bound,
		#speed up, speed down, speed left, speed right, is moving round, clockwise movement]
		hard_round_spikes = [
			#see just above
		]

		#[width, height, x, y, top bound, bottom bound, speed, pause]
		hard_moving_magma = [
			[1900, 270, 8100, HEIGHT, HEIGHT-250, HEIGHT+270, 2, 200]
		]





		###################################################################################
		###################################################################################


		"""Generation of the platform corresponding to the difficulty level"""

		if level_dif == "easy":
			for plat in easy_plats:
				block = Platform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for plat in easy_magma:
				block = MagmaPlat(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				self.magma_list.add(block)

			for plat in easy_horiz_plat:
				block = MovingPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_left = plat[4]
				block.boundary_right = plat[5]
				block.change_x = plat[6]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for plat in easy_vert_plat:
				block = MovingPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = plat[6]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			#block round moving platform.
			for plat in easy_block_round_moving:
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
				#subblock
				for sub in plat[14]:
					subblock = SpecialSpike(sub[0])
					subblock.rect.x = sub[1]
					subblock.rect.y = sub[2]
					subblock.boundary_top = sub[3]
					subblock.boundary_bottom = sub[4]
					subblock.boundary_left = sub[5]
					subblock.boundary_right = sub[6]
					subblock.change_y_u = -sub[7]
					subblock.change_y_d = sub[8]
					subblock.change_x_l = -sub[9]
					subblock.change_x_r = sub[10]
					subblock.round_mov = sub[11]
					subblock.clockwise = sub[12]
					if sub[12] == False:
						subblock.change_y = sub[8]
					else:
						subblock.change_y = -sub[7]
					subblock.player = self.player
					subblock.level = self
					block.subblock.add(subblock)

				self.mov_plat_list.add(block)

			#moving magma
			for plat in easy_moving_magma:
				block = MagmaPlat(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = -plat[6]
				block.change_y_u = -plat[6]
				block.change_y_d = plat[6]
				block.pause_down = plat[7]
				block.player = self.player
				block.level = self
				self.magma_list.add(block)

			for plat in easy_checkpoints:
				block = CheckPoint(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				#CheckPoint is white!
				block.image.fill(constants.WHITE)
				self.platform_list.add(block)



		###################################################################################

		elif level_dif == "medium":
			for plat in medium_plats:
				block = Platform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for plat in easy_magma:
				block = MagmaPlat(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				self.magma_list.add(block)

			#static spikes
			for spike in medium_spikes:
				block = Spike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for plat in medium_horiz_plat:
				block = MovingPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_left = plat[4]
				block.boundary_right = plat[5]
				block.change_x = plat[6]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for plat in medium_vert_plat:
				block = MovingPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = plat[6]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for spike in medium_horiz_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_left = spike[3]
				block.boundary_right = spike[4]
				block.change_x = spike[5]
				block.player = self.player
				block.level = self
				for sub in spike[6]:
					subblock = MovingSpike(sub[0])
					subblock.rect.x = sub[1]
					subblock.rect.y = sub[2]
					subblock.boundary_left = sub[3]
					subblock.boundary_right = sub[4]
					subblock.change_x = sub[5]
					subblock.player = self.player
					subblock.level = self
					block.subblock.add(subblock)
				self.mov_plat_list.add(block)

			for spike in medium_vert_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_top = spike[3]
				block.boundary_bottom = spike[4]
				block.change_y = spike[5]
				block.player = self.player
				block.level = self
				for sub in spike[6]:
					subblock = MovingSpike(sub[0])
					subblock.rect.x = sub[1]
					subblock.rect.y = sub[2]
					subblock.boundary_top = sub[3]
					subblock.boundary_bottom = sub[4]
					subblock.change_y = sub[5]
					subblock.player = self.player
					subblock.level = self
					block.subblock.add(subblock)
				self.mov_plat_list.add(block)


			#round moving platform.
			for plat in medium_block_round_moving:
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
				#subblock
				for sub in plat[14]:
					subblock = SpecialSpike(sub[0])
					subblock.rect.x = sub[1]
					subblock.rect.y = sub[2]
					subblock.boundary_top = sub[3]
					subblock.boundary_bottom = sub[4]
					subblock.boundary_left = sub[5]
					subblock.boundary_right = sub[6]
					subblock.change_y_u = -sub[7]
					subblock.change_y_d = sub[8]
					subblock.change_x_l = -sub[9]
					subblock.change_x_r = sub[10]
					subblock.round_mov = sub[11]
					subblock.clockwise = sub[12]
					if sub[12] == False:
						subblock.change_y = sub[8]
					else:
						subblock.change_y = -sub[7]
					subblock.player = self.player
					subblock.level = self
					block.subblock.add(subblock)

				self.mov_plat_list.add(block)

			#moving magma
			for plat in medium_moving_magma:
				block = MagmaPlat(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = -plat[6]
				block.change_y_u = -plat[6]
				block.change_y_d = plat[6]
				block.pause_down = plat[7]
				block.player = self.player
				block.level = self
				self.magma_list.add(block)

			for plat in easy_checkpoints:
				block = CheckPoint(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				#CheckPoint is white!
				block.image.fill(constants.WHITE)
				self.platform_list.add(block)




		###################################################################################

		elif level_dif == "hard":
			for plat in hard_plats:
				block = Platform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for spike in medium_spikes:
				block = Spike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for plat in hard_magma:
				block = MagmaPlat(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				self.magma_list.add(block)

			for plat in hard_horiz_plat:
				block = MovingPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_left = plat[4]
				block.boundary_right = plat[5]
				block.change_x = plat[6]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for spike in hard_horiz_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_left = spike[3]
				block.boundary_right = spike[4]
				block.change_x = spike[5]
				block.player = self.player
				block.level = self
				for sub in spike[6]:
					subblock = MovingSpike(sub[0])
					subblock.rect.x = sub[1]
					subblock.rect.y = sub[2]
					subblock.boundary_left = sub[3]
					subblock.boundary_right = sub[4]
					subblock.change_x = sub[5]
					subblock.player = self.player
					subblock.level = self
					block.subblock.add(subblock)
				self.mov_plat_list.add(block)

			for plat in hard_vert_plat:
				block = MovingPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = plat[6]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for spike in hard_vert_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_top = spike[3]
				block.boundary_bottom = spike[4]
				block.change_y = spike[5]
				block.player = self.player
				block.level = self
				for sub in spike[6]:
					subblock = MovingSpike(sub[0])
					subblock.rect.x = sub[1]
					subblock.rect.y = sub[2]
					subblock.boundary_top = sub[3]
					subblock.boundary_bottom = sub[4]
					subblock.change_y = sub[5]
					subblock.player = self.player
					subblock.level = self
					block.subblock.add(subblock)
				self.mov_plat_list.add(block)


			#round moving platform.
			for plat in hard_round_moving:
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
				#subblock
				for sub in plat[14]:
					subblock = SpecialSpike(sub[0])
					subblock.rect.x = sub[1]
					subblock.rect.y = sub[2]
					subblock.boundary_top = sub[3]
					subblock.boundary_bottom = sub[4]
					subblock.boundary_left = sub[5]
					subblock.boundary_right = sub[6]
					subblock.change_y_u = -sub[7]
					subblock.change_y_d = sub[8]
					subblock.change_x_l = -sub[9]
					subblock.change_x_r = sub[10]
					subblock.round_mov = sub[11]
					subblock.clockwise = sub[12]
					if sub[12] == False:
						subblock.change_y = sub[8]
					else:
						subblock.change_y = -sub[7]
					subblock.player = self.player
					subblock.level = self
					block.subblock.add(subblock)

				self.mov_plat_list.add(block)


			#block round moving platform.
			for plat in hard_block_round_moving:
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
				#subblock
				for sub in plat[14]:
					if sub[0] == 'standard':
						subblock = SpecialSpike(sub[1])
						subblock.rect.x = sub[2]
						subblock.rect.y = sub[3]
						subblock.boundary_top = sub[4]
						subblock.boundary_bottom = sub[5]
						subblock.boundary_left = sub[6]
						subblock.boundary_right = sub[7]
						subblock.change_y_u = -sub[8]
						subblock.change_y_d = sub[9]
						subblock.change_x_l = -sub[10]
						subblock.change_x_r = sub[11]
						subblock.round_mov = sub[12]
						subblock.clockwise = sub[13]
						if sub[13] == False:
							subblock.change_y = sub[9]
						else:
							subblock.change_y = -sub[8]
						subblock.player = self.player
						subblock.level = self
						block.subblock.add(subblock)
					elif sub[0] == 'special':
						subblock = SpecialSpike(sub[1])
						subblock.rect.x = sub[2]
						subblock.rect.y = sub[3]
						subblock.boundary_left = sub[4]
						subblock.boundary_right = sub[5]
						subblock.change_x = -sub[6]
						subblock.change_x_l = -sub[6]
						subblock.change_x_r = sub[6]
						subblock.pause_left = sub[7]
						subblock.pause_right = sub[7]
						subblock.player = self.player
						subblock.level = self
						block.subblock.add(subblock)

				self.mov_plat_list.add(block)


			#moving magma
			for plat in hard_moving_magma:
				block = MagmaPlat(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = -plat[6]
				block.change_y_u = -plat[6]
				block.change_y_d = plat[6]
				block.pause_down = plat[7]
				block.player = self.player
				block.level = self
				self.magma_list.add(block)
