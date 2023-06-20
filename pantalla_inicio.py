import pygame
import sys
import colores
from class_score import Score
from class_vidas import Vidas


def inicio(pantalla_principal):

    pygame.init()

    FPS = 60
    RELOJ = pygame.time.Clock()

    Score.reiniciar_score()
    Vidas.reiniciar_lives_player()
    Vidas.reiniciar_lives_enemy()
    
    #SONIDO
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    sonido_inicio = pygame.mixer.Sound("ARCADE GAME SERIES_ GALAGA - full soundtrack _ OST.mp3")
    sonido_inicio.set_volume(0.2)
    

    pantalla_principal.fill(colores.NEGRO)

    logo_galaxian = pygame.image.load("galaxian logo.png")
    logo_galaxian = pygame.transform.scale(logo_galaxian, (300, 100))

    fuente_inicio = pygame.font.SysFont("arialblack", 25)

    running = True

    while running:

        sonido_inicio.play(-1)

        teclas_presionadas = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if teclas_presionadas[pygame.K_RETURN]:
                sonido_inicio.stop()
                running = False


        star = fuente_inicio.render("STAR", True, (colores.BLANCO))
        press_enter = fuente_inicio.render("PRESS ENTER", True, (colores.BLANCO))
        
        pantalla_principal.blit(logo_galaxian,(100, 100))    
        pantalla_principal.blit(star, (215,350))
        pantalla_principal.blit(press_enter, (155,400))

        RELOJ.tick(FPS)    
        pygame.display.flip()
    
        

