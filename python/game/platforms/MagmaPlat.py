import constants
import pygame
from Platform import Platform
from MovingPlatform import MovingPlatform

class MagmaPlat(MovingPlatform):

	def update(self):

		MovingPlatform.update(self)

		self.player.rect.y += 1
		hit = not(self.player.rect.collidelist([self.rect]))
		self.player.rect.y -= 1

		if hit and not self.player.hit:
			self.player.hit = True
			self.player.change_y = -10