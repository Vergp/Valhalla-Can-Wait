import socket
import pygame
from random import randint, randrange
from data.opening import abertura

# Conexão do Cliente com Servidor - REDES

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1234))


# Iniciando o pygame
pygame.init()

# Cores
yellow = (255, 255, 0)
white = (255, 255, 255)
green = (38, 166, 7)
black = (0, 0, 0)
red = (186, 30, 30)

# Criação tela do jogo
icon = pygame.image.load("data/icon.png")
pygame.display.set_icon(icon)
tLargura = 800
tAltura = 600
tela = pygame.display.set_mode((tLargura, tAltura))
gameOVer = pygame.image.load("data/gameOver.jpg")
rectgameover = gameOVer.get_rect()

# Menu
bgMenu = pygame.image.load("data/menuzin.png").convert()
rectMenu = bgMenu.get_rect()
name = pygame.image.load("data/skjaldmo.png")
jogar = pygame.image.load("data/jogar.png")
sair = pygame.image.load("data/sair.png")

Demofim = pygame.image.load("data/endDemo.png")

#Prologo
textin = pygame.image.load("data/cinematic2.png").convert()
rectTexto = textin.get_rect()

#SCORE
newScore = 0
score = 0

# Fase 1
bg1 = pygame.image.load('data/bg1.png')
falas = [
    pygame.image.load("data/falas/invis.png"), pygame.image.load("data/falas/fala1.png"),
    pygame.image.load("data/falas/fala2.png"), pygame.image.load("data/falas/fala3.png"),
    pygame.image.load("data/falas/fala4.png"), pygame.image.load("data/falas/fala6.png"),
    pygame.image.load("data/falas/fala7.png"), pygame.image.load("data/falas/invis.png"),
    pygame.image.load("data/falas/fala8.png")
]
falinhas = 1
falax, falay = 480, 180

bg2 = pygame.image.load('data/bg2.png')
bgX = 0
bgY = 0

# Lagherta
lagerthaD = pygame.image.load("data/lagertha/lagerthaD.png")
lagerthaE = pygame.image.load("data/lagertha/lagerthaE.png")
lagerthaF = pygame.image.load("data/lagertha/lagertha_frente.png")

# Animação Player
pDireita = [
    pygame.image.load('data/Direita/machado_classico_000.png'), pygame.image.load('data/Direita/machado_classico_001.png'),
    pygame.image.load('data/Direita/machado_classico_002.png'), pygame.image.load('data/Direita/machado_classico_003.png'),
    pygame.image.load('data/Direita/machado_classico_004.png'), pygame.image.load('data/Direita/machado_classico_005.png'),
    pygame.image.load('data/Direita/machado_classico_006.png'), pygame.image.load('data/Direita/machado_classico_007.png'),
    pygame.image.load('data/Direita/machado_classico_008.png'), pygame.image.load('data/Direita/machado_classico_009.png'),
    pygame.image.load('data/Direita/machado_classico_010.png'), pygame.image.load('data/Direita/machado_classico_011.png'),
    pygame.image.load('data/Direita/machado_classico_012.png'), pygame.image.load('data/Direita/machado_classico_013.png'),
    pygame.image.load('data/Direita/machado_classico_014.png'), pygame.image.load('data/Direita/machado_classico_015.png'),
    pygame.image.load('data/Direita/machado_classico_016.png'), pygame.image.load('data/Direita/machado_classico_017.png'),
    pygame.image.load('data/Direita/machado_classico_018.png'), pygame.image.load('data/Direita/machado_classico_019.png'),
    pygame.image.load('data/Direita/machado_classico_020.png'), pygame.image.load('data/Direita/machado_classico_021.png'),
    pygame.image.load('data/Direita/machado_classico_022.png'), pygame.image.load('data/Direita/machado_classico_023.png'),
    pygame.image.load('data/Direita/machado_classico_024.png')
]
pEsquerda = [
    pygame.image.load('data/Esquerda/machado_esquerda_000.png'), pygame.image.load('data/Esquerda/machado_esquerda_001.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_002.png'), pygame.image.load('data/Esquerda/machado_esquerda_003.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_004.png'), pygame.image.load('data/Esquerda/machado_esquerda_005.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_006.png'), pygame.image.load('data/Esquerda/machado_esquerda_007.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_008.png'), pygame.image.load('data/Esquerda/machado_esquerda_009.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_010.png'), pygame.image.load('data/Esquerda/machado_esquerda_011.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_012.png'), pygame.image.load('data/Esquerda/machado_esquerda_013.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_014.png'), pygame.image.load('data/Esquerda/machado_esquerda_015.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_016.png'), pygame.image.load('data/Esquerda/machado_esquerda_017.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_018.png'), pygame.image.load('data/Esquerda/machado_esquerda_019.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_020.png'), pygame.image.load('data/Esquerda/machado_esquerda_021.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_022.png'), pygame.image.load('data/Esquerda/machado_esquerda_023.png'),
    pygame.image.load('data/Esquerda/machado_esquerda_024.png')
]
playerD = pygame.image.load('data/paradadir.png')
playerE = pygame.image.load('data/paradaesq.png')

atacando = [
    pygame.image.load('data/machado1/ataque_000.png'), pygame.image.load('data/machado1/ataque_001.png'),
    pygame.image.load('data/machado1/ataque_002.png'), pygame.image.load('data/machado1/ataque_003.png'),
    pygame.image.load('data/machado1/ataque_004.png'), pygame.image.load('data/machado1/ataque_005.png'),
    pygame.image.load('data/machado1/ataque_006.png'), pygame.image.load('data/machado1/ataque_007.png'),
    pygame.image.load('data/machado1/ataque_008.png'), pygame.image.load('data/machado1/ataque_009.png'),
    pygame.image.load('data/machado1/ataque_010.png')
]

atkSom = pygame.mixer.Sound("data/swish_2.wav")

timer = 0

# Animação Inimigo

inimigoA = [
    pygame.image.load('data/Inimig/Ataque_Inimigo_000.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_001.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_002.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_003.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_004.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_005.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_006.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_007.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_008.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_009.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_010.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_011.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_012.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_013.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_014.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_015.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_016.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_017.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_018.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_019.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_020.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_021.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_022.png'), pygame.image.load('data/Inimig/Inimigo_Esquerda_023.png'),
    pygame.image.load('data/Inimig/Inimigo_Esquerda_024.png')
]
inimigoAtk = [
    pygame.image.load("data/Inimig/Ataque_Inimigo_000.png"), pygame.image.load("data/Inimig/Ataque_Inimigo_001.png"),
    pygame.image.load("data/Inimig/Ataque_Inimigo_002.png"), pygame.image.load("data/Inimig/Ataque_Inimigo_003.png"),
    pygame.image.load("data/Inimig/Ataque_Inimigo_004.png"), pygame.image.load("data/Inimig/Ataque_Inimigo_006.png"),
    pygame.image.load("data/Inimig/Ataque_Inimigo_007.png"), pygame.image.load("data/Inimig/Ataque_Inimigo_008.png"),
    pygame.image.load("data/Inimig/Ataque_Inimigo_009.png"), pygame.image.load("data/Inimig/Ataque_Inimigo_010.png"),
    pygame.image.load("data/Inimig/Ataque_Inimigo_011.png"), pygame.image.load("data/Inimig/Ataque_Inimigo_012.png"),
    pygame.image.load("data/Inimig/Ataque_Inimigo_013.png"), pygame.image.load("data/Inimig/Ataque_Inimigo_014.png"),
    pygame.image.load("data/Inimig/Ataque_Inimigo_015.png"), pygame.image.load("data/Inimig/Ataque_Inimigo_000.png")
]

ini1morto = pygame.image.load("data/inimigocaido.png")
# Inserindo título na tela do jogo
pygame.display.set_caption("Valhalla Can Wait")

# Controla o FPS
relogio = pygame.time.Clock()

# Atributos do Player
hp = 200
pos_x = 100
pos_y = 300
larPlayer = 130
altPlayer = 214
vel = 5
colisaoPlayer = 0

direita = False
esquerda = False
nd = False
ne = False
ataque = False
walkCount = 0
atkCount = 1

# Atributos Inimigos
enemy1hp = 100
inimigoX1 = 1200
inimigoY1 = 200
vel_ini1 = 0
enemyCount1 = 0
atkenemyCount1 = 0
colisaoEnemy1 = 0
ini1dir = False
ini1esq = False
ini1atk = False

enemy2hp = 100
inimigoX2 = 500
inimigoY2 = 280
vel_ini2 = 0
enemyCount2 = 0
atkenemyCount2 = 0
colisaoEnemy2 = 0
ini2dir = False
ini2esq = False
ini2atk = False

enemy3hp = 100
inimigoX3 = 1100
inimigoY3 = 200
vel_ini3 = 0
enemyCount3 = 0
atkenemyCount3 = 0
colisaoEnemy3 = 0
ini3dir = False
ini3esq = False
ini3atk = False

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)  # Cria uma fonte do sistema
    texto1 = font.render(msg, True, cor)  # render() - função para desenhar o texto na superficie
    tela.blit(texto1, [x, y])


def fase1():
    global f1
    global colisaoPlayer
    global colisaoEnemy1
    global atkenemyCount1
    global vel_ini1
    global enemyCount1
    global falinhas
    global walkCount
    global atkCount

    tela.blit(bg1, (bgX, bgY))


    #SCORE
    texto("Score: " + str(score), (0, 0, 0), 25, 650, 20)

    pygame.draw.rect(tela, black, [38, 10, 204, 24])
    pygame.draw.rect(tela, red, [40, 12, 200, 20])
    pygame.draw.rect(tela, green, [40, 12, hp, 20])
    tela.blit(icon, (20, 10))


    # Mestra
    if pos_x < 280:
        tela.blit(lagerthaE, (500 + bgX, 260))
    else:
        tela.blit(lagerthaD, (500 + bgX, 260))

    tela.blit(falas[falinhas], (falax + bgX, falay))
    #########################################

    if enemy1hp <= 0:
        tela.blit(ini1morto, (inimigoX1 + 10, inimigoY1 + 150))

    #########################################

    if walkCount + 1 >= 25:
        walkCount = 1

    elif walkCount - 1 <= 0:
        walkCount = 24

    if atkCount + 1 >= 12:
        atkCount = 0

    #######################################################
    # tela.blit(inimigoA[enemyCount], (inimigoX, inimigoY))

    if esquerda:
        tela.blit(pDireita[walkCount], (pos_x, pos_y))
        walkCount -= 1
        atkCount = 0

    elif direita:
        tela.blit(pDireita[walkCount], (pos_x, pos_y))
        walkCount += 1
        atkCount = 0

    elif ataque:
        tela.blit(atacando[atkCount], (pos_x, pos_y))
        atkCount += 1

    else:
        tela.blit(playerD, (pos_x, pos_y))
        walkCount = 0
        atkCount = 0

    ####################  COLISAO  #######################################
    # tela.blit(icon, (colisaoPlayer, 320))

    ####################  INIMIGO  #######################################
    if enemy1hp >= 1:
        # tela.blit(icon, (colisaoEnemy1, 320))
        pygame.draw.rect(tela, black, [colisaoEnemy1 + 28, inimigoY1 + 48, 104, 10])
        pygame.draw.rect(tela, red, [colisaoEnemy1 + 30, inimigoY1 + 50, 100, 5])
        pygame.draw.rect(tela, yellow, [colisaoEnemy1 + 30, inimigoY1 + 50, enemy1hp, 5])

        if ini1dir:
            tela.blit(inimigoA[enemyCount1], (inimigoX1 + bgX, inimigoY1))
            enemyCount1 -= 1
            vel_ini1 = -3

        elif ini1esq:
            tela.blit(inimigoA[enemyCount1], (inimigoX1 + bgX, inimigoY1))
            enemyCount1 += 1
            vel_ini1 = -5

        elif ini1atk:
            tela.blit(inimigoAtk[atkenemyCount1], (inimigoX1 + bgX, inimigoY1))
            atkenemyCount1 += 1
        else:
            enemyCount1 = 0
            tela.blit(inimigoA[enemyCount1], (inimigoX1 + bgX, inimigoY1))
            vel_ini1 = 0

    pygame.display.update()
def fase2():
    global colisaoPlayer
    global falinhas
    global walkCount
    global atkCount
    global colisaoEnemy1
    global atkenemyCount1
    global vel_ini1
    global enemyCount1
    global colisaoEnemy2
    global atkenemyCount2
    global vel_ini2
    global enemyCount2
    global colisaoEnemy3
    global atkenemyCount3
    global vel_ini3
    global enemyCount3

    tela.blit(bg2, (bgX, bgY))
    pygame.draw.rect(tela, black, [38, 10, 204, 24])
    pygame.draw.rect(tela, red, [40, 12, 200, 20])
    pygame.draw.rect(tela, green, [40, 12, hp, 20])
    tela.blit(icon, (20, 10))

    # Mestra
    # if pos_x < 280:
    #     tela.blit(lagerthaE, (500 + bgX, 260))
    # else:
    #     tela.blit(lagerthaD, (500 + bgX, 260))
    #
    # tela.blit(falas[falinhas], (falax + bgX, falay))
    #########################################

    if walkCount + 1 >= 25:
        walkCount = 1

    elif walkCount - 1 <= 0:
        walkCount = 24

    if atkCount + 1 >= 12:
        atkCount = 0

    #######################################################
    # tela.blit(inimigoA[enemyCount], (inimigoX, inimigoY))

    if esquerda:
        tela.blit(pDireita[walkCount], (pos_x, pos_y))
        walkCount -= 1
        atkCount = 0

    elif direita:
        tela.blit(pDireita[walkCount], (pos_x, pos_y))
        walkCount += 1
        atkCount = 0

    elif ataque:
        tela.blit(atacando[atkCount], (pos_x, pos_y))
        atkCount += 1

    else:
        tela.blit(playerD, (pos_x, pos_y))
        walkCount = 0
        atkCount = 0

    ####################  COLISAO  #######################################

    tela.blit(icon, (colisaoPlayer, pos_y + 30))
    print(pos_x)

    ####################  INIMIGO  #######################################
    if enemy1hp >= 1:
        tela.blit(icon, (colisaoEnemy1, 320))
        pygame.draw.rect(tela, black, [colisaoEnemy1 + 28, inimigoY1 + 48, 104, 10])
        pygame.draw.rect(tela, red, [colisaoEnemy1 + 30, inimigoY1 + 50, 100, 5])
        pygame.draw.rect(tela, yellow, [colisaoEnemy1 + 30, inimigoY1 + 50, enemy1hp, 5])

        if ini1dir:
            tela.blit(inimigoA[enemyCount1], (inimigoX1 + bgX, inimigoY1))
            enemyCount1 -= 1
            vel_ini1 = 5

        elif ini1esq:
            tela.blit(inimigoA[enemyCount1], (inimigoX1 + bgX, inimigoY1))
            enemyCount1 += 1
            vel_ini1 = -5

        elif ini1atk:
            tela.blit(inimigoAtk[atkenemyCount1], (inimigoX1 + bgX, inimigoY1))
            atkenemyCount1 += 1
        else:
            enemyCount1 = 0
            tela.blit(inimigoA[enemyCount1], (inimigoX1 + bgX, inimigoY1))
            vel_ini1 = 0

    if enemy2hp >= 1:
        tela.blit(icon, (colisaoEnemy2, 400))
        pygame.draw.rect(tela, black, [colisaoEnemy2 + 28, inimigoY2 + 48, 104, 10])
        pygame.draw.rect(tela, red, [colisaoEnemy2 + 30, inimigoY2 + 50, 100, 5])
        pygame.draw.rect(tela, yellow, [colisaoEnemy2 + 30, inimigoY2 + 50, enemy2hp, 5])

        if ini2dir:
            tela.blit(inimigoA[enemyCount2], (inimigoX2 + bgX, inimigoY2))
            enemyCount2 -= 1
            vel_ini2 = 5

        elif ini1esq:
            tela.blit(inimigoA[enemyCount2], (inimigoX2 + bgX, inimigoY2))
            enemyCount2 += 1
            vel_ini2 = -5

        elif ini2atk:
            tela.blit(inimigoAtk[atkenemyCount2], (inimigoX2 + bgX, inimigoY2))
            atkenemyCount2 += 1
        else:
            enemyCount2 = 0
            tela.blit(inimigoA[enemyCount2], (inimigoX2 + bgX, inimigoY2))
            vel_ini2 = 0

    if enemy3hp >= 1:
        tela.blit(icon, (colisaoEnemy3, 320))
        pygame.draw.rect(tela, black, [colisaoEnemy3 + 28, inimigoY3 + 48, 104, 10])
        pygame.draw.rect(tela, red, [colisaoEnemy3 + 30, inimigoY3 + 50, 100, 5])
        pygame.draw.rect(tela, yellow, [colisaoEnemy3 + 30, inimigoY3 + 50, enemy3hp, 5])

        if ini1dir:
            tela.blit(inimigoA[enemyCount3], (inimigoX3 + bgX, inimigoY3))
            enemyCount3 -= 1
            vel_ini3 = 5

        elif ini1esq:
            tela.blit(inimigoA[enemyCount3], (inimigoX3 + bgX, inimigoY3))
            enemyCount3 += 1
            vel_ini3 = -5

        elif ini1atk:
            tela.blit(inimigoAtk[atkenemyCount3], (inimigoX3 + bgX, inimigoY3))
            atkenemyCount3 += 1
        else:
            enemyCount3 = 0
            tela.blit(inimigoA[enemyCount3], (inimigoX3 + bgX, inimigoY3))
            vel_ini3 = 0


    pygame.display.update()
def menu():
    tela.blit(bgMenu, (0, 0))
    tela.blit(name, (125, 10))
    # texto("VALHALLA CAN WAIT",white, 70, 170, 100)
    # texto("Skajdmö", white, 60, 300, 180)

    # pygame.draw.rect(tela, green, [50, 420, 120, 40])
    # texto("JOGAR", white, 25, 360, 280)
    # pygame.draw.rect(tela, green, [50, 500, 120, 40])

    tela.blit(jogar, (50, 420))
    tela.blit(sair, (50, 500))

    # texto("SAIR", white, 25, 370, 380)

    pygame.display.update()

def gamerOverr():
    tela.blit(gameOVer, (0, 0))

    pygame.display.update()

def demofim():
    tela.blit(Demofim, (0, 0))
    texto("Score: " + str(newScore), (255, 255, 255), 80, 250, 300)
    pygame.display.update()

# Loop do Jogo
gameover = False
menuzin = True
textinho = False
f1 = False
f2 = False
jogo = True
jogavel = False
enemy1 = True
enemy2 = True
enemy3 = True
dano = False
endDemo = False


cont = 0

#Musica do Menu
pygame.mixer.music.load("data/menutest.mp3")
pygame.mixer.music.play(-1)
#
abertura()

while jogo:
    if hp <= 0:
        pygame.mixer.music.stop()
        menuzin = False
        gamerOverr()
        for event in pygame.event.get():  # Para cada evento que ocorrer será printado na tela
            if event.type == pygame.QUIT:
                jogo = False
                menuzin = False
                f1 = False
                f2 = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # Se clicar na tela, guardar posições x e y do clique
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                # Se clicar em JOGAR, inicia cinematic

                if 260 < x < 525 and 420 < y < 470:  # Localização exata do botão JOGAR DE NOVO
                    pygame.mixer.music.fadeout(2500)  # FADE OUT Musica
                    for p in range(255, 0, -1):  # FADE OUT GAMEOVER
                        tela.fill(black)
                        gameOVer.set_alpha(p)
                        tela.blit(gameOVer, rectgameover)
                        pygame.time.delay(10)
                        pygame.display.flip()
                    pygame.mixer.music.load("data/mm.mp3")  # Troca a musica
                    pygame.mixer.music.play(-1)  # Play musica
                    hp = 200

                    for i in range(255):  # FADE IN TEXTINHO
                        tela.fill(black)
                        textin.set_alpha(i)
                        tela.blit(textin, rectTexto)
                        pygame.time.delay(10)
                        pygame.display.flip()
                    # tela.blit(icon, (300, 300))
                    menuzin = False
                    textinho = True

                # Se clicar em SAIR, jogo fecha

                elif 328 < x < 470 and 502 < y < 580:  # Localização exata do botão SAIR
                    for p in range(255, 0, -1):  # FADEOUT GAMEOVER
                        tela.fill(black)
                        gameOVer.set_alpha(p)
                        tela.blit(gameOVer, rectgameover)
                        # pygame.time.delay(2)
                        pygame.display.flip()
                    jogo = False
                    menuzin = False
                    f1 = False
                    f2 = False


            pygame.display.update()

    while menuzin:
    #MENU
        menu()
        for event in pygame.event.get():  # Para cada evento que ocorrer será printado na tela
            if event.type == pygame.QUIT:
                jogo = False
                menuzin = False
                f1 = False
                f2 = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # Se clicar na tela, guardar posições x e y do clique
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                # Se clicar em JOGAR, inicia cinematic

                if 50 < x < 170 and 420 < y < 479:  # Localização exata do botão JOGAR
                    pygame.mixer.music.fadeout(2500)  # FADE OUT Musica
                    for p in range(255, 0, -1):  # FADE OUT MENU
                        tela.fill(black)
                        bgMenu.set_alpha(p)
                        tela.blit(bgMenu, rectMenu)
                        pygame.time.delay(10)
                        pygame.display.flip()
                    pygame.mixer.music.load("data/mm.mp3")  # Troca a musica
                    pygame.mixer.music.play(-1)  # Play musica

                    for i in range(255):  # FADE IN TEXTINHO
                        tela.fill(black)
                        textin.set_alpha(i)
                        tela.blit(textin, rectTexto)
                        pygame.time.delay(10)
                        pygame.display.flip()
                    # tela.blit(icon, (300, 300))
                    menuzin = False
                    textinho = True

                # Se clicar em SAIR, jogo fecha

                elif 50 < x < 170 and 500 < y < 559:  # Localização exata do botão SAIR
                    for p in range(255, 0, -1):  # FADEOUT MENU
                        tela.fill(black)
                        bgMenu.set_alpha(p)
                        tela.blit(bgMenu, rectMenu)
                        # pygame.time.delay(2)
                        pygame.display.flip()
                    menuzin = False
                    f1 = False
                    f2 = False
                    jogo = False

            pygame.display.update()


    #CINEMATIC
    while textinho:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
                textinho = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:# Se clicar na tela, começa fase 1
                    pygame.mixer.music.fadeout(2700)  # FADE OUT Musica
                    for i in range(255, 0, -1):  # FADE OUT TEXTINHO
                         tela.fill(black)
                         textin.set_alpha(i)
                         tela.blit(textin, rectTexto)
                         #pygame.time.delay(100)
                         pygame.display.flip()
                    pygame.mixer_music.load("data/tutorial2.mp3")  # Troca musica
                    textinho = False
                    pygame.mixer.music.play(-1)  # Toca musica
                    f1 = True

    pygame.display.update()

    # FASE 1
    while f1:
        if endDemo:
            demofim()
            f1 = False
            f2 = False
            menuzin = False
            gameOVer = False
        if hp <= 0:
            f1 = False
        print(pos_x)
        print(inimigoX1)



        relogio.tick(30)  # Controla o FPS
        colisaoPlayer = pos_x + 120
        colisaoEnemy1 = inimigoX1 + 50 + bgX
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
                f1 = False
                f2 = False

            # Falinhas mestra
            if falinhas >= 1 and falinhas < 7:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                    # if event.key == pygame.K_z:
                    falinhas += 1
                jogavel = False

            elif falinhas == 8:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                    # if event.key == pygame.K_z:
                    endDemo = True
                    f1 = False
                    f2 = False
                jogavel = False
            else:
                jogavel = True
                enemy1 = True

        if enemy1hp <= 0:
            jogavel = False
            ataque = False
            falinhas = 8

        # Movimentação do Player - Setas do teclado
        if jogavel:

            teclas = pygame.key.get_pressed()
            if ataque == False and teclas[pygame.K_LEFT] and pos_x > vel + bgX:
                pos_x -= vel
                esquerda = True
                direita = False
                bgX += 1
                ataque = False

            elif ataque == False and teclas[pygame.K_RIGHT] and pos_x < tLargura - larPlayer:
                pos_x += vel
                esquerda = False
                direita = True
                bgX -= 1
                ataque = False
                if enemy1hp >= 1:
                    if pos_x + 50 >= colisaoEnemy1:
                        direita = False
                        pos_x = colisaoEnemy1 - 20
                        bgX += 2

            elif ataque == False and teclas[pygame.K_UP] and pos_y > 280:
                pos_y -= vel
                esquerda = False
                direita = True
                ataque = False

            elif ataque == False and teclas[pygame.K_DOWN] and pos_y < 305:
                pos_y += vel
                esquerda = False
                direita = True
                ataque = False

            elif ataque == False and teclas[pygame.K_z]:
                atkSom.play()
                esquerda = False
                direita = False
                ataque = True

            else:
                direita = False
                esquerda = False
                walkCount = 0

            if atkCount == 11:
                ataque = False
                walkCount = 0



###############    #INIMIGO 1    ###############

            if enemy1:
                inimigoX1 += vel_ini1

                if ini1atk == False and inimigoX1 >= pos_x + 120:
                    timer = 30 # 1 segundo
                    # print(cont)
                    ini1esq = True
                    ini1dir = False
                else:
                    print(timer)
                    ini1esq = False
                    timer -= 1
                    if timer <= 0:
                        ini1atk = True
                        timer = 60


                # elif ini1atk == False and inimigoX1 <= 300:
                #     ini1esq = False
                #     ini1dir = True

                # elif cont == 2:
                #     ini1esq = False
                #     ini1dir = False
                #     cont += 1
                # elif cont == 3:
                #     ini1atk = False

                if atkenemyCount1 + 1 >= 17:
                    ini1atk = False
                    atkenemyCount1 = 1

                if enemyCount1 >= 16:
                    enemyCount1 = 2
                if enemyCount1 <= 1:
                    enemyCount1 = 15

            ####TRETAS###


            if ataque and colisaoPlayer >= colisaoEnemy1 + 40:
                enemy1hp -= 5
                inimigoX1 += 20

                # Se o player não sofrer nenhum dano, a cada ataque ao inimigo, o score aumenta 15
                if hp == 200:
                    score += 15
                # Se o player sofrer dano, a cada ataque ao inimigo, o score aumenta somente 5
                elif hp < 200:
                    score += 5

            if ini1atk and colisaoPlayer >= colisaoEnemy1:
                hp -= 10
                pos_x -= 50


        fase1()



    while endDemo:
        newScore = score
        demofim()
        for event in pygame.event.get():  # Para cada evento que ocorrer será printado na tela
            if event.type == pygame.QUIT:
                jogo = False
                endDemo = False

    # FASE 2
    while f2:
        jogavel = True
        relogio.tick(30)  # Controla o FPS
        colisaoPlayer = pos_x + 120
        colisaoEnemy1 = inimigoX1 + 50 + bgX
        colisaoEnemy2 = inimigoX2 + 50 + bgX
        colisaoEnemy3 = inimigoX3 + 50 + bgX
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
                f1 = False
                f2 = False

            # # Falinhas mestra
            # if falinhas >= 1 and falinhas < 7:
            #     if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            #         # if event.key == pygame.K_z:
            #         falinhas += 1
            # else:
            #     jogavel = True
            #     enemy1 = True

        # Movimentação do Player - Setas do teclado
        if jogavel:

            teclas = pygame.key.get_pressed()
            if ataque == False and teclas[pygame.K_LEFT] and pos_x > vel + bgX:
                pos_x -= vel
                esquerda = True
                direita = False
                bgX += vel
                ataque = False

            elif ataque == False and teclas[pygame.K_RIGHT] and pos_x < tLargura - larPlayer:
                pos_x += vel
                esquerda = False
                direita = True
                bgX -= vel
                ataque = False
                if enemy3hp >= 1:
                    if pos_x + 50 >= colisaoEnemy3:
                        direita = False
                        pos_x = colisaoEnemy3 - 20
                        bgX += 5
                if enemy2hp >= 1:
                    if pos_x + 50 >= colisaoEnemy2:
                        direita = False
                        pos_x = colisaoEnemy2 - 20
                        bgX += 5
                if enemy1hp >= 1:
                    if pos_x + 50 >= colisaoEnemy1:
                        direita = False
                        pos_x = colisaoEnemy1 - 20
                        bgX += 5

            elif ataque == False and teclas[pygame.K_UP] and pos_y > 280:
                pos_y -= vel
                esquerda = False
                direita = True
                ataque = False

            elif ataque == False and teclas[pygame.K_DOWN] and pos_y < 370:
                pos_y += vel
                esquerda = False
                direita = True
                ataque = False

            elif ataque == False and teclas[pygame.K_z]:
                atkSom.play()
                esquerda = False
                direita = False
                ataque = True
                if atkCount == 8:
                    dano = True

            else:
                direita = False
                esquerda = False
                walkCount = 0

            if atkCount == 11:
                ataque = False
                walkCount = 0

            elif teclas[pygame.K_SPACE]:
                f2 = True
                f1 = False
                jogo = False

            ###############     INIMIGO 1    ###############

            if enemy1:
                inimigoX1 += vel_ini1

                if ini1atk == False and inimigoX1 >= 750:
                    cont += 1
                    ini1esq = True
                    ini1dir = False

                elif ini1atk == False and inimigoX1 <= 600:
                    ini1esq = False
                    ini1dir = True
                elif cont == 2:
                    ini1esq = False
                    ini1dir = False
                    cont += 1
                elif cont == 3:
                    ini1atk = False

                if atkenemyCount1 + 1 >= 17:
                    ini1atk = False
                    atkenemyCount1 = 1

                if enemyCount1 >= 16:
                    enemyCount1 = 2
                if enemyCount1 <= 1:
                    enemyCount1 = 15

            ###############     INIMIGO 2    ###############

            if enemy2:
                inimigoX2 += vel_ini2

                if ini2atk == False and inimigoX2 >= 500:
                    cont += 1
                    ini2esq = True
                    ini2dir = False

                elif ini2atk == False and inimigoX2 <= 400:
                    ini2esq = False
                    ini2dir = True
                elif cont == 2:
                    ini2esq = False
                    ini2dir = False
                    cont += 1
                elif cont == 3:
                    ini2atk = False

                if atkenemyCount2 + 1 >= 17:
                    ini2atk = False
                    atkenemyCount2 = 1

                if enemyCount2 >= 16:
                    enemyCount2 = 2
                if enemyCount2 <= 1:
                    enemyCount2 = 15

            ###############     INIMIGO 3    ###############
            if enemy3:
                inimigoX3 += vel_ini3

                if ini3atk == False and inimigoX3 >= 500:
                    cont += 1
                    ini3esq = True
                    ini3dir = False

                elif ini3atk == False and inimigoX3 <= 400:
                    ini3esq = False
                    ini3dir = True
                elif cont == 2:
                    ini3esq = False
                    ini3dir = False
                    cont += 1
                elif cont == 3:
                    ini3atk = False

                if atkenemyCount3 + 1 >= 17:
                    ini3atk = False
                    atkenemyCount3 = 1

                if enemyCount3 >= 16:
                    enemyCount3 = 2
                if enemyCount3 <= 1:
                    enemyCount3 = 15

            ####TRETAS###

            if ataque and colisaoPlayer >= colisaoEnemy1 + 40:
                enemy1hp -= 5
                inimigoX1 += 20
            if ataque and colisaoPlayer >= colisaoEnemy2 + 40:
                enemy2hp -= 5
                inimigoX2 += 20
            if ataque and colisaoPlayer >= colisaoEnemy3 + 40:
                enemy3hp -= 5
                inimigoX3 += 20

            if ini1atk and colisaoPlayer >= colisaoEnemy1:
                hp -= 10
                pos_x -= 50
            if ini2atk and colisaoPlayer >= colisaoEnemy2:
                hp -= 10
                pos_x -= 50
            if ini3atk and colisaoPlayer >= colisaoEnemy3:
                hp -= 10
                pos_x -= 50


        fase2()

pygame.quit()  # Fecha o pygame
