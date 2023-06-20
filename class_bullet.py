import pygame
import colores

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("bullet.png")
		self.image = pygame.transform.scale(self.image, (8, 12))
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -7

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

