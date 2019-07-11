import pygame

from settings import *
from bird import *
from game_functions import *
from game_stats import *
from canos import *
from menu import *

def run():
    pygame.init()
    conf = Settings()
    gs = GameStats()
    screen = pygame.display.set_mode((conf.width, conf.height))
    tela = Tela(screen)
    sb = ScoreBoard(screen, gs)
    bird = Bird(screen, gs)
    canos = Cano(screen, conf, gs)
    menu = Menu(screen, gs)
    moeda = Moeda(screen, canos, gs)
    bau = Bau(screen, canos, gs)
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()

    while True:
        clock.tick(25)
        
        # Atualiza funções do jogo
        update_screen(gs, canos, bird, sb, moeda, menu, screen, tela, conf, bau)
        
run()
