# Criando o Passáro

import pygame
from random import randint


class Bird():
    # Inicia as caracteristicas do passaro
    def __init__(self, screen, gs):
        self.screen = screen
        self.gs = gs
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/bird.png")
        self.image_top = pygame.image.load("images/bird_top.png")
        self.image_bottom = pygame.image.load("images/bird_bottom.png")
        self.rect = self.image.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx - 23

    def desenha(self):
        self.screen.blit(self.image, self.rect)
    
    # Faz o passaro cair de acordo com o up
    def moveDown(self):
        if self.gs.up == 0:
            self.image = self.image_bottom
            self.rect.centery += self.gs.gravidade
    
    # Move para cima de acordo com o up
    def moveUp(self):
        if self.gs.up > 0:
            self.gs.up -= 1
            self.image = self.image_top
            self.rect.centery -= self.gs.vel


class Moeda():
    '''Inicia uma moeda e suas caracteristicas'''
    def __init__(self, screen, canos, gs):
        self.gs = gs
        self.screen = screen
        self.canos = canos
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("images/moeda.png")
        self.image = pygame.transform.scale(self.image, [20, 20])
        self.rect = self.image.get_rect()

        # Posiciona a moeda entre os canos
        self.rect.centery = canos.a + canos.e / 2
        self.rect.centerx = canos.x + canos.l / 2

    def desenha(self):
        '''Desenha a moeda'''
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        '''Atualiza a posição da moeda'''
        self.rect.centerx -= self.gs.vel


class Bau(Moeda):
    '''Inicia um baú e faz dele uma classe filha de Moeda'''
    def __init__(self, screen, canos, gs):
        super().__init__(screen, canos, gs)
        self.image = pygame.image.load("images/bau.jpg") 
        self.rect = self.image.get_rect()
        self.rect.centery = -100

        # Area de spaw do baú de acordo com os espaço entre os próximos obstáculos
        self.area_spaw_x = (canos.x - canos.x / 2, canos.x - 200)
        self.area_spaw_y = (100, canos.conf.height - 100)

    def random_spaw(self):
        '''Randomiza um spaw para o baú de acordo com a area de spaw'''
        self.rect.centerx = randint(self.area_spaw_x[0], self.area_spaw_x[1])
        self.rect.centery = randint(self.area_spaw_y[0], self.area_spaw_y[1])

    def desenha(self):
        '''Desenha o baú'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''Atualiza a posição do baú'''
        self.rect.centerx -= self.gs.vel


