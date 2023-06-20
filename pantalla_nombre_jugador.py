import pygame
import sys
import re
import tkinter
from tkinter.messagebox import showinfo as alert
import colores
from class_nombre_jugador import Nombre_jugador

def nombre_jugador(pantalla_principal):

    pygame.init()

    FPS = 60
    RELOJ = pygame.time.Clock()

    pantalla_principal.fill(colores.NEGRO)

    #SONIDOS
    pygame.mixer.music.set_volume(0.5)
    triunfo_sound = pygame.mixer.Sound("victory-electronic-video-game-soundtrack-denouement-credits-153944.mp3")
    pygame.mixer.music.set_volume(0.2)

    font = pygame.font.SysFont("Consola", 50)

    #ELEMENTOS EN PANTALLA
    logo_galaxian = pygame.image.load("galaxian logo 2.png")
    logo_galaxian = pygame.transform.scale(logo_galaxian, (350, 200))
    save_game = font.render("SAVE GAME", True, (colores.BLANCO))
    enter_your_name = font.render("ENTER YOUR NAME:", True, (colores.BLANCO))

    #VARIABLES PARA EL CAMPO DE ENTRADA DE TEXTO 
    input_box = pygame.Rect(150, 450, 200, 30)
    color_inactivo = pygame.Color(colores.VERDE)
    color_activo = pygame.Color(colores.CELESTE)
    font = pygame.font.Font(None, 36)
    activo = False
    text = ''

    running = True

    while running:    

        pygame.mixer.init()
        triunfo_sound.play(-1)

        teclas_presionadas = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if teclas_presionadas[pygame.K_SPACE]:
                triunfo_sound.stop()
                running = False

            #VERIFICAR QUE EL CLICK SEA SOBRE EL CAMPO DE TEXTO
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    activo = True
                else:
                    activo = False

            if event.type == pygame.KEYDOWN:
                if activo:
                    if event.key == pygame.K_RETURN:
                        if re.match("^[A-Za-z]+$", text):
                        #GUARDAR EL NOMBRE DEL JUGADOR Y PRINTEARLO
                            print("Nombre del jugador:", text)
                        else:
                        #MENSAJE DE ALERTA POR ERROR DE CARGA
                            alert(title = "ERROR", message = "Nombre inválido\n\nSolo se permiten caracteres alfabeticos")
                    elif event.key == pygame.K_BACKSPACE:
                        #ELIMINAR EL ULTIMO CARACTER INGRESADO 
                        text = text[:-1]
                    elif event.unicode:
                        #AGREGAR EL CARACTER INGRESADO AL TEXTO
                        text += event.unicode

        #LIMPIAR LA VENTANA
        pantalla_principal.fill((0, 0, 0))

        #DIBUJAR EL CAMPO DE ENTRADA DE TEXTO 
        pygame.draw.rect(pantalla_principal, color_activo if activo else color_inactivo, input_box, 2)

        #RENDERIZAR EL TEXTO INGRESADO EN EL CAMPO DE ENTRADA
        texto_ingresado = font.render(text, True, (colores.AMARILLO))
        pantalla_principal.blit(logo_galaxian,(80, 50))  
        pantalla_principal.blit(save_game, (145, 270))
        pantalla_principal.blit(enter_your_name, (80, 370))
        pantalla_principal.blit(texto_ingresado, (input_box.x + 5, input_box.y + 5))

        #Nombre_jugador.update_score(text)
 
        RELOJ.tick(FPS)    

        pygame.display.flip()

        

