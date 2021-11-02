import pygame
w, h = 800, 600
tela = pygame.display.set_mode((w, h))
black = (0, 0, 0)
logo = pygame.image.load("data/six.jpg")
logo_game = pygame.image.load("data/pglogo.png").convert()
bgMenu = pygame.image.load("data/menuzin.png").convert()

def abertura() :  # logos do grupo e do pygame
    rect = logo.get_rect()
    rect_game = logo_game.get_rect()
    rectMenu = bgMenu.get_rect()
    for i in range(255):  # FADE IN SIX
        tela.fill(black)
        logo.set_alpha(i)
        tela.blit(logo, rect)
        pygame.time.delay(5)
        pygame.display.flip()

    for f in range(255, 0, -1):  # FADE OUT SIX
        tela.fill(black)
        logo.set_alpha(f)
        tela.blit(logo, rect)
        pygame.time.delay(5)
        pygame.display.flip()

    for j in range(255):  # FADE IN PYGAME
        tela.fill(black)
        logo_game.set_alpha(j)
        tela.blit(logo_game, rect_game)
        pygame.time.delay(10)
        pygame.display.flip()

    for k in range(255, 0, -1):  # FADE OUT PYGAME
        tela.fill(black)
        logo_game.set_alpha(k)
        tela.blit(logo_game, rect_game)
        pygame.time.delay(10)
        pygame.display.flip()

    for i in range(255):  # FADE IN MENU
        tela.fill(black)
        bgMenu.set_alpha(i)
        tela.blit(bgMenu, rectMenu)
        pygame.time.delay(15)
        pygame.display.flip()



