import pygame
import sys
import colores
from class_inicio_juego import Inicio_juego

def game_over(pantalla_principal):


    pygame.init()

    pantalla_principal.fill(colores.NEGRO)

    FPS = 60
    RELOJ = pygame.time.Clock()

    timer_texto = pygame.USEREVENT + 0
    pygame.time.set_timer(timer_texto, 500)

    font = pygame.font.SysFont("Arial Black", 50)
    font_2 = pygame.font.SysFont("Arial Black", 30)

    pygame.mixer.music.set_volume(0.5)
    game_over_sound = pygame.mixer.Sound("Game Over.ogg")
    pygame.mixer.music.set_volume(0.2)

    running = True

    while running:
        
        pygame.mixer.init()
        game_over_sound.play(-1)

        teclas_presionadas = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if teclas_presionadas[pygame.K_RETURN]:
                running = False
                game_over_sound.stop()
                Inicio_juego.inicio_juego = False

        texto_game_over = font.render("GAME OVER", True, (colores.ROJO))
        texto_restart = font_2.render("RESTART", True, (colores.BLANCO))
        texto_press_enter = font_2.render("PRESS ENTER", True, (colores.BLANCO))
    
        pantalla_principal.blit(texto_game_over, (80,200))
        pantalla_principal.blit(texto_restart, (180,350))
        pantalla_principal.blit(texto_press_enter, (140,420))

        RELOJ.tick(FPS)    
        pygame.display.flip()
    
    pygame.QUIT
