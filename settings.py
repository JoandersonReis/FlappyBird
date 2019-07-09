import pygame

class Settings():

    def __init__(self):
        # Configurações de tela
        self.width = 600
        self.height = 700
        self.bg_color = (0, 0, 0)

class Tela():
    '''Inicia a tela de fundo e suas caracteristicas'''
    def __init__(self, janela):
        self.janela = janela
        self.bg = pygame.image.load("images/bg.png")
        self.bg2 = pygame.image.load("images/bg2.png")
        self.rect = self.bg.get_rect()
        self.rect2 = self.bg2.get_rect()
        self.rect2.left = 620

    def draw(self):
        '''Desenha o fundo'''
        self.janela.blit(self.bg, self.rect)
        self.janela.blit(self.bg2, self.rect2)

    def update(self):
        '''Atualiza o fundo'''
        self.rect.centerx -= 1
        self.rect2.centerx -= 1
    
    def check_fim_tela(self):
        '''Checa se chegou no final da tela e da um respaw nas imagens de bg'''
        if self.rect.right <= 0:
            self.rect.left = 620
        if self.rect2.right <= 0:
            self.rect2.left = 620
        
