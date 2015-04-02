import constants
import pygame
from Platform import Platform
from MovingPlatform import MovingPlatform
from SpecialPlatform import SpecialPlatform
#import routines


class MagmaPlat(SpecialPlatform):

	def update(self):

		self.player.rect.y += 2
		hit = not(self.player.rect.collidelist([self.rect]))
		self.player.rect.y -= 2

		if hit and not self.player.hit:
			self.player.hit = True
			self.player.change_y = -10

		SpecialPlatform.update(self)

		