import pygame.font
from random import randint
import json

class GameStats():

    def __init__(self):
        self.reset_stats()
        # Status da música
        self.canal_sons = pygame.mixer.Channel(1)

        self.music = pygame.mixer.music.load("sounds/music_menu.wav")
        self.buy_skin = pygame.mixer.Sound("sounds/buy_skin.wav")
        self.select = pygame.mixer.Sound("sounds/select_menu.wav")
        self.asas = pygame.mixer.Sound("sounds/asas.wav")
        self.catch_coin = pygame.mixer.Sound("sounds/catch_coin.wav")
        self.catch_bau = pygame.mixer.Sound("sounds/catch_bau.wav")
        self.game_over = pygame.mixer.Sound("sounds/game_over.wav")

        self.price_skin1 = 500
        self.price_skin2 = 250

        # Carrega ou cria arquivo de salvamento
        try:
            with open('settings.json') as arquivo:
                save = json.load(arquivo)
                self.status_music = save[0]
                self.status_sons = save[1]
                self.skin1 = save[2]
                self.skin2 = save[3]
                self.skin1_active = save[4]
                self.skin2_active = save[5]
                self.skin_padrao_active = save[6]
                self.moedas = save[7]
                self.highscore = save[8]

        except:
            with open('settings.json', 'w') as arquivo:
                save = [self.status_music, self.status_sons, self.skin1, self.skin2, self.skin1_active, self.skin2_active, self.skin_padrao_active, self.moedas, self.highscore]
                json.dump(save, arquivo)

        if self.status_music:
            pygame.mixer.music.play()

    def reset_stats(self):
        '''Status que serão resetados quando começar um novo jogo'''
        # Status do pássaro
        self.vel = 10
        self.up = 0
        self.gravidade = 10
        self.menu_skin = False
        self.pegou_moeda = False
        self.pegou_bau = False

        # Status da tela
        self.pause = True

        # Status do Player e itens
        self.points = 0
        self.tot = 0
        self.nivel = 1
        self.nivel_bau = randint(3, 7)
        

class ScoreBoard():

    def __init__(self, screen, gs):
        self.gs = gs
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.cor = (0, 0, 0)

        # Configurações do score
        self.fonte = pygame.font.SysFont("Arial", 16)

        # Prepara a imagem da pontuação, moedas e recorde
        self.prep_score()
        self.prep_moedas()
        self.prep_highscore()


    def prep_score(self):
        # Renderiza os pontos
        self.score = f"Pontos: {self.gs.points}"
        self.score_image = self.fonte.render(self.score, True, self.cor)
        
        # Posiciona os pontos na tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10
    
    def prep_highscore(self):
        # Renderiza a imagem do Highscore
        self.highscore_str = f"Recorde: {self.gs.highscore}"
        self.highscore_img = self.fonte.render(self.highscore_str, True, self.cor)
        self.rect_highscore = self.highscore_img.get_rect()
        
        # Posiciona Highscore na tela
        self.rect_highscore.left = 10
        self.rect_highscore.top = 10
    
    def prep_moedas(self):
        # Renderiza as moedas e carrega a imagem da moeda
        self.img = pygame.image.load("images/moeda.png")
        self.img_rect = self.img.get_rect()
        self.moedas_str = f"X {int(self.gs.moedas)}"
        self.image_moedas = self.fonte.render(self.moedas_str, True, self.cor)
        self.rect_moedas = self.image_moedas.get_rect()

        # Posiciona a imagem da moeda e as moedas na tela
        self.rect_moedas.top = 10
        self.rect_moedas.centerx = self.screen_rect.centerx
        self.img_rect.right = self.rect_moedas.left - 10
        self.img_rect.top = 10


    def show_score(self):
        # Desenha a pontuação
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_img, self.rect_highscore)
        
        # Desenha as moedas
        if self.gs.pause:
            self.screen.blit(self.img, self.img_rect)
            self.screen.blit(self.image_moedas, self.rect_moedas)

        
