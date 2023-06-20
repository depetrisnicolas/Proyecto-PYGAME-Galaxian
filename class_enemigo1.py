import pygame
import colores
import random
import class_nave


class Enemigo_1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("enemigo1.png")
		self.image = pygame.transform.scale(self.image, (25, 25))
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(500 - self.rect.width)
		self.rect.y = random.randrange(-350, -100, 35)
		self.speedy = random.randrange(6, 9)

	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > 600 + 10 or self.rect.left < -40 or self.rect.right > 500 + 40:
			self.rect.x = random.randrange(500 - self.rect.width)
			self.rect.y = random.randrange(-140, - 100)
			self.speedy = random.randrange(4, 7)
		


    
                