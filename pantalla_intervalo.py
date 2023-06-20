import pygame
import sys
import colores

def intervalo(pantalla_principal, nivel):

    pygame.init()

    FPS = 60
    RELOJ = pygame.time.Clock()

    pantalla_principal.fill(colores.NEGRO)

    #TEMPORIZADOR DURACION INTERVALO
    timer_intervalo = pygame.USEREVENT + 0
    pygame.time.set_timer(timer_intervalo, 1500)

    font = pygame.font.SysFont("Arial Black", 50)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == timer_intervalo:
                running = False
        
        texto_intervalo = font.render(nivel, True, (colores.BLANCO))
        
        pantalla_principal.blit(texto_intervalo, (140,200))

        RELOJ.tick(FPS)    
        pygame.display.flip()

        

