import pygame
import colores


animaciones_exp = []
for i in range(9):
	file = "regularExplosion0{}.png".format(i)
	img = pygame.image.load(file)
	img.set_colorkey(colores.NEGRO)
	img_scale = pygame.transform.scale(img, (70,70))
	animaciones_exp.append(img_scale)


class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = animaciones_exp[0]
		self.rect = self.image.get_rect()
		self.rect.center = center 
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # VELOCIDAD DE LA EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(animaciones_exp):
				self.kill()
			else:
				center = self.rect.center
				self.image = animaciones_exp[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

	def actualizar_pantalla(self, ventana):
		ventana.blit(self.image, self.rect)