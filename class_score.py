import pygame

class Score:
    score_partida = 0

    def update_score(puntos):
        Score.score_partida += puntos

    def reiniciar_score():
        Score.score_partida = 0