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
			[2600, 20, 0, HEIGHT],
			#obstacles
			[100, 300, 1200, HEIGHT-300],
			[550, 20, 550, HEIGHT-100],
			[20, 420, 530, HEIGHT-500],
			[550, 20, 650, HEIGHT-200],
			[50, 50, 700, HEIGHT-250],
			[50, 50, 900, HEIGHT-250],
			[50, 50, 1100, HEIGHT-250],
			#second obstacles
			[20, HEIGHT-80, 1500, 0],
			[20, 300, 1700, HEIGHT-300],
			[50, 20, 1650, HEIGHT-50],
			[50, 20, 1520, HEIGHT-100],
			[50, 20, 1650, HEIGHT-150],
			[50, 20, 1520, HEIGHT-200],
			[50, 20, 1650, HEIGHT-250],
			#third obstacles
			[20, HEIGHT-80, 1850, 0],
			#air platform
			[100, 20, 3250, HEIGHT-150],
			[30, 30, 3685, HEIGHT-165],
			#second ground platform
			[2000, 20, 4300, HEIGHT],
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
			[3, 3640, HEIGHT-165]
		]

		#checkpoints
		#[widht, height, x, y]
		checkpoints = [
			[80, 20, 4050, HEIGHT-150]
		]

		#array of diag moving plat
		#[widght, height, x, y, left bound, right bound, top bound, bottom bound, speed]
		diag = [
			[100, 20, 2700, HEIGHT-150, 2700, 3000, HEIGHT-300, HEIGHT+20, 1],
			[100, 20, 3500, HEIGHT-150, 3500, 3800, HEIGHT-300, HEIGHT+20, 1]
		]


		#death moving wall
		#[width, height, x, y, left bound, right bound, speed right, speed left, pause right, pause left,
		#[[Array of magma subblock]]]
		horiz_mov_wall = [
			[500, HEIGHT, -400, 0, -400, 2000, 1, 0, 60, 60,
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