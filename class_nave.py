import pygame
import colores



class Nave(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("nave2 (1).png")
		self.image = pygame.transform.scale(self.image, (30, 30))
		self.rect = self.image.get_rect()
		self.rect.centerx = 500 // 2
		self.rect.bottom = 600
		self.speed_x = 0


	def update(self):
		self.speed_x = 0
		lista_teclas = pygame.key.get_pressed()
		if lista_teclas[pygame.K_LEFT]:
			self.speed_x = -5
		if lista_teclas[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > 500:
			self.rect.right = 500
		if self.rect.left < 0:
			self.rect.left = 0

	def actualizar_pantalla(self, ventana):
		ventana.blit(self.image, self.rect)


                    


        


