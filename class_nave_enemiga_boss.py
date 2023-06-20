import pygame
import colores
import random



class Nave_Boss(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("nave_enemiga_boss.png")
		self.image = pygame.transform.scale(self.image, (30, 35))
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(500 - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speedy = 7
		self.speedx = random.randrange(-2, 2)

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > 610 or self.rect.left < -40 or self.rect.right > 540:
			self.rect.x = random.randrange(500 - self.rect.width)
			self.rect.y = random.randrange(-140, -100)
			self.speedy = 7
		
	def actualizar_pantalla(self, ventana):
		ventana.blit(self.image, self.rect)

            

                    


        


