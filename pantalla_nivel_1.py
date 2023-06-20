import pygame
import sys
import time
import random
import colores
from class_nave import Nave
from class_bullet import Bullet
from class_enemigo1 import Enemigo_1
from class_explosion import *
from class_score import Score
from class_vidas import Vidas
from pantalla_game_over import game_over


def nivel_1(pantalla_principal, nivel):


	pygame.init()

	posicion_espacio = (0, 0)

	#SONIDO
	pygame.mixer.music.set_volume(0.5)
	laser_sound = pygame.mixer.Sound("15 Fighter Shot2.mp3")
	explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
	pygame.mixer.music.load("assets/music.ogg")
	pygame.mixer.music.set_volume(0.2)

	pygame.mixer.music.play(loops=-1)	
	start_time = time.time()

	imagen_espacio = pygame.image.load("imagen_galaxia3.jpeg")

	clock = pygame.time.Clock()

	#CREACION GRUPOS DE SPRITE
	all_sprites = pygame.sprite.Group()
	enemigos_list = pygame.sprite.Group()
	bullets = pygame.sprite.Group()

	#INSTANCIA PLAYER
	player = Nave()
	all_sprites.add(player)

	#INSTANCIA ENEMIGOS
	for i in range(random.randrange(17,20)):
		enemigo_1 = Enemigo_1()
		all_sprites.add(enemigo_1)
		enemigos_list.add(enemigo_1)
	

	running = True

	while running:

		pygame.mixer.init()

		#TIEMPO DE JUEGO
		tiempo_transcurrido = round(time.time() - start_time)
		minutos = tiempo_transcurrido // 60
		segundos = tiempo_transcurrido % 60
		tiempo_formateado = "{:02d}:{:02d}".format(minutos, segundos)

		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#GENERACION DE DISPAROS	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					#INSTANCIA BALA
					bullet = Bullet(player.rect.centerx, player.rect.top)
					all_sprites.add(bullet)
					bullets.add(bullet)		
					laser_sound.play()	

		#ACTUALIZACION DE TODOS LOS SPRITES DE LA PANTALLA
		all_sprites.update()

		#VERIFICACION DE COLISION ENTRE EL GRUPO DE BALAS DEL PLAYER Y EL GRUPO DE ENEMIGOS
		#LOS ELIMINA AUTOMATICAMENTE
		hits = pygame.sprite.groupcollide(enemigos_list, bullets, True, True)
		for hit in hits:
			puntos = 50
			Score.update_score(puntos)
			explosion_sound.play()
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)

		#VERIFICACION DE COLISION ENTRE EL PLAYER Y EL GRUPO DE ENEMIGOS
		hits = pygame.sprite.spritecollide(player, enemigos_list, True)
		for hit in hits:
			perdida = 25
			Vidas.update_lives_player(perdida)
			explosion_sound.play()
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)

		#BLITEAR EL FONDO PRINCIPAL (ESPACIO)
		pantalla_principal.blit(imagen_espacio,(posicion_espacio)) 

		#BLITEAR TODOS LOS SPRITES DEL NIVEL
		all_sprites.draw(pantalla_principal)

		#GAME OVER
		if Vidas.shield < 25:
			explosion_sound.play()
			pygame.mixer.music.stop()
			running = False
			game_over(pantalla_principal)		
			
		#TRIUNFO
		if len(enemigos_list) == 0:
			pygame.mixer.music.stop()
			running = False

		font = pygame.font.SysFont("Consolas", 20)

		#RENDERIZACION SCORE - TIME - LEVEL
		score_1 = font.render("Score", True, (colores.ROJO))
		score_2 = font.render("{0}".format(Score.score_partida), True, (colores.ROJO))
		cronometro_1 = font.render("Time", True, (colores.BLANCO))
		cronometro_2 = font.render("{0}".format(tiempo_formateado), True, (colores.BLANCO))
		level = font.render(nivel, True, (colores.BLANCO))
				
		#BLITEAR TODOS LOS ELEMENTOS DEL NIVEL
		pantalla_principal.blit(score_1, (10,10))
		pantalla_principal.blit(score_2, (10, 30))
		pantalla_principal.blit(cronometro_1, (230,50))
		pantalla_principal.blit(cronometro_2, (225,70))
		pantalla_principal.blit(level, (220, 10))
		Vidas.dibujar_barra_vidas(pantalla_principal, 390, 10, Vidas.shield, colores.VERDE)

		pygame.display.flip()


	pygame.QUIT

