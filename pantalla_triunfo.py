import pygame
import sys
import colores

def triunfo(pantalla_principal, score, tiempo):


    pygame.init()

    FPS = 60
    RELOJ = pygame.time.Clock()

    pantalla_principal.fill(colores.NEGRO)

    #SONIDOS
    pygame.mixer.music.set_volume(0.5)
    triunfo_sound = pygame.mixer.Sound("13. Ending.mp3")
    pygame.mixer.music.set_volume(0.2)


    logo_triunfo = pygame.image.load("you win.png")
    logo_triunfo = pygame.transform.scale(logo_triunfo, (350, 180))

    timer_triunfo = pygame.USEREVENT + 0
    pygame.time.set_timer(timer_triunfo, 10000)

    font = pygame.font.SysFont("Arial Black", 25)

    running = True

    while running:    

        pygame.mixer.init()
        triunfo_sound.play(-1)

        teclas_presionadas = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if teclas_presionadas[pygame.K_RETURN]:
                running = False
                triunfo_sound.stop()
        
        texto_score = font.render(score, True, (colores.BLANCO))
        texto_tiempo = font.render(tiempo, True, (colores.BLANCO))
        texto_press_key = font.render("PRESS ENTER", True, (colores.AMARILLO))
        
        pantalla_principal.blit(logo_triunfo, (80, 100))
        pantalla_principal.blit(texto_score, (170,350))
        pantalla_principal.blit(texto_tiempo, (180,400))
        pantalla_principal.blit(texto_press_key, (160,450))
 
        RELOJ.tick(FPS)    

        pygame.display.flip()


