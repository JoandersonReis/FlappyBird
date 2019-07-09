import pygame.font
import pygame


class Menu():

    def __init__(self, screen, gs):
        self.msg_skin1 = f"{gs.price_skin1} Moedas"
        self.msg_skin2 = f"{gs.price_skin2} Moedas"

        self.gs = gs

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.color_text = (255, 255, 255)
        self.color_button = (0, 255, 0)
        self.color_button_skin1 = (0, 100, 0)
        self.color_button_skin2 = (0, 100, 0)
        self.color_button_skin_padrao = (0, 255, 0)

        self.b_width, self.b_height = 200, 50

        self.font = pygame.font.SysFont("Arial", 32)
        self.font_skin = pygame.font.SysFont("Arial", 18)
        
        # Cria o background dos botões
        self.play = pygame.Rect(0, 0, self.b_width, self.b_height)
        self.skin = pygame.Rect(0, 0, self.b_width, self.b_height)
        self.sair = pygame.Rect(0, 0, self.b_width, self.b_height)
        self.back = pygame.Rect(0, 0, 50, 20)
        self.skin1 = pygame.Rect(0, 0, self.b_width, self.b_height)
        self.skin2 = pygame.Rect(0, 0, self.b_width, self.b_height)
        self.skin_padrao = pygame.Rect(0, 0, self.b_width, self.b_height)

        # Prepara as configurações dos botões
        self.prep_button_play()
        self.prep_button_skin()
        self.prep_button_exit()
        self.prep_button_music()
        self.prep_button_sons()
        self.prep_button_back()
        self.prep_skin1()
        self.prep_skin2()
        self.prep_skin_padrao()

    def prep_button_play(self):
        # Renderiza o botão de play
        msg = "Jogar"
        self.image_play = self.font.render(msg, True, self.color_text, self.color_button)
        self.rect_play = self.image_play.get_rect()

        # Posiciona o botão de play
        self.play.centerx = self.screen_rect.centerx
        self.play.centery = self.screen_rect.centery - 100
        self.rect_play.center = self.play.center

    def prep_button_skin(self):
        # Renderiza o botão Skin
        msg = "Skin"
        self.image_skin = self.font.render(msg, True, self.color_text, self.color_button)
        self.rect_skin = self.image_skin.get_rect()

        # Posiciona o botão de Skin
        self.skin.centerx = self.screen_rect.centerx
        self.skin.centery = self.screen_rect.centery
        self.rect_skin.center = self.skin.center

    def prep_button_exit(self):
        # Renderiza o botão de sair
        msg = "Sair"
        self.image_sair = self.font.render(msg, True, self.color_text)
        self.rect_sair = self.image_sair.get_rect()

        # Posiciona o botão de sair
        self.sair.centerx = self.screen_rect.centerx
        self.sair.centery = self.screen_rect.centery + 100
        self.rect_sair.center = self.sair.center

    def prep_button_music(self):
        # Renderiza a imagem de musica off e on 
        if self.gs.status_music:
            self.imagem_music = pygame.image.load("images/music_on.png")
        else:
            self.imagem_music = pygame.image.load("images/music_off.png")

        # Posiciona aimagem de música off e on
        self.rect_music = self.imagem_music.get_rect()
        self.rect_music.right = self.screen_rect.right - 60
        self.rect_music.bottom = self.screen_rect.bottom - 10

    def prep_button_sons(self):
        if self.gs.status_sons:
            self.imagem_sons = pygame.image.load("images/sons_on.png")
        else:
            self.imagem_sons = pygame.image.load("images/sons_off.png")

        self.rect_sons = self.imagem_sons.get_rect()
        self.rect_sons.right = self.screen_rect.right - 20
        self.rect_sons.bottom = self.screen_rect.bottom - 10

    def prep_button_back(self):
        # Renderiza o botão Voltar
        msg = "voltar"
        font = pygame.font.SysFont("Arial", 16)
        self.image_back = font.render(msg, True, self.color_text, self.color_button)
        self.rect_back = self.image_back.get_rect()

        # Posiciona o botão de Voltar
        self.back.centerx = self.screen_rect.centerx - 60
        self.back.centery = self.screen_rect.centery - 100
        self.rect_back.center = self.back.center

    def prep_skin1(self):
        # Renderiza o botão da skin vermelha
        self.image_skin1 = self.font_skin.render(self.msg_skin1, True, self.color_text)
        self.rect_skin1 = self.image_skin1.get_rect()

        # Posiciona o botão com a msg
        self.skin1.centerx = self.screen_rect.centerx
        self.skin1.centery = self.screen_rect.centery - 30
        self.rect_skin1.centery = self.skin1.centery
        self.rect_skin1.centerx = self.skin1.centerx + 20 

        # Posiciona o sprite do passaro vermelho
        self.img_bird_skin1 = pygame.image.load("skins/s1.png")
        self.rect_bird_skin1 = self.img_bird_skin1.get_rect()
        self.rect_bird_skin1.centerx = self.skin1.centerx - 60
        self.rect_bird_skin1.centery = self.skin1.centery

    def prep_skin2(self):
        # Renderiza o botão da skin verde
        self.image_skin2 = self.font_skin.render(self.msg_skin2, True, self.color_text)
        self.rect_skin2 = self.image_skin2.get_rect()

        # Posiciona o botão com a msg
        self.skin2.centerx = self.screen_rect.centerx
        self.skin2.centery = self.screen_rect.centery + 30
        self.rect_skin2.centery = self.skin2.centery
        self.rect_skin2.centerx = self.skin2.centerx + 20 

        # Posiciona o sprite do passaro verde
        self.img_bird_skin2 = pygame.image.load("skins/s2.png")
        self.rect_bird_skin2 = self.img_bird_skin2.get_rect()
        self.rect_bird_skin2.centerx = self.skin2.centerx - 60
        self.rect_bird_skin2.centery = self.skin2.centery

    def prep_skin_padrao(self):
        # Prepara a skin padrão
        msg = "Adquirido"
        self.imagem_padrao = self.font_skin.render(msg, True, self.color_text)
        self.rect_padrao = self.imagem_padrao.get_rect()

        # Posiciona o nome ao lado da imagem de skin
        self.skin_padrao.centerx = self.screen_rect.centerx
        self.skin_padrao.centery = self.screen_rect.centery + 90
        self.rect_padrao.centerx = self.skin_padrao.centerx + 20
        self.rect_padrao.centery = self.skin_padrao.centery

        # Posiciona a skin padrão dentro do botão
        self.img_skin_padrao = pygame.image.load("images/bird.png")
        self.rect_img_padrao = self.img_skin_padrao.get_rect()
        self.rect_img_padrao.centerx = self.skin_padrao.centerx - 60
        self.rect_img_padrao.centery = self.skin_padrao.centery

    def show_buttons(self):
        # Desenha o botão de Play
        self.screen.fill(self.color_button, self.play)
        self.screen.blit(self.image_play, self.rect_play)

        # Desenha o botão de Skin
        self.screen.fill(self.color_button, self.skin)
        self.screen.blit(self.image_skin, self.rect_skin)

        # Desenha o botão de sair
        self.screen.fill(self.color_button, self.sair)
        self.screen.blit(self.image_sair, self.rect_sair)

        # Desenha o botão de musica e sons
        self.screen.blit(self.imagem_music, self.rect_music)
        self.screen.blit(self.imagem_sons, self.rect_sons)

    def show_buttons_skin(self):
        # Desenha o botão back
        self.screen.fill(self.color_button, self.back)
        self.screen.blit(self.image_back, self.rect_back)

        # Desenha o botão de skin 1
        self.screen.fill(self.color_button_skin1, self.skin1)
        self.screen.blit(self.img_bird_skin1, self.rect_bird_skin1)
        self.screen.blit(self.image_skin1, self.rect_skin1)

        # Desenha o botão de skin 2
        self.screen.fill(self.color_button_skin2, self.skin2)
        self.screen.blit(self.img_bird_skin2, self.rect_bird_skin2)
        self.screen.blit(self.image_skin2, self.rect_skin2)

        # Desenha o botão de skin padrão
        self.screen.fill(self.color_button_skin_padrao, self.skin_padrao)
        self.screen.blit(self.img_skin_padrao, self.rect_img_padrao)
        self.screen.blit(self.imagem_padrao, self.rect_padrao)

