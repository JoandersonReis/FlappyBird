# Criando os obstaculos
from random import randint
import pygame

class Cano():
    '''Inicia 2 canos e suas caracteristicas'''
    def __init__(self, screen, conf, gs):
        self.gs = gs
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.conf = conf
        self.cor = (200, 255, 0)
        self.l = 100
        self.a = randint(100, 400)
        
        # Inicio das posições
        self.x = conf.width + 400
        self.e = 120

        # REnderiza os canos
        self.prep_img_cano_sup()
        self.prep_img_cano_inf()

    def prep_img_cano_sup(self):
        '''Prepara e atualiza a posição e imagem do cano superior'''
        self.cano_top = pygame.image.load("images/cano_top.png")
        self.cano_top = pygame.transform.scale(self.cano_top, [self.l, self.a])
        self.rect_top = self.cano_top.get_rect()
        self.rect_top.top = -1
        self.rect_top.left = self.x

    def prep_img_cano_inf(self):
        '''Prepara e atualiza a posição e imagem do cano inferior'''
        self.cano_inf = pygame.image.load("images/cano_bottom.png")
        self.cano_inf = pygame.transform.scale(self.cano_inf, [self.l, self.a + self.e * 5])
        self.rect_inf = self.cano_inf.get_rect()
        self.rect_inf.top = self.a + self.e
        self.rect_inf.left = self.x

    def desenha(self):
        '''Desenha os canos''' 
        self.screen.blit(self.cano_top, self.rect_top)
        self.screen.blit(self.cano_inf, self.rect_inf)

    def update(self):
        '''Atualiza a posição dos canos'''
        self.x -= self.gs.vel
        self.rect_top.left -= self.gs.vel
        self.rect_inf.left -= self.gs.vel

