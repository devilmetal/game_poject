import constants
import pygame
from Platform import Platform
from MovingPlatform import MovingPlatform
from SpecialPlatform import SpecialPlatform
import routines


class MagmaPlat(SpecialPlatform):
	def __init__ (self, width, height):
		super(Platform, self).__init__()
		
		self.image = pygame.Surface([width, height])
		magma_image = routines.load_png('world/lava/magma.png')
		magma_texture = pygame.transform.scale(magma_image[0], (width, height))
		self.image.blit(magma_texture, (0, 0))
		self.rect = self.image.get_rect()

		self.subblock = pygame.sprite.Group()

	def update(self):

		self.player.rect.y += 2
		hit = not(self.player.rect.collidelist([self.rect]))
		self.player.rect.y -= 2

		if hit and not self.player.hit:
			self.player.hit = True
			self.player.change_y = -10

		self.player.rect.y -= 2
		hit = not(self.player.rect.collidelist([self.rect]))
		self.player.rect.y += 2

		if hit and not self.player.hit:
			self.player.hit = True
			self.player.change_y = -10

		self.player.rect.x -= 2
		hit = not(self.player.rect.collidelist([self.rect]))
		self.player.rect.x += 2

		if hit and not self.player.hit:
			self.player.hit = True
			self.player.change_y = -10

		self.player.rect.y += 2
		hit = not(self.player.rect.collidelist([self.rect]))
		self.player.rect.y -= 2

		if hit and not self.player.hit:
			self.player.hit = True
			self.player.change_y = -10

		SpecialPlatform.update(self)

		