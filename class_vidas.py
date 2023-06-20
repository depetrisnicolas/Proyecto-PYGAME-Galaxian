import pygame

class Vidas:
	
    shield = 100
    shield_enemigo = 100

    def dibujar_barra_vidas(surface, x, y, percentage, color):
        BARRA_LENGHT = 100
        BARRA_HEIGHT = 10
        relleno = (percentage / 100) * BARRA_LENGHT
        border = pygame.Rect(x, y, BARRA_LENGHT, BARRA_HEIGHT)
        relleno = pygame.Rect(x, y, relleno, BARRA_HEIGHT)
        pygame.draw.rect(surface, color, relleno)
        pygame.draw.rect(surface, "white", border, 2)
        
    def update_lives_player(perdida):
        Vidas.shield -= perdida

    def update_lives_enemy(perdida):
        Vidas.shield_enemigo -= perdida

    def reiniciar_lives_player():
        Vidas.shield = 100

    def reiniciar_lives_enemy():
        Vidas.shield_enemigo = 100