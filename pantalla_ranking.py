import pygame
import sqlite3
import sys
import colores

def ranking(pantalla_principal):

    #SONIDOS
    pygame.mixer.music.set_volume(0.5)
    ranking_sound = pygame.mixer.Sound("chiptune-grooving-142242.mp3")
    pygame.mixer.music.set_volume(0.2)

    #CONEXION CON BDD
    conexion = sqlite3.connect("bd_btf.db")
    cursor = conexion.cursor()

    tabla = "players"

    #SELECCIONAR LAS COLUMNAS DE LA TABLA A MOSTRAR
    columnas_mostrar = ['NAME', 'SCORE', 'TIME']

    #OBTENER LOS DATOS DE LAS COLUMNAS SELECCIONADAS DESDE SQLITE3 SEGUN ORDEN
    columnas_query = ", ".join(columnas_mostrar)
    cursor.execute(f"SELECT {columnas_query} FROM {tabla} ORDER BY score DESC, time ASC, name ASC LIMIT 5")
    datos_tabla = cursor.fetchall()

    conexion.close()   


    posicion_espacio = (0, 0)

    pygame.init()

    #TEMPORIZADOR DURACION RANKING
    timer_ranking = pygame.USEREVENT + 0
    pygame.time.set_timer(timer_ranking, 8000)

    FPS = 60
    RELOJ = pygame.time.Clock()

    pantalla_principal.fill(colores.NEGRO)

    fuente_ranking = pygame.font.SysFont("Calibri", 50)
    fuente_tabla = pygame.font.SysFont("Calibri", 25)

    running = True

    while running:
        
        pygame.mixer.init()
        ranking_sound.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == timer_ranking:
                ranking_sound.stop()
                running = False

        #MOSTRAR EN LA PANTALLA LOS TITULOS DE LAS COLUMNAS ELEGIDAS
        x = 70
        y = 160
        for titulo_columna in columnas_mostrar:
            texto_renderizado = fuente_tabla.render(titulo_columna, True, (colores.BLANCO))
            pantalla_principal.blit(texto_renderizado, (x, y))
            x += 150

        #MOSTRAR LOS REGISTROS DE LAS COLUMNAS SELECCIONADAS
        x = 70
        y = 200
        for fila in datos_tabla:
            for columna in fila:
                texto_fila = str(columna)
                texto_renderizado = fuente_tabla.render(texto_fila, True, (colores.ROJO))
                pantalla_principal.blit(texto_renderizado, (x, y))
                x += 150
            x = 70
            y += 30
        

        texto_ranking = fuente_ranking.render("RANKING TOP 5", True, (colores.BLANCO))
        pantalla_principal.blit(texto_ranking, (95, 70))
        
        RELOJ.tick(FPS)    
        pygame.display.flip()
