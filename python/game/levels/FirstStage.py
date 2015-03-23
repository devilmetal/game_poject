from Level import Level
from platforms.Platform import Platform
from platforms.MovingPlatform import MovingPlatform
from platforms.BoostPlatform import BoostPlatform
from platforms.Spike import Spike
from platforms.MovingSpike import MovingSpike
from world.Tree import Tree
from platforms.SpecialPlatform import SpecialPlatform
from platforms.SpecialSpike import SpecialSpike
from platforms.EndPlatform import EndPlatform
from platforms.CheckPoint import CheckPoint

from PNJ.Blob import Blob

import constants
import pygame



# Create platforms for the level

class FirstStage(Level):
	"""Overview of the "easy/standard" way of the first stage"""

	def __init__(self, player, level_dif):

		Level.__init__(self, player)
		next_level = 0
		self.level_limit = -14300

		HEIGHT = constants.SCREEN_HEIGHT-20


		"""Static platforms"""
		#array of platforms
		#[width, height, top-left x coordinate, top-left y coordinate]
		level = [
				#just two little thingy to add a monster TODO:Remove
				[70, 70, 500, HEIGHT-50],
				[3200, 20, 0, HEIGHT],
				[300, HEIGHT, 0, 0],
				[100, 120, 1000, HEIGHT-120],
				[100, 120, 1500, HEIGHT-120],
				[100, 240, 1600, HEIGHT-240],
				[100, 120, 1700, HEIGHT-120],
				[150, 10, 2000, HEIGHT-240],
				[100, 240, 2500, HEIGHT-240],
				#small platform on the ground
				#variation in difficulty part

				#small platform in the air right after the first horiz. mov. plat.
				#see diff part

				#platform between moving plat in the air
				[50, 20, 7050, HEIGHT-300],
				#2nd ground plateform
				[2000, 20, 8300, HEIGHT],
				#first plateforms with spikes
				[30, 90, 8800, HEIGHT-90],
				[60, 5, 8770, HEIGHT-95],
				[30, 90, 9065, HEIGHT-90],
				#airwall of spikes
				[13, 120, 9495, HEIGHT-170],
				[103, 10, 9450, HEIGHT-180],
				#second airwall
				[13, 90, 9800, HEIGHT-170],
				[103, 10, 9755, HEIGHT-180],
				[60, HEIGHT-170, 9855, 0],
				#last air part of the level
				[30, 95, 10400, HEIGHT-75],
				[120, 20, 10430, HEIGHT-75],
				[130, 20, 10580, HEIGHT-200],
				[130, 20, 10740, HEIGHT-320],
				#last ground part
				[2900, 20, 12100, HEIGHT],
				#first end platform
				[120, 20, 14500, HEIGHT-100],
				]

		#if we are on a platform that should make us go to the next level
		#[width, height, top-left x, top-left y, next level]
		end_plat = [
					[120, 20, 14380, HEIGHT-350, 1]
					]
		# checkpoints
		#[top-left x, top-left , width, height]
		checkpoints = [
					[50, 20, 2600, HEIGHT-240],
					[60, 20, 5750, HEIGHT-300],
					[50, 20, 8400, HEIGHT-20]
					]

		"""Special moving platform and spikes"""
		#falling spikes at the end of the level		

		number_spikes = range(70) #create a list of number from 0 to 69


		"""Simple moving platforms"""
		#array of vertical moving platform
		#[width, height, top-left x, top-left y, top bound, bottom bound, speed]
		vert = [
				[60, 20, 4850, HEIGHT-20, HEIGHT-300, HEIGHT, 1],
				[30, 220, 10550, HEIGHT-200, HEIGHT-200, HEIGHT+200, 2],
				[30, 340, 10710, HEIGHT-320, HEIGHT-320, HEIGHT+200, 2],
				]


		#array of horizontal moving platform
		#[width, height, top-left x, top-left y, left bound, right bound, speed]
		horiz = [
				[60, 20, 5100, HEIGHT-300, 5100, 5600, 2],
				#chain moving platform in the air
				#see diff part

				#last moving platform
				[120, 20, 10900, HEIGHT-200, 10900, 11700, 2]
				]

		#array of diag moving plat
		#[widght, height, top-left x, top-left y, left bound, right bound, top bound, bottom bound, speed]
		diag = [
				[100, 20, 7850, HEIGHT-300, 7850, 8130, HEIGHT-300, HEIGHT, 1]
				]


		"""Static spikes"""
		#spikes list (capable to kill player ! :S)
		#[orientation, top-left x, top-left y]
		spikes = [
				[3, 8755, HEIGHT-30],
				[3, 8755, HEIGHT-60],
				[3, 8755, HEIGHT-90],
				[0, 8830, HEIGHT-45],
				[0, 8860, HEIGHT-45],
				#[0, 8920, HEIGHT-45],
				[3, 9020, HEIGHT-30],
				[3, 9020, HEIGHT-60],
				[3, 9020, HEIGHT-90],
				#airwall of spikes
				[3, 9450, HEIGHT-80],
				[1, 9505, HEIGHT-80],
				[3, 9450, HEIGHT-110],
				[1, 9505, HEIGHT-110],
				[3, 9450, HEIGHT-140],
				[1, 9505, HEIGHT-140],
				[3, 9450, HEIGHT-170],
				[1, 9505, HEIGHT-170],
				#second airwall
				[3, 9755, HEIGHT-110],
				[1, 9810, HEIGHT-110],
				[3, 9755, HEIGHT-140],
				[1, 9810, HEIGHT-140],
				[3, 9755, HEIGHT-170],
				[1, 9810, HEIGHT-170],
				[0, 9755, HEIGHT-225],
				[0, 9789, HEIGHT-225],
				[0, 9823, HEIGHT-225],
				#last air part of the level
				[0, 10400, HEIGHT-120]
				]

		#TODO REMOVE THIS
		#adding tree to background along the level
		x_trees=0
		back_trees=[]
		while x_trees < -self.level_limit:
			back_trees.append([0,x_trees,HEIGHT - 150])
			x_trees+=200

		"""Simple moving spikes"""
		#moving vert spikes
		#[orientation, top-left x, top-left y, top bound, bottom bound, speed]
		ver_mov_spikes = [
				[0, 10550, HEIGHT-245, HEIGHT-245, HEIGHT-19, 2],
				[0, 10710, HEIGHT-365, HEIGHT-365, HEIGHT-139, 2]
				]

		#moving horiz spikes
		#[orientation, top-left x, top-left y, left bound, right bound, speed]
		hor_mov_spikes = [
						]



		"""Some foes"""
		#TODO: REMOVE
		#Blobs dummies

		blobs = [[500, HEIGHT-100, 1, 2],
				[500, HEIGHT-100, -1, 2],
				]


		"""Some background"""
		#TODO REMOVE THIS
		#adding tree to background along the level
		x_trees=0
		back_trees=[]
		while x_trees < -self.level_limit:
			back_trees.append([0,x_trees,HEIGHT - 150])
			x_trees+=200



		"""Generation of the differents platforms/spikes"""
		# Go through the array above and add platforms
		for plat in level:
			block = Platform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		for plat in vert:
			block = MovingPlatform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.boundary_top = plat[4]
			block.boundary_bottom = plat[5]
			block.change_y = plat[6]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		for plat in horiz:
			block = MovingPlatform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.boundary_left = plat[4]
			block.boundary_right = plat[5]
			block.change_x = plat[6]
			block.player = self.player
			block.level = self
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

		for spike in spikes:
			block = Spike(spike[0])
			block.rect.x = spike[1]
			block.rect.y = spike[2]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		for spike in ver_mov_spikes:
			block = MovingSpike(spike[0])
			block.rect.x = spike[1]
			block.rect.y = spike[2]
			block.boundary_top = spike[3]
			block.boundary_bottom = spike[4]
			block.change_y = spike[5]
			block.player = self.player
			block.level = self
			self.platform_list.add(block)

		for tree in back_trees:
			block = Tree(tree[0])
			block.rect.x = tree[1]
			block.rect.y = tree[2]
			self.back_world_list.add(block)

		for pnj in blobs:
			enemy = Blob(pnj[2],pnj[3])
			enemy.rect.x = pnj[0]
			enemy.rect.y = pnj[1]
			enemy.player=self.player
			enemy.level=self
			self.pnj_list.add(enemy)

		#end platforms
		for plat in end_plat:
			block = EndPlatform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			block.level_pointer = plat[4]
			self.platform_list.add(block)

		#checkpoints platforms
		for plat in checkpoints:
			block = CheckPoint(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
			block.level = self
			#CheckPoint is red!
			block.image.fill(constants.RED)
			self.platform_list.add(block)




		"""here will stands specific platform for the different levels of difficulty"""

		#easy
		#[width, height, top-left x, top-left y]
		easy_plat = [
					[100, 20, 3400, HEIGHT],
					[100, 20, 3700, HEIGHT],
					[100, 20, 4000, HEIGHT],
					[80, 20, 4300, HEIGHT],
					[100, 20, 4650, HEIGHT],
					[80, 20, 6000, HEIGHT-300],
					[80, 20, 6250, HEIGHT-300],
					[100, 20, 6500, HEIGHT-300],
					]

		#[width, height, top-left x, top-left y, left bound, right bound, speed]
		easy_horiz = [
				[100, 20, 6700, HEIGHT-300, 6700, 6900, 2],
				[70, 20, 7200, HEIGHT-300, 7150, 7250, 1],
				[70, 20, 7400, HEIGHT-300, 7350, 7500, 2],
				[70, 20, 7700, HEIGHT-300, 7550, 7800, 2],
				#fast moving plateform
				[90, 20, 9760, HEIGHT-50, 9150, 9850, 3],
				[23, 30, 9795, HEIGHT-30, 9185, 9885, 3],
				]

		#falling roof at the end of the level
		#[width, height, top-left x, top-left y, top bound, bottom bound, speed down, speed up, pause down, pause up]
		easy_roofs = [
				[2100, HEIGHT-60, 12200, -HEIGHT+85, -HEIGHT+85, HEIGHT-60, 1, 3, 120, 60]
				]



		#medium
		medium_plat = [
					[100, 20, 3400, HEIGHT],
					[80, 20, 3700, HEIGHT],
					[50, 20, 4000, HEIGHT],
					[50, 20, 4300, HEIGHT],
					[30, 20, 4700, HEIGHT],
					#air platforms
					[50, 20, 6000, HEIGHT-300],
					[50, 20, 6250, HEIGHT-300],
					[50, 20, 6500, HEIGHT-300]
					]

		medium_horiz = [
				[100, 20, 6700, HEIGHT-300, 6700, 6900, 2],
				[70, 20, 7200, HEIGHT-300, 7150, 7250, 1],
				[50, 20, 7400, HEIGHT-300, 7350, 7500, 2],
				[50, 20, 7700, HEIGHT-300, 7550, 7800, 3],
				#fast moving plateform with spikes under it
				[90, 20, 9760, HEIGHT-50, 9150, 9850, 5],
				[23, 30, 9795, HEIGHT-30, 9185, 9885, 5]
				]

		medium_spikes = [
				[0, 8770, HEIGHT-135],
				[0, 8800, HEIGHT-135],
				[0, 8890, HEIGHT-45]
				]

		medium_horiz_spikes = [
						[3, 9750, HEIGHT-30, 9140, 9840, 5],
						[1, 9815, HEIGHT-30, 9205, 9905, 5],
						[3, 10900, HEIGHT-230, 10900, 12055, 10],
						[1, 10945, HEIGHT-230, 10945, 12100, 10]
						]

		#falling roof at the end of the level
		#[width, height, top-left x, top-left y, top bound, bottom bound, speed down, speed up, pause down, pause up]
		medium_roofs = [
				[2100, HEIGHT-60, 12200, -HEIGHT+85, -HEIGHT+85, HEIGHT-60, 1, 4, 120, 0]
				]


		if level_dif == "easy":
			for plat in easy_plat:
				block = Platform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for plat in easy_horiz:
				block = MovingPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_left = plat[4]
				block.boundary_right = plat[5]
				block.change_x = plat[6]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for roof in easy_roofs:
				block = SpecialPlatform(roof[0], roof[1])
				block.rect.x = roof[2]
				block.rect.y = roof[3]
				block.boundary_top = roof[4]
				block.boundary_bottom = roof[5]
				block.change_y = roof[6]
				block.change_y_d = roof[6]
				block.change_y_u = -roof[7]
				block.pause_down = roof[8]
				block.pause_up = roof[9]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			#create special moving spikes for the roof
			for i in number_spikes:
				block = SpecialSpike(2)
				block.rect.x = 12200 + (i*30)
				block.rect.y = 23
				block.boundary_top = 23
				block.boundary_bottom = HEIGHT-16
				block.change_y = 1
				block.change_y_d = 1
				block.change_y_u = -3
				block.pause_down = 120
				block.pause_up = 60
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

		elif level_dif == "medium":
			for plat in medium_plat:
				block = Platform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for plat in medium_horiz:
				block = MovingPlatform(plat[0], plat[1])
				block.rect.x = plat[2]
				block.rect.y = plat[3]
				block.boundary_left = plat[4]
				block.boundary_right = plat[5]
				block.change_x = plat[6]
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

			for spike in medium_horiz_spikes:
				block = MovingSpike(spike[0])
				block.rect.x = spike[1]
				block.rect.y = spike[2]
				block.boundary_left = spike[3]
				block.boundary_right = spike[4]
				block.change_x = spike[5]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for roof in medium_roofs:
				block = SpecialPlatform(roof[0], roof[1])
				block.rect.x = roof[2]
				block.rect.y = roof[3]
				block.boundary_top = roof[4]
				block.boundary_bottom = roof[5]
				block.change_y = roof[6]
				block.change_y_d = roof[6]
				block.change_y_u = -roof[7]
				block.pause_down = roof[8]
				block.pause_up = roof[9]
				block.player = self.player
				block.level = self
				self.platform_list.add(block)

			for i in number_spikes:
				block = SpecialSpike(2)
				block.rect.x = 12200 + (i*30)
				block.rect.y = 23
				block.boundary_top = 23
				block.boundary_bottom = HEIGHT-16
				block.change_y = 1
				block.change_y_d = 1
				block.change_y_u = -4
				block.pause_down = 120
				block.pause_up = 0
				block.player = self.player
				block.level = self
				self.platform_list.add(block)