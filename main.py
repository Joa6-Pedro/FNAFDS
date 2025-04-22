import pygame

pygame.init()
rodando = True

#screens
menu = True
carregando = False

screen = pygame.display.set_mode((800,600))

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #while menu:
    
    #while carregando:
