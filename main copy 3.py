import pygame
import sqlite3
import time
from pantalla_inicio import inicio
from pantalla_nivel_1 import nivel_1
from pantalla_nivel_2 import nivel_2
from pantalla_nivel_3 import nivel_3
from pantalla_intervalo import intervalo
from pantalla_triunfo import triunfo
from pantalla_nombre_jugador import nombre_jugador
from pantalla_ranking import ranking
from class_score import Score
from class_inicio_juego import Inicio_juego
from class_nombre_jugador import Nombre_jugador

pygame.init()

#CREACION DE PANTALLA PRINCIPAL
pantalla_del_juego = pygame.display.set_mode((500, 600))
pygame.display.set_caption("G A L A X I A N")

running = True

#PANTALLAS
while running:

    if Inicio_juego.inicio_juego == False:
        inicio(pantalla_del_juego)
        Inicio_juego.inicio_juego = True

    if Inicio_juego.inicio_juego == True:
        #INICIA TIEMPO DE JUEGO
        start_time = time.time()
        intervalo(pantalla_del_juego, "LEVEL 1")
        nivel_1(pantalla_del_juego, "LEVEL 1")

    if Inicio_juego.inicio_juego == True:
        intervalo(pantalla_del_juego, "LEVEL 2")
        nivel_2(pantalla_del_juego, "LEVEL 2") 

    if Inicio_juego.inicio_juego == True:
        intervalo(pantalla_del_juego, "LEVEL 3")
        nivel_3(pantalla_del_juego, "LEVEL 3") 

    if Inicio_juego.inicio_juego == True:
        #FINALIZA TIEMPO DE JUEGO
        tiempo_transcurrido = round(time.time() - start_time)
        minutos = tiempo_transcurrido // 60
        segundos = tiempo_transcurrido % 60
        tiempo_formateado = "{:02d}:{:02d}".format(minutos, segundos)

        #FINAL
        triunfo(pantalla_del_juego, "SCORE {0}".format(Score.score_partida), "TIME {0}".format(tiempo_formateado))
        nombre_jugador(pantalla_del_juego)

        # ACTUALIZAR BDD
        # with sqlite3.connect("bd_btf.db") as conexion:
        #     try:
        #         conexion.execute("insert into players(name,time,score) values (?,?,?)", (Nombre_jugador.nombre_jugador, tiempo_formateado, Score.score_partida))
        #         conexion.commit()# Actualiza los datos realmente en la tabla
        #     except:
        #         print("Error")

        #MOSTRAR RANKING
        ranking(pantalla_del_juego)
        Inicio_juego.inicio_juego = False


