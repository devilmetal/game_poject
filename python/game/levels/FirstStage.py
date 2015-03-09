from Level import Level
from Platform import Platform
from MovingPlatform import MovingPlatform
from BoostPlatform import BoostPlatform
import constants
# Create platforms for the level

class FirstStage(Level):
	"""Overview of the "easy/standard" way of the first stage"""

	def __init__(self, player):

		Level.__init__(self, player)

		self.level_limit = -10000

		HEIGHT = constants.SCREEN_HEIGHT-20

		#array of platforms 
		#[width, height, top-left x coordinate, top-left y coordinate]
		level = [
				[3200, 20, 0, HEIGHT],
				[150, HEIGHT, 0, 0],
				[100, 120, 1000, HEIGHT-120],
				[100, 120, 1500, HEIGHT-120],
				[100, 240, 1600, HEIGHT-240],
				[100, 120, 1700, HEIGHT-120],
				[150, 10, 2000, HEIGHT-240],
				[100, 240, 2500, HEIGHT-240],
				#small platform on the ground
				[80, 20, 3500, HEIGHT],
				[70, 20, 3800, HEIGHT],
				[40, 20, 4000, HEIGHT],
				[30, 20, 4300, HEIGHT],
				[30, 20, 4700, HEIGHT],
				#small platform in the air right after the first horiz. mov. plat.
				[60, 20, 5750, HEIGHT-300],
				[60, 20, 6000, HEIGHT-300],
				[40, 20, 6400, HEIGHT-300],
				[100, 20, 6500, HEIGHT-300],
				#platform between moving plat in the air
				[50, 20, 7050, HEIGHT-300]
				]

		#array of vertical moving platform 
		#[width, height, top-left x, top-left y, top bound, bottom bound, speed]
		vert = [
				[60, 20, 4850, HEIGHT-20, HEIGHT-300, HEIGHT, 1]
				]


		#array of horizontal moving platform
		#[width, height, top-left x, top-left y, left bound, right bound, speed]
		horiz = [
				[60, 20, 5100, HEIGHT-300, 5100, 5600, 2],
				#chain moving platform in the air
				[100, 20, 6700, HEIGHT-300, 6700, 6900, 1],
				[50, 20, 7200, HEIGHT-300, 7200, 7300, 2],
				[20, 20, 7400, HEIGHT-300, 7400, 7500, 2],
				[20, 20, 7600, HEIGHT-300, 7550, 7800, 3]
				]

		#array of diag moving plat
		#[widght, height, top-left x, top-left y, left bound, right bound, top bound, bottom bound, speed]
		diag = [
				[100, 20, 7850, HEIGHT-300, 7850, 8130, HEIGHT-300, HEIGHT, 1]
				]

		# Go through the array above and add platforms
		for plat in level:
			block = Platform(plat[0], plat[1])
			block.rect.x = plat[2]
			block.rect.y = plat[3]
			block.player = self.player
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