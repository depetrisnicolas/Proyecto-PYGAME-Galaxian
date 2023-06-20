import pygame
import sys
import time
import random
from class_nave import Nave
from class_bullet import Bullet
from class_disparo_enemigos import Bullet_enemigo
from class_enemigo1 import Enemigo_1
from class_enemigo2 import Enemigo_2
from class_nave_enemiga_boss import Nave_Boss
from class_score import Score
from class_vidas import Vidas
from class_explosion import *
import colores
from pantalla_game_over import game_over
from pantalla_intervalo import intervalo


def nivel_3(pantalla_principal, nivel):


	pygame.init()

	posicion_espacio = (0, 0)

	#SONIDOS
	pygame.mixer.music.set_volume(0.5)
	laser_sound = pygame.mixer.Sound("15 Fighter Shot2.mp3")
	explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
	pygame.mixer.music.load("Boss Fight.ogg")
	pygame.mixer.music.set_volume(0.2)
	pygame.mixer.music.play(loops=-1)	

	#INICIA TIEMPO
	start_time = time.time()

	imagen_espacio = pygame.image.load("imagen_galaxia3.jpeg")

	clock = pygame.time.Clock()

	#TIMER DISPAROS NAVE BOSS
	timer_disparo_enemigo = pygame.USEREVENT + 0
	pygame.time.set_timer(timer_disparo_enemigo, 300)

	#CREACION GRUPOS DE SPRITE
	all_sprites = pygame.sprite.Group()
	enemigos1_list = pygame.sprite.Group()
	enemigos2_list = pygame.sprite.Group()
	naves_enemigas_list = pygame.sprite.Group()
	bullets = pygame.sprite.Group()
	bullets_enemigo = pygame.sprite.Group()

	#INSTANCIA PLAYER
	player = Nave()
	nave_boss = Nave_Boss()
	all_sprites.add(player)


	#INSTANCIA ENEMIGOS 1
	for i in range(random.randrange(8, 12)):
		enemigo_1 = Enemigo_1()
		all_sprites.add(enemigo_1)
		enemigos1_list.add(enemigo_1)
	
	#INSTANCIA ENEMIGOS 2
	for i in range(random.randrange(10, 15)):
		enemigo_2 = Enemigo_2()
		all_sprites.add(enemigo_2)
		enemigos2_list.add(enemigo_2)

	running = True

	while running:

		pygame.mixer.init()

		#TIEMPO TRANSCURRIDO PARCIAL NIVEL
		tiempo_transcurrido = round(time.time() - start_time)
		minutos = tiempo_transcurrido // 60
		segundos = tiempo_transcurrido % 60
		tiempo_formateado = "{:02d}:{:02d}".format(minutos, segundos)

		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			#GENERACION DE DISPAROS PLAYER
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					bullet = Bullet(player.rect.centerx, player.rect.top)
					all_sprites.add(bullet)
					bullets.add(bullet)		
					laser_sound.play()	

			#GENERACION DE DISPAROS NAVE BOSS
			if event.type == timer_disparo_enemigo:
				bullet_enemigo = Bullet_enemigo(nave_boss.rect.centerx, nave_boss.rect.bottom)
				bullets_enemigo.add(bullet_enemigo)

		#ACTUALIZACION DE TODOS LOS SPRITES DE LA PANTALLA
		all_sprites.update()

		#VERIFICACION DE COLISION ENTRE EL GRUPO DE BALAS DEL PLAYER Y EL GRUPO DE ENEMIGOS 1
		#LOS ELIMINA AUTOMATICAMENTE
		hits = pygame.sprite.groupcollide(enemigos1_list, bullets, True, True)
		for hit in hits:
			puntos = 50
			Score.update_score(puntos)
			explosion_sound.play()
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)

		#VERIFICACION DE COLISION ENTRE EL GRUPO DE BALAS DEL PLAYER Y EL GRUPO DE ENEMIGOS 2
		#LOS ELIMINA AUTOMATICAMENTE
		hits = pygame.sprite.groupcollide(enemigos2_list, bullets, True, True)
		for hit in hits:
			puntos = 150
			Score.update_score(puntos)
			explosion_sound.play()
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)

		#VERIFICACION DE COLISION ENTRE EL GRUPO DE BALAS DEL PLAYER Y EL GRUPO DE NAVES BOSS
		#LOS ELIMINA AUTOMATICAMENTE
		hits = pygame.sprite.groupcollide(naves_enemigas_list, bullets, True, True)
		for hit in hits:
			puntos = 500
			Score.update_score(puntos)
			explosion_sound.play()
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)
			perdida = 25
			Vidas.update_lives_enemy(perdida)
			

		#VERIFICACION DE COLISION ENTRE EL PLAYER Y EL GRUPO DE ENEMIGOS 1
		hits = pygame.sprite.spritecollide(player, enemigos1_list, True)
		for hit in hits:
			perdida = 25
			Vidas.update_lives_player(perdida)
			explosion_sound.play()
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)

		#VERIFICACION DE COLISION ENTRE EL PLAYER Y EL GRUPO DE ENEMIGOS 2
		hits = pygame.sprite.spritecollide(player, enemigos2_list, True)
		for hit in hits:
			perdida = 25
			Vidas.update_lives_player(perdida)
			explosion_sound.play()
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)

		#VERIFICACION DE COLISION ENTRE EL PLAYER Y EL GRUPO DE NAVE BOSS	
		hits = pygame.sprite.spritecollide(player, naves_enemigas_list, True)
		for hit in hits:
			explosion_sound.play()
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)
			perdida = 100
			Vidas.update_lives_player(perdida)
		
		#VERIFICACION DE COLISION ENTRE EL PLAYER Y EL GRUPO DE BALAS DE LA NAVE BOSS
		hits = pygame.sprite.spritecollide(player, bullets_enemigo, True)
		for hit in hits:
			explosion_sound.play()
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)
			perdida = 100
			Vidas.update_lives_player(perdida)

		pantalla_principal.blit(imagen_espacio,(posicion_espacio)) 

		#BLITEAR EL FONDO PRINCIPAL (ESPACIO)		
		all_sprites.draw(pantalla_principal)

		#GAME OVER
		if Vidas.shield < 25:
			explosion_sound.play()
			pygame.mixer.music.stop()
			game_over(pantalla_principal)
			running = False
		
		#APARICION DE NAVE BOSS
		if len(enemigos1_list) == 0 and len(enemigos2_list) == 0: 
			naves_enemigas_list.add(nave_boss)
			all_sprites.add(nave_boss)
			bullets_enemigo.add(bullet_enemigo)
			all_sprites.add(bullet_enemigo)
			Vidas.dibujar_barra_vidas(pantalla_principal, 390, 30, Vidas.shield_enemigo, colores.ROJO)

		#TRIUNFO
		if Vidas.shield_enemigo < 25:
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

	return(Score.score_partida)