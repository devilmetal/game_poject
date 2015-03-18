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
		self.start_x = 12100
		self.start_y = HEIGHT - player.rect.height