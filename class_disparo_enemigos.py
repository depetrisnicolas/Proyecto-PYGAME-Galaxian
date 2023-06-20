import pygame
import colores

class Bullet_enemigo(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("assets\laser1.png")
		self.image = pygame.transform.scale(self.image, (18, 18))
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = 10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > 600:
			self.kill()

