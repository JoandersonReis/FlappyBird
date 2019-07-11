# Define as funções do game

import pygame
import sys
from random import randint
from time import sleep
import json

# Da um reset no game posicionando tudo no seu lugar de inicio
def reset_game(gs, bird, canos, moeda, bau):
    gs.reset_stats()
    # Reset bird
    bird.rect.centerx = bird.screen_rect.centerx - 23
    bird.rect.centery = bird.screen_rect.centery
    bird.image = pygame.image.load("images/bird.png")
    # Reset canos
    canos.x = canos.conf.width + 400
    canos.prep_img_cano_sup()
    canos.prep_img_cano_inf()
    canos.a = randint(100, 400)
    # Reset moedas
    moeda.rect.centerx = canos.x + canos.l / 2
    moeda.rect.centery = canos.a + canos.e / 2
    # Reset baú e música
    bau.rect.centery = -100
    if gs.status_music:
        gs.music = pygame.mixer.music.load("sounds/game_song.wav")


# Verifica se o jogador ira receber pontos e adiciona pontos se o tot for 1 OBS: Se tot for 0 o jogador estará apto a passar pelos canos e ganhar um ponto
def check_points(rect, gs, bird, sb):
    if rect.centerx <= bird.rect.centerx - 50:
        gs.tot += 1
        if gs.tot > 1:
            pass
        else:
            gs.points += 1
            sb.prep_score()
            # Gerencia o sistema de Highscore
            if gs.points > gs.highscore:
                gs.highscore = gs.points
                sb.prep_highscore()


# Checa colisão dos canos com a bordas da tela
def check_canos_borda(canos, gs, moeda, bau):
    if canos.x + canos.l <= 0:
        canos.x = canos.conf.width
        canos.a = randint(100, 400)
        canos.prep_img_cano_sup()
        canos.prep_img_cano_inf()
        
        moeda.rect.centerx = canos.x + canos.l / 2
        moeda.rect.centery = canos.a + canos.e / 2
        
        gs.tot = 0

# Troca musica    
def troca_music(gs):
    if not gs.status_music:
        pygame.mixer.music.pause()
    else:
        gs.music = pygame.mixer.music.load("sounds/music_menu.wav")


# Checa a colisão do pássaro a objetos
def check_collision_bird(bird, canos, screen, gs, sb):
    screen_rect = screen.get_rect()  

    if bird.rect.bottom >= screen_rect.bottom or bird.rect.top <= 0:
        gs.pause = True
        pygame.mouse.set_visible(True)
        troca_music(gs)
        if gs.status_sons:
            gs.canal_sons.play(gs.game_over)

    if bird.rect.colliderect(canos.rect_top):
        gs.pause = True
        pygame.mouse.set_visible(True)
        troca_music(gs)
        if gs.status_sons:
            gs.canal_sons.play(gs.game_over)
    
    elif bird.rect.colliderect(canos.rect_inf):
        gs.pause = True
        pygame.mouse.set_visible(True)
        troca_music(gs)
        if gs.status_sons:
            gs.canal_sons.play(gs.game_over) 
    
    else:
        check_points(canos.rect_top, gs, bird, sb)


# Salva dados
def save(gs):
    with open("settings.json", "w") as arquivo:
        save = [gs.status_music, gs.status_sons, gs.skin1, gs.skin2, gs.skin1_active, gs.skin2_active, gs.skin_padrao_active, gs.moedas, gs.highscore]
        json.dump(save, arquivo)


# Função que checa o click no mouse
def click_button(mouse_x, mouse_y, gs, bird, canos, menu, sb, moeda, bau):
    click_play = menu.play.collidepoint(mouse_x, mouse_y)
    click_skin = menu.skin.collidepoint(mouse_x, mouse_y)
    click_sair = menu.sair.collidepoint(mouse_x, mouse_y)
    click_music = menu.rect_music.collidepoint(mouse_x, mouse_y)
    click_sons = menu.rect_sons.collidepoint(mouse_x, mouse_y)
    
    click_back = menu.back.collidepoint(mouse_x, mouse_y)
    click_skin1 = menu.skin1.collidepoint(mouse_x, mouse_y)
    click_skin2 = menu.skin2.collidepoint(mouse_x, mouse_y)
    click_button_skin_padrao = menu.skin_padrao.collidepoint(mouse_x, mouse_y)

    if click_play and gs.pause and not gs.menu_skin:
        reset_game(gs, bird, canos, moeda, bau)
        sb.prep_score()
        gs.pause = False
        
        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)

    # Pressiona o botão de skin caso esteja pausado e com parametro de skin apertado falso e transforma parametro de skin para True
    elif click_skin and gs.pause and not gs.menu_skin:
        gs.menu_skin = True
        if gs.status_sons:
            gs.canal_sons.play(gs.select)
    elif click_sair and gs.pause and not gs.menu_skin:
        save(gs)
        sys.exit()
    # Pressiona o botão de music para ativar ou desativar a musica
    elif click_music and gs.pause:
        if gs.status_sons:
            gs.canal_sons.play(gs.select)
        if gs.status_music:
            gs.status_music = False
            pygame.mixer.music.pause()
        else:
            gs.status_music = True
            gs.music = pygame.mixer.music.load("sounds/music_menu.wav")
            pygame.mixer.music.play()
        
        menu.prep_button_music()
    # Pressiona o botão de sons, para ativar ou desativar o som
    elif click_sons and gs.pause:
        if gs.status_sons:
            gs.canal_sons.play(gs.select)
            gs.status_sons = False
        else:
            gs.status_sons = True
        
        menu.prep_button_sons()
        
    # Pressiona o botão de back caso esteja pausado e com parametro de skin apertado True e transforma parametro de skin para False
    elif click_back and gs.menu_skin and gs.pause:
        gs.menu_skin = False
        if gs.status_sons:
            gs.canal_sons.play(gs.select)
    
    # Verifica se foi clikado o botão de skin1 caso menu_skin seja verdadeiro
    elif click_skin1 and gs.menu_skin and gs.pause:
        gs.skin1_active = True

        # Se tiver moedas suficiente compra a skin
        if not gs.skin1 and gs.moedas >= gs.price_skin1:
            gs.moedas -= gs.price_skin1
            sb.prep_moedas()
            menu.msg_skin1 = "Adquirido"
            gs.skin1 = True
            menu.prep_skin1()
            gs.click_button_skin_padrao = False
            if gs.status_sons:
                gs.canal_sons.play(gs.buy_skin)
        
        # Carrega a skin caso tenha sido comprada e a seleciona retirando a seleção das outras
        if gs.skin1 and gs.skin1_active:
            bird.image = pygame.image.load("skins/s1.png")
            bird.image_bottom = pygame.image.load("skins/sb1.png")
            bird.image_top = pygame.image.load("skins/su1.png")
            menu.color_button_skin1 = (0, 255, 0)
            menu.color_button_skin2 = (0, 100, 0)
            menu.color_button_skin_padrao = (0, 100, 0)
            gs.skin2_active = False
            gs.click_button_skin_padrao = False
    elif click_skin2 and gs.menu_skin and gs.pause:
        gs.skin2_active = True
        # Se tiver moedas suficiente compra a skin
        if not gs.skin2 and gs.moedas >= gs.price_skin2:
            gs.moedas -= gs.price_skin2
            sb.prep_moedas()
            menu.msg_skin2 = "Adquirido"
            gs.skin2 = True
            menu.prep_skin2()
            gs.click_button_skin_padrao = False
            if gs.status_sons:
                gs.canal_sons.play(gs.buy_skin)
        
        # Carrega a skin caso tenha sido comprada e a seleciona retirando a seleção das outras
        if gs.skin2 and gs.skin2_active:
            bird.image = pygame.image.load("skins/s2.png")
            bird.image_bottom = pygame.image.load("skins/sb2.png")
            bird.image_top = pygame.image.load("skins/su2.png")
            menu.color_button_skin2 = (0, 255, 0)
            menu.color_button_skin1 = (0, 100, 0)
            menu.color_button_skin_padrao = (0, 100, 0)
            menu.prep_skin2()
            gs.skin1_active = False
            gs.click_button_skin_padrao = False
    elif click_button_skin_padrao and gs.menu_skin and gs.pause:
        bird.image = pygame.image.load("images/bird.png")
        bird.image_bottom = pygame.image.load("images/bird_bottom.png")
        bird.image_top = pygame.image.load("images/bird_top.png")
        menu.color_button_skin_padrao = (0, 255, 0)
        menu.color_button_skin2 = (0, 100, 0)
        menu.color_button_skin1 = (0, 100, 0)
        gs.click_button_skin_padrao = True
        gs.skin1_active = False
        gs.skin2_active = False


# Checa se o passaro pegou a moeda
def check_catch_moeda(gs, bird, moeda, sb):
    if not gs.pegou_moeda and bird.rect.colliderect(moeda.rect):
        gs.moedas += gs.nivel
        sb.prep_moedas()
        gs.pegou_moeda = True
        if gs.status_sons:
            gs.canal_sons.play(gs.catch_coin)
    elif moeda.rect.centerx <= 0:
        gs.pegou_moeda = False


# Verifica se o passaro pegou o baú
def check_catch_bau(gs, bird, sb, bau):
    if not gs.pegou_bau and bird.rect.colliderect(bau.rect):
        gs.moedas += randint(5, 15)
        sb.prep_moedas()
        gs.nivel_bau = randint(3, 10)
        gs.pegou_bau = True
        if gs.status_sons:
            gs.canal_sons.play(gs.catch_bau)
    elif bau.rect.right <= 0:
        gs.pegou_bau = False


# Aumenta o nivel do jogo de acordo com os pontos
def more_level(gs, bau):
    if gs.points % 15 == 0 and gs.tot == 1:
        gs.nivel += 1
        gs.vel += 1    


def events(bird, gs, canos, menu, sb, moeda, bau):
    # Verifica os eventos do teclado e mouse
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save(gs)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if gs.status_sons:
                        gs.canal_sons.play(gs.asas)
                    gs.up = 6
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                click_button(mouse_x, mouse_y, gs, bird, canos, menu, sb, moeda, bau)


# Verifica se pode desenhar ou respawnar o baú
def spaw_draw_bau(gs, bau):
    if gs.points % gs.nivel_bau == 0 and gs.tot == 1:
        bau.random_spaw()       
    if gs.points % gs.nivel_bau == 0 and bau.rect.right >= 0 and not gs.pegou_bau:
        bau.desenha()


def update_screen(gs, canos, bird, sb, moeda, menu, screen, tela, conf, bau):
    events(bird, gs, canos, menu, sb, moeda, bau)
    screen.fill(conf.bg_color)
    tela.draw()
    tela.update()
    tela.check_fim_tela()

    # Desenha o passaro, cano e a moeda na tela
    if not gs.pegou_moeda:
        moeda.desenha()

    # Desenha bird e canos
    bird.desenha()
    canos.desenha()

    # Loop infinito da música carregada
    if gs.status_music and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
    
    # Esquema de pause
    if not gs.pause:    
        '''Ações caso o jogo não esteja pausado'''
        bird.moveDown()
        bird.moveUp()
        check_canos_borda(canos, gs, moeda, bau)
        check_collision_bird(bird, canos, screen, gs, sb)
        check_catch_moeda(gs, bird, moeda, sb)
        canos.update()
        moeda.update()
        more_level(gs, bau)
        check_catch_bau(gs, bird, sb, bau)
        spaw_draw_bau(gs, bau)
        bau.update()
    elif gs.pause and not gs.menu_skin:
        menu.show_buttons()
    elif gs.pause and gs.menu_skin:
        menu.show_buttons_skin()

    # Desenha pontuação
    sb.show_score()

    # Atualiza o jogo
    pygame.display.flip()
