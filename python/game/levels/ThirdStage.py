from Level import Level
from platforms.Platform import Platform
from platforms.MovingPlatform import MovingPlatform
from platforms.BoostPlatform import BoostPlatform
from platforms.Spike import Spike
from platforms.MovingSpike import MovingSpike
from platforms.SpecialPlatform import SpecialPlatform
from platforms.SpecialSpike import SpecialSpike
from platforms.EndPlatform import EndPlatform
from platforms.CheckPoint import CheckPoint
from platforms.MagmaPlat import MagmaPlat
from world.Parallax import Parallax
from PNJ.Blob import Blob
from PNJ.Fairy import Fairy
from world.Sign import Sign
import constants
import pygame


class ThirdStage(Level):
	"""Overview of the "easy/standard" way of the first stage"""

	def __init__(self, player, level_dif):

		Level.__init__(self, player)
		next_level = 2
		self.level_limit = -15000
		self.level_name = "Stage 3"

		HEIGHT = constants.SCREEN_HEIGHT-20


		"""static platforms"""

		#static platforms
		#[width, height, x, y]
		platforms = [
			#obstacles
			[100, 300, 1200, HEIGHT-300],
			[550, 20, 550, HEIGHT-100],
			[20, 420, 530, HEIGHT-500],
			[50, 50, 700, HEIGHT-250],
			[50, 50, 900, HEIGHT-250],
			[50, 50, 1100, HEIGHT-250],
			#second obstacles
			[20, HEIGHT-80, 1500, 0],
			[20, 300, 1700, HEIGHT-300],
			#third obstacles
			[20, HEIGHT-80, 1850, 0],
			#air platform
			[100, 20, 3250, HEIGHT-150],
			[30, 30, 3685, HEIGHT-165],
			#second ground platform
			[2000, 20, 4300, HEIGHT],
			[400, HEIGHT-50, 4400, 0],
			[400, HEIGHT-150, 4850, 0],
			[400, 100, 4850, HEIGHT-100],
			[100, HEIGHT-50, 5300, 0],
			[130, HEIGHT-100, 5400, 0],
			[120, HEIGHT-50, 5530, 0],
			[130, HEIGHT-100, 5650, 0],
			[220, HEIGHT-50, 5780, 0],
			[30, 50, 5450, HEIGHT-50],
			[30, 20, 5700, HEIGHT-50],
			[50, 20, 6400, HEIGHT-100],
			[50, 20, 6600, HEIGHT-20],
			[50, 20, 6800, HEIGHT-120],
			[50, 20, 7000, HEIGHT-20],
			#second part of the level
			[1900, 20, 7200, HEIGHT-100],
			#platforms between top & bott. moving platforms
			[50, 20, 7400, HEIGHT-200],
			[50, 20, 7600, HEIGHT-200],
			[50, HEIGHT-150, 7750, -50],
			[90, 20, 8200, HEIGHT-200],
			[50, 270, 8900, HEIGHT-350],
			[50, 300, 8600, HEIGHT-500],
			[50, 20, 8850, HEIGHT-200],
			[50, 20, 8650, HEIGHT-250],
			[50, 20, 8950, HEIGHT-200],
			#part without ground
			[50, 20, 9200, HEIGHT-200],
			[50, 20, 9400, HEIGHT-250],
			[50, 20, 9600, HEIGHT-250],
			[50, 20, 9900, HEIGHT-200],
			[500, 20, 10000, HEIGHT-100],
			[500, 20, 10700, HEIGHT-200],
			#last part of the level. Cave + moving ground
			[600, 120, 11400, HEIGHT-100],
			[400, HEIGHT-110, 11600, -40],
			[580, 300, 12050, HEIGHT-280],
			[1050, HEIGHT-290, 12000, -40],
			[190, 230, 12630, HEIGHT-210],
			[50, 20, 12700, HEIGHT-280],
			[180, 300, 12820, HEIGHT-280],
			[1000, 120, 13050, HEIGHT-100],
			[500, HEIGHT-110, 13050, -40],
			[420, HEIGHT-110, 13630, -40],
			[1000, 20, 14050, HEIGHT]

		]

		#some standard spikes
		#[orientation, x, y]
		spikes = [
			[0, 2000, HEIGHT-45],
			[0, 2200, HEIGHT-45],
			[0, 2400, HEIGHT-45],
			[0, 3685, HEIGHT-208],
			[1, 3712, HEIGHT-165],
			[2, 3685, HEIGHT-138],
			[3, 3640, HEIGHT-165],
			#spikes between the 2 vert moving platforms with magma
			[0, 7900, HEIGHT-145],
			[0, 7930, HEIGHT-145],
			[0, 7960, HEIGHT-145],
			[1, 8245, HEIGHT-180],
			[3, 8200, HEIGHT-180],
			[1, 8245, HEIGHT-150],
			[3, 8200, HEIGHT-150],
			[1, 8245, HEIGHT-120],
			[3, 8200, HEIGHT-120],
		]

		#checkpoints
		#[widht, height, x, y]
		checkpoints = [
			[100, 20, 7100, HEIGHT-100]
		]

		#array of diag moving plat
		#[widght, height, x, y, left bound, right bound, top bound, bottom bound, speed]
		diag = [
			[100, 20, 2700, HEIGHT-150, 2700, 3000, HEIGHT-300, HEIGHT+20, 1],
			[100, 20, 3500, HEIGHT-150, 3500, 3800, HEIGHT-300, HEIGHT+20, 1]
		]

		#vertical moving spikes
		#[orientation, x, y, top bound, bottome bound, speed]
		vert_spikes = [
			#spikes between moving magma platforms
			[0, 10585, HEIGHT-100, HEIGHT-400, HEIGHT-54, 5],
			[2, 10585, HEIGHT-55, HEIGHT-355, HEIGHT-9, 5],
		]


		#death moving wall
		#[width, height, x, y, left bound, right bound, speed right, speed left, pause right, pause left,
		#[[Array of magma subblock]]]
		horiz_mov_wall = [
			[500, HEIGHT, -400, 0, -400, 2000, 1, 0, 60, 60,
				#[width, height, x, y, left bound, right bound, speed right, speed left, pause right, pause left]
				[[20, HEIGHT, 100, 0, 100, 2500, 1, 0, 60, 60]]
			]
		]


		#if we are on a platform that should make us go to the next level
		#[width, height, top-left x, top-left y, next level]
		end_plat = []
		end_plat.append([200, 20, 14500, HEIGHT, 3, 'little_fat'])

		signs = [
			[14300, HEIGHT,"Boss ==>"],
		]


		#adding parallax stuff to background along the level
		x_parallax=0
		front_p=[]
		while x_parallax < -self.level_limit + constants.SCREEN_WIDTH:
			front_p.append([x_parallax])
			x_parallax+=constants.SCREEN_WIDTH

		"""Some foes"""
		blobs = [
			[1350, HEIGHT-30, 1, 2],
			[1350, HEIGHT-30, 1, 3]
		]

		fairy = [
			[8950, HEIGHT-145, player]
		]


		###################################################################################
		###################################################################################


		"""generation of the platforms"""
		for plat in platforms:
			block = Platform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			block.setcave()
			self.platform_list.add(block)

		for spike in spikes:
			block = Spike(spike[0])
			block.rect.x = spike[1]
			block.rect.y = spike[2]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		for plat in checkpoints:
			block = CheckPoint(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			#CheckPoint is white!
			block.image.fill(constants.WHITE)
			self.platform_list.add(block)

		for plat in diag:
			block = MovingPlatform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.boundary_left = plat[4]
			block.boundary_right = plat[5]
			block.boundary_top = plat[6]
			block.boundary_bottom = plat[7]
			block.change_x = plat[8]
			block.change_y = plat[8]
			block.player = self.player
			block.level = self
			block.setcave()
			self.platform_list.add(block)

		for spike in vert_spikes:
			block = MovingSpike(spike[0])
			block.rect.x = spike[1]
			block.rect.y = spike[2]
			block.boundary_top = spike[3]
			block.boundary_bottom = spike[4]
			block.change_y = spike[5]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		for wall in horiz_mov_wall:
			block = SpecialPlatform(wall[0], wall[1])
			block.rect.x = wall[2]
			block.rect.y = wall[3]
			block.boundary_left = wall[4]
			block.boundary_right = wall[5]
			block.change_x = wall[6]
			block.change_x_r = wall[6]
			block.change_x_l = -wall[7]
			block.pause_right = wall[8]
			block.pause_left = wall[9]
			block.player = self.player
			block.level = self
			block.setcave()

			for magma in wall[10]:
				subblock = MagmaPlat(magma[0], magma[1])
				subblock.rect.x = magma[2]
				subblock.rect.y = magma[3]
				subblock.boundary_left = magma[4]
				subblock.boundary_right = magma[5]
				subblock.change_x = magma[6]
				subblock.change_x_r = magma[6]
				subblock.change_x_l = -magma[7]
				subblock.pause_right = magma[8]
				subblock.pause_left = magma[9]
				subblock.player = self.player
				subblock.level = self
				block.subblock.add(subblock)
				self.sub_plat_list.add(subblock)

			self.mov_plat_list.add(block)



		for plat in end_plat:
			block = EndPlatform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			block.level_pointer = plat[4]
			block.character_pointer = plat[5]
			block.setcave()
			self.platform_list.add(block)

		#Parallax background
		for elem in front_p:
			x = elem[0]
			y = 0
			width = constants.SCREEN_WIDTH
			height = constants.SCREEN_HEIGHT
			mode = "cave_p"
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
			#ground platform
			[2600, 20, 0, HEIGHT],
			#obstacles
			[550, 20, 650, HEIGHT-200],
			[50, 20, 1650, HEIGHT-100],
			[50, 20, 1520, HEIGHT-200],
			[50, 20, 10100, HEIGHT-200],
			[80, HEIGHT-300, 13550, -40],
		]

		easy_vert_spikes = [
			[0, 4810, HEIGHT-90, HEIGHT-300, HEIGHT-44, 2],
			[2, 4810, HEIGHT-45, HEIGHT-255, HEIGHT+1, 2],
			[0, 5260, HEIGHT-90, HEIGHT-300, HEIGHT-44, 2],
			[2, 5260, HEIGHT-45, HEIGHT-255, HEIGHT+1, 2],
		]

		easy_horiz_spikes = [
			#spikes in the last part of the stage
			[1, 12545, HEIGHT-310, 12545, 12895, 4, [3,12500, HEIGHT-310, 12500, 12850, 4]]
		]

		###/!\/!\/!\ I had to split the platform into subarray in order to make it still move if
		#plat.rect.x is out of the limit (i.e. abs(plat.rect.x - self.rect.x) < screen.width*3)

		#vertical moving platform
		#[width, height, x, y, top bound, bottom bound, speed down, speed up, pause down, pause up,
		#	[[subbaray of the same kind]]]
		easy_vert_plat = [
			[900, 300, 7300, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 1, 300, 300,
				[
				[1000, 300, 8200, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 1, 300, 300],
				[1000, 300, 9200, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 1, 300, 300],
				[1000, 300, 10200, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 1, 300, 300],
				]
			],
			[900, HEIGHT-100, 7300, -230, -410, HEIGHT-330, 1, 1, 300, 300,
				[
				[1000, HEIGHT-100, 8200, -230, -410, HEIGHT-330, 1, 1, 300, 300],
				[1000, HEIGHT-100, 9200, -230, -410, HEIGHT-330, 1, 1, 300, 300],
				[1000, HEIGHT-100, 10200, -230, -410, HEIGHT-330, 1, 1, 300, 300],
				]
			],
			#last vertical ground that can kill if stuck in a tunnel
			[1000, 600, 11600, HEIGHT-50, HEIGHT-200, HEIGHT+550, 2, 1, 180, 240,
				[
				[1000, 600, 12600, HEIGHT-50, HEIGHT-200, HEIGHT+550, 2, 1, 180, 240],
				[450, 600, 13600, HEIGHT-50, HEIGHT-200, HEIGHT+550, 2, 1, 180, 240]
				]
			]
		]


		#vertical moving magma
		#[width, height, x, y, top bound, bottom bound, speed down, speed up, pause down, pause up]
		easy_vert_magma = [
			[900, 40, 7300, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 1, 300, 300,
				[
				[1000, 40, 8200, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 1, 300, 300],
				[1000, 40, 9200, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 1, 300, 300],
				[1000, 40, 10200, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 1, 300, 300],
				]
			],
			[900, 40, 7300, HEIGHT-370, HEIGHT-550, HEIGHT-330, 1, 1, 300, 300,
				[
				[1000, 40, 8200, HEIGHT-370, HEIGHT-550, HEIGHT-330, 1, 1, 300, 300],
				[1000, 40, 9200, HEIGHT-370, HEIGHT-550, HEIGHT-330, 1, 1, 300, 300],
				[1000, 40, 10200, HEIGHT-370, HEIGHT-550, HEIGHT-330, 1, 1, 300, 300],
				]
			]
		]

		easy_med_checkpoints = [
			[80, 20, 4050, HEIGHT-150],
			[80, 20, 11200, HEIGHT-200]
		]

		###################################################################################

		#medium

		med_plats = [
			#ground platform
			[2600, 20, 0, HEIGHT],
			#osbtacles
			[50, 20, 650, HEIGHT-200],
			[50, 20, 1650, HEIGHT-50],
			[50, 20, 1520, HEIGHT-100],
			[50, 20, 1650, HEIGHT-150],
			[50, 20, 1520, HEIGHT-200],
			[50, 20, 1650, HEIGHT-250],
			[30, 30, 2885, HEIGHT-165],
			[50, 20, 10300, HEIGHT-200],
			[80, HEIGHT-110, 13550, -40],
		]

		med_spikes = [
			[0, 2100, HEIGHT-45],
			[0, 2300, HEIGHT-45],
			#spikes in the center of the moving platform
			[0, 2885, HEIGHT-208],
			[1, 2912, HEIGHT-165],
			[2, 2885, HEIGHT-138],
			[3, 2840, HEIGHT-165],
			#wall of spikes
			[1, 8445, HEIGHT-180],
			[3, 8400, HEIGHT-180],
			[1, 8445, HEIGHT-210],
			[3, 8400, HEIGHT-210],
			[1, 8445, HEIGHT-240],
			[3, 8400, HEIGHT-240],
			[1, 8445, HEIGHT-270],
			[3, 8400, HEIGHT-270],
			[1, 8445, HEIGHT-300],
			[3, 8400, HEIGHT-300],
			[1, 8445, HEIGHT-330],
			[3, 8400, HEIGHT-330],
			[1, 8445, HEIGHT-360],
			[3, 8400, HEIGHT-360],
			[1, 8445, HEIGHT-390],
			[3, 8400, HEIGHT-390],
		]

		med_horiz_spikes = [
			[1, 5545, HEIGHT-30, 5545, 5995, 5, [3, 5500, HEIGHT-30, 5500, 5950, 5]],
			#spikes in the last part of the stage
			[1, 12545, HEIGHT-310, 12545, 12895, 4, [3,12500, HEIGHT-310, 12500, 12850, 4]]
		]

		med_vert_spikes = [
			[0, 3150, HEIGHT-300, HEIGHT-300, HEIGHT-50, 8],
			[2, 3150, HEIGHT-255, HEIGHT-255, HEIGHT-5, 8],
			[0, 3400, HEIGHT-300, HEIGHT-300, HEIGHT-50, 8],
			[2, 3400, HEIGHT-255, HEIGHT-255, HEIGHT-5, 8],
			[0, 4810, HEIGHT-90, HEIGHT-300, HEIGHT-44, 5],
			[2, 4810, HEIGHT-45, HEIGHT-255, HEIGHT+1, 5],
			[0, 5260, HEIGHT-90, HEIGHT-300, HEIGHT-44, 5],
			[2, 5260, HEIGHT-45, HEIGHT-255, HEIGHT+1, 5],
			[0, 10615, HEIGHT-100, HEIGHT-400, HEIGHT-54, 8],
			[2, 10615, HEIGHT-55, HEIGHT-355, HEIGHT-9, 8],
		]

		#vertical moving platform
		#[width, height, x, y, top bound, bottom bound, speed down, speed up, pause down, pause up,
		#	[[subbaray of the same kind]]]
		med_vert_plat = [
			[900, 300, 7300, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 1, 300, 300,
				[
				[1000, 300, 8200, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 1, 300, 300],
				[1000, 300, 9200, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 1, 300, 300],
				[1000, 300, 10200, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 1, 300, 300],
				]
			],
			[900, HEIGHT-100, 7300, -190, -370, HEIGHT-290, 1, 1, 300, 300,
				[
				[1000, HEIGHT-100, 8200, -190, -370, HEIGHT-290, 1, 1, 300, 300],
				[1000, HEIGHT-100, 9200, -190, -370, HEIGHT-290, 1, 1, 300, 300],
				[1000, HEIGHT-100, 10200, -190, -370, HEIGHT-290, 1, 1, 300, 300],
				]
			],
			#last vertical ground that can kill if stuck in a tunnel
			[1000, 600, 11600, HEIGHT-50, HEIGHT-200, HEIGHT+550, 2, 2, 300, 240,
				[
				[1000, 600, 12600, HEIGHT-50, HEIGHT-200, HEIGHT+550, 2, 2, 300, 240],
				[450, 600, 13600, HEIGHT-50, HEIGHT-200, HEIGHT+550, 2, 2, 300, 240]
				]
			]
		]

		#vertical moving magma
		#[width, height, x, y, top bound, bottom bound, speed down, speed up, pause down, pause up]
		med_vert_magma = [
			[900, 40, 7300, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 1, 300, 300,
				[
				[1000, 40, 8200, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 1, 300, 300],
				[1000, 40, 9200, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 1, 300, 300],
				[1000, 40, 10200, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 1, 300, 300],
				]
			],
			[900, 40, 7300, HEIGHT-330, HEIGHT-510, HEIGHT-290, 1, 1, 300, 300,
				[
				[1000, 40, 8200, HEIGHT-330, HEIGHT-510, HEIGHT-290, 1, 1, 300, 300],
				[1000, 40, 9200, HEIGHT-330, HEIGHT-510, HEIGHT-290, 1, 1, 300, 300],
				[1000, 40, 10200, HEIGHT-330, HEIGHT-510, HEIGHT-290, 1, 1, 300, 300],
				]
			]
		]


		###################################################################################

		#hard

		hard_plats = [
			[1580, 20, 0, HEIGHT],
			[900, 20, 1700, HEIGHT],
			[50, 20, 650, HEIGHT-200],
			[50, 20, 1650, HEIGHT-50],
			[50, 20, 1520, HEIGHT-100],
			[50, 20, 1650, HEIGHT-150],
			[50, 20, 1520, HEIGHT-200],
			[50, 20, 1650, HEIGHT-250],
			[30, 30, 2885, HEIGHT-165],
			#replace the first checkpoint
			[80, 20, 4050, HEIGHT-150],
			[50, 20, 10300, HEIGHT-200],
			[80, HEIGHT-110, 13550, -40],
		]

		hard_spikes = [
			[0, 2100, HEIGHT-45],
			[0, 2300, HEIGHT-45],
			#square of spike in the center of a square moving platform
			[0, 2885, HEIGHT-208],
			[1, 2912, HEIGHT-165],
			[2, 2885, HEIGHT-138],
			[3, 2840, HEIGHT-165],
			#wall of spikes
			[1, 8445, HEIGHT-180],
			[3, 8400, HEIGHT-180],
			[1, 8445, HEIGHT-210],
			[3, 8400, HEIGHT-210],
			[1, 8445, HEIGHT-240],
			[3, 8400, HEIGHT-240],
			[1, 8445, HEIGHT-270],
			[3, 8400, HEIGHT-270],
			[1, 8445, HEIGHT-300],
			[3, 8400, HEIGHT-300],
			[1, 8445, HEIGHT-330],
			[3, 8400, HEIGHT-330],
			[1, 8445, HEIGHT-360],
			[3, 8400, HEIGHT-360],
			[1, 8445, HEIGHT-390],
			[3, 8400, HEIGHT-390],
		]

		hard_magma = [
			[120, 20, 1580, HEIGHT+10]
		]

		hard_vert_spikes = [
			[0, 800, HEIGHT-345, HEIGHT-445, HEIGHT-145, 5],
			[2, 800, HEIGHT-300, HEIGHT-400, HEIGHT-100, 5],
			[0, 1000, HEIGHT-345, HEIGHT-445, HEIGHT-145, 5],
			[2, 1000, HEIGHT-300, HEIGHT-400, HEIGHT-100, 5],
			#moving spikes between platform in the air
			[0, 3150, HEIGHT-300, HEIGHT-300, HEIGHT-50, 8],
			[2, 3150, HEIGHT-255, HEIGHT-255, HEIGHT-5, 8],
			[0, 3400, HEIGHT-300, HEIGHT-300, HEIGHT-50, 8],
			[2, 3400, HEIGHT-255, HEIGHT-255, HEIGHT-5, 8],
			#spikes inside the tunnel
			[0, 4810, HEIGHT-90, HEIGHT-300, HEIGHT-44, 6],
			[2, 4810, HEIGHT-45, HEIGHT-255, HEIGHT+1, 6],
			[0, 5260, HEIGHT-90, HEIGHT-300, HEIGHT-44, 6],
			[2, 5260, HEIGHT-45, HEIGHT-255, HEIGHT+1, 6],
			#at the end of the sandwich plat
			[0, 10615, HEIGHT-100, HEIGHT-400, HEIGHT-54, 8],
			[2, 10615, HEIGHT-55, HEIGHT-355, HEIGHT-9, 8],
		]

		hard_horiz_spikes = [
			[1, 3350, HEIGHT-200, 3045, 3550, 4, [3, 3305, HEIGHT-200, 3000, 3505, 4]],
			[1, 5545, HEIGHT-30, 5545, 5995, 6, [3, 5500, HEIGHT-30, 5500, 5950, 6]],
			[1, 8345, HEIGHT-130, 8345, 8845, 6, [3, 8300, HEIGHT-130, 8300, 8800, 6]],
			[1, 9945, HEIGHT-130, 9945, 10545, 6, [3, 9900, HEIGHT-130, 9900, 10500, 6]],
			#spikes in the last part of the stage
			[1, 12545, HEIGHT-310, 12545, 12895, 6, [3,12500, HEIGHT-310, 12500, 12850, 6]]
		]

		#vertical moving platform
		#[width, height, x, y, top bound, bottom bound, speed down, speed up, pause down, pause up,
		#	[[subbaray of the same kind]]]
		hard_vert_plat = [
			[900, 300, 7300, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 2, 300, 300,
				[
				[1000, 300, 8200, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 2, 300, 300],
				[1000, 300, 9200, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 2, 300, 300],
				[1000, 300, 10200, HEIGHT, HEIGHT-180, HEIGHT+300, 1, 2, 300, 300],
				]
			],
			[900, HEIGHT-100, 7300, -190, -370, HEIGHT-290, 1, 2, 300, 300,
				[
				[1000, HEIGHT-100, 8200, -190, -370, HEIGHT-290, 1, 2, 300, 300],
				[1000, HEIGHT-100, 9200, -190, -370, HEIGHT-290, 1, 2, 300, 300],
				[1000, HEIGHT-100, 10200, -190, -370, HEIGHT-290, 1, 2, 300, 300],
				]
			],
			#last vertical ground that can kill if stuck in a tunnel
			[1000, 600, 11600, HEIGHT-50, HEIGHT-200, HEIGHT+550, 2, 2, 300, 240,
				[
				[1000, 600, 12600, HEIGHT-50, HEIGHT-200, HEIGHT+550, 2, 2, 300, 240],
				[450, 600, 13600, HEIGHT-50, HEIGHT-200, HEIGHT+550, 2, 2, 300, 240]
				]
			]
		]

		#vertical moving magma
		#[width, height, x, y, top bound, bottom bound, speed down, speed up, pause down, pause up]
		hard_vert_magma = [
			[900, 40, 7300, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 2, 300, 300,
				[
				[1000, 40, 8200, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 2, 300, 300],
				[1000, 40, 9200, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 2, 300, 300],
				[1000, 40, 10200, HEIGHT, HEIGHT-180, HEIGHT+40, 1, 2, 300, 300],
				]
			],
			[900, 40, 7300, HEIGHT-330, HEIGHT-510, HEIGHT-290, 1, 2, 300, 300,
				[
				[1000, 40, 8200, HEIGHT-330, HEIGHT-510, HEIGHT-290, 1, 2, 300, 300],
				[1000, 40, 9200, HEIGHT-330, HEIGHT-510, HEIGHT-290, 1, 2, 300, 300],
				[1000, 40, 10200, HEIGHT-330, HEIGHT-510, HEIGHT-290, 1, 2, 300, 300],
				]
			]
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
				block.setcave()
				self.platform_list.add(block)

			for spike in easy_vert_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_top = spike[3]
				block.boundary_bottom = spike[4]
				block.change_y = spike[5]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for spike in easy_horiz_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_left = spike[3]
				block.boundary_right = spike[4]
				block.change_x = spike[5]
				block.player = self.player
				block.level = self

				subspike = MovingSpike(spike[6][0])
				subspike.rect.x = spike[6][1]
				subspike.rect.y = spike[6][2]
				subspike.boundary_left = spike[6][3]
				subspike.boundary_right = spike[6][4]
				subspike.change_x = spike[6][5]
				subspike.player = self.player
				subspike.level = self
				block.subblock.add(subspike)

				self.mov_plat_list.add(block)


			for plat in easy_vert_plat:
				block = SpecialPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = plat[6]
				block.change_y_d = plat[6]
				block.change_y_u = -plat[7]
				block.pause_down = plat[8]
				block.pause_up = plat[9]
				block.player = self.player
				block.setcave()
				block.level = self
				for sub in plat[10]:
					subblock = SpecialPlatform(sub[0], sub[1])
					subblock.rect.x = sub[2]
					subblock.rect.y = sub[3]
					subblock.boundary_top = sub[4]
					subblock.boundary_bottom = sub[5]
					subblock.change_y = sub[6]
					subblock.change_y_d = sub[6]
					subblock.change_y_u = -sub[7]
					subblock.pause_down = sub[8]
					subblock.pause_up = sub[9]
					subblock.player = self.player
					subblock.setcave()
					subblock.level = self
					block.subblock.add(subblock)
					self.sub_plat_list.add(subblock)
				self.mov_plat_list.add(block)


			for plat in easy_vert_magma:
				block = MagmaPlat(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = plat[6]
				block.change_y_d = plat[6]
				block.change_y_u = -plat[7]
				block.pause_down = plat[8]
				block.pause_up = plat[9]
				block.player = self.player
				block.level = self
				for sub in plat[10]:
					subblock = MagmaPlat(sub[0], sub[1])
					subblock.rect.x = sub[2]
					subblock.rect.y = sub[3]
					subblock.boundary_top = sub[4]
					subblock.boundary_bottom = sub[5]
					subblock.change_y = sub[6]
					subblock.change_y_d = sub[6]
					subblock.change_y_u = -sub[7]
					subblock.pause_down = sub[8]
					subblock.pause_up = sub[9]
					subblock.player = self.player
					subblock.level = self
					block.subblock.add(subblock)
					self.sub_plat_list.add(subblock)
				self.magma_list.add(block)

			for plat in easy_med_checkpoints:
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
			for plat in med_plats:
				block = Platform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				block.setcave()
				self.platform_list.add(block)

			for spike in med_spikes:
				block = Spike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for spike in med_vert_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_top = spike[3]
				block.boundary_bottom = spike[4]
				block.change_y = spike[5]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for spike in med_horiz_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_left = spike[3]
				block.boundary_right = spike[4]
				block.change_x = spike[5]
				block.player = self.player
				block.level = self

				subspike = MovingSpike(spike[6][0])
				subspike.rect.x = spike[6][1]
				subspike.rect.y = spike[6][2]
				subspike.boundary_left = spike[6][3]
				subspike.boundary_right = spike[6][4]
				subspike.change_x = spike[6][5]
				subspike.player = self.player
				subspike.level = self
				block.subblock.add(subspike)

				self.mov_plat_list.add(block)


			for plat in med_vert_plat:
				block = SpecialPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = plat[6]
				block.change_y_d = plat[6]
				block.change_y_u = -plat[7]
				block.pause_down = plat[8]
				block.pause_up = plat[9]
				block.player = self.player
				block.level = self
				block.setcave()
				for sub in plat[10]:
					subblock = SpecialPlatform(sub[0], sub[1])
					subblock.rect.x = sub[2]
					subblock.rect.y = sub[3]
					subblock.boundary_top = sub[4]
					subblock.boundary_bottom = sub[5]
					subblock.change_y = sub[6]
					subblock.change_y_d = sub[6]
					subblock.change_y_u = -sub[7]
					subblock.pause_down = sub[8]
					subblock.pause_up = sub[9]
					subblock.player = self.player
					subblock.level = self
					subblock.setcave()
					block.subblock.add(subblock)
					self.sub_plat_list.add(subblock)
				self.mov_plat_list.add(block)


			for plat in med_vert_magma:
				block = MagmaPlat(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = plat[6]
				block.change_y_d = plat[6]
				block.change_y_u = -plat[7]
				block.pause_down = plat[8]
				block.pause_up = plat[9]
				block.player = self.player
				block.level = self
				for sub in plat[10]:
					subblock = MagmaPlat(sub[0], sub[1])
					subblock.rect.x = sub[2]
					subblock.rect.y = sub[3]
					subblock.boundary_top = sub[4]
					subblock.boundary_bottom = sub[5]
					subblock.change_y = sub[6]
					subblock.change_y_d = sub[6]
					subblock.change_y_u = -sub[7]
					subblock.pause_down = sub[8]
					subblock.pause_up = sub[9]
					subblock.player = self.player
					subblock.level = self
					block.subblock.add(subblock)
					self.sub_plat_list.add(subblock)
				self.magma_list.add(block)

			for plat in easy_med_checkpoints:
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
				block.setcave()
				self.platform_list.add(block)

			for spike in hard_spikes:
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

			for spike in hard_horiz_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_left = spike[3]
				block.boundary_right = spike[4]
				block.change_x = spike[5]
				block.player = self.player
				block.level = self

				subspike = MovingSpike(spike[6][0])
				subspike.rect.x = spike[6][1]
				subspike.rect.y = spike[6][2]
				subspike.boundary_left = spike[6][3]
				subspike.boundary_right = spike[6][4]
				subspike.change_x = spike[6][5]
				subspike.player = self.player
				subspike.level = self
				block.subblock.add(subspike)

				self.mov_plat_list.add(block)

			for spike in hard_vert_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_top = spike[3]
				block.boundary_bottom = spike[4]
				block.change_y = spike[5]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for plat in hard_vert_plat:
				block = SpecialPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = plat[6]
				block.change_y_d = plat[6]
				block.change_y_u = -plat[7]
				block.pause_down = plat[8]
				block.pause_up = plat[9]
				block.player = self.player
				block.level = self
				block.setcave()
				for sub in plat[10]:
					subblock = SpecialPlatform(sub[0], sub[1])
					subblock.rect.x = sub[2]
					subblock.rect.y = sub[3]
					subblock.boundary_top = sub[4]
					subblock.boundary_bottom = sub[5]
					subblock.change_y = sub[6]
					subblock.change_y_d = sub[6]
					subblock.change_y_u = -sub[7]
					subblock.pause_down = sub[8]
					subblock.pause_up = sub[9]
					subblock.player = self.player
					subblock.level = self
					subblock.setcave()
					block.subblock.add(subblock)
					self.sub_plat_list.add(subblock)
				self.mov_plat_list.add(block)


			for plat in hard_vert_magma:
				block = MagmaPlat(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_top = plat[4]
				block.boundary_bottom = plat[5]
				block.change_y = plat[6]
				block.change_y_d = plat[6]
				block.change_y_u = -plat[7]
				block.pause_down = plat[8]
				block.pause_up = plat[9]
				block.player = self.player
				block.level = self
				for sub in plat[10]:
					subblock = MagmaPlat(sub[0], sub[1])
					subblock.rect.x = sub[2]
					subblock.rect.y = sub[3]
					subblock.boundary_top = sub[4]
					subblock.boundary_bottom = sub[5]
					subblock.change_y = sub[6]
					subblock.change_y_d = sub[6]
					subblock.change_y_u = -sub[7]
					subblock.pause_down = sub[8]
					subblock.pause_up = sub[9]
					subblock.player = self.player
					subblock.level = self
					block.subblock.add(subblock)
					self.sub_plat_list.add(subblock)
				self.magma_list.add(block)
