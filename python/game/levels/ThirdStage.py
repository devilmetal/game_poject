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
import constants
import pygame


class ThirdStage(Level):
	"""Overview of the "easy/standard" way of the first stage"""

	def __init__(self, player, level_dif):

		Level.__init__(self, player)
		next_level = 2
		self.level_limit = -15000

		HEIGHT = constants.SCREEN_HEIGHT-20


		"""static platforms"""
		
		#static platforms
		#[width, height, x, y]
		platforms = [
			#ground platform
			[2600, 20, 0, HEIGHT]
		]

		#death moving wall
		#[width, height, x, y, left bound, right bound, speed right, speed left, pause right, pause left,
		#[[Array of magma subblock]]]
		horiz_mov_wall = [
			[400, HEIGHT, -300, 0, -300, 2000, 1, 0, 60, 60,
				[[20, HEIGHT, 100, 0, 100, 2400, 1, 0, 60, 60]]
			]
		]

		#[width, height, x, y, left bound, right bound, speed right, speed left, pause right, pause left]
		horiz_magma_wall = [
			[20, HEIGHT, 100, 0, 100, 2400, 1, 0, 60, 60]
		]


		#adding parallax stuff to background along the level
		x_parallax=0
		back_p=[]
		front_p=[]
		while x_parallax < -self.level_limit + constants.SCREEN_WIDTH:
			back_p.append([x_parallax])
			front_p.append([x_parallax])
			x_parallax+=constants.SCREEN_WIDTH


		###################################################################################
		###################################################################################


		"""generation of the platforms"""
		for plat in platforms:
			block = Platform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
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

			self.mov_plat_list.add(block)


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