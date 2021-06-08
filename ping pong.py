import pygame, sys, time, random
from pygame.event import get

pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((800, 400))
fps = pygame.time.Clock()
GREEN = (0, 200, 0 )
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)




def juego():
    #coordenadas y velocidad jugador 1 
    j1_cordx = 50
    j1_cordy = 150
    j1speed_Y = 0
    # coordenadas y velocidad jugador 2 
    j2_cordx = 730
    j2_cordy = 150
    j2speed_Y = 0
    #coordendas pelota 
    pel_cordX = 360
    pel_cordy = 200
    speedpelotax = 5
    speedpelotay = 5 
    #pygame.mixer.music.load("musica.mp3")
    #pygame.mixer.music.play()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                #jugador1
                if event.key == pygame.K_w:
                    j1speed_Y = -4
                if event.key == pygame.K_s:
                    j1speed_Y = 4
                if event.key == pygame.K_UP:
                    j2speed_Y = -4
                if event.key == pygame.K_DOWN:
                    j2speed_Y = 4
            #dejo de apretar la tecla        
            if event.type == pygame.KEYUP:
                #jugador1
                if event.key == pygame.K_w:
                    j1speed_Y = 0
                if event.key == pygame.K_s:
                    j1speed_Y = 0
                if event.key == pygame.K_UP:
                    j2speed_Y = 0
                if event.key == pygame.K_DOWN:
                    j2speed_Y = 0
        # ------mueve el jugador-------
        j1_cordy += j1speed_Y
        j2_cordy += j2speed_Y 
        #--------------------------------

        #--------limites del jugador ---------
        if j1_cordy > 340 :
            j1_cordy = 340
        if j1_cordy < 0:
            j1_cordy = 0 
        if j2_cordy > 340:
            j2_cordy = 340
        if j2_cordy < 0:
            j2_cordy = 0
        #------------------------------

        #------movimiento de pelota-------
        pel_cordX += speedpelotax
        pel_cordy += speedpelotay
        if pel_cordy > 390 or pel_cordy < 5 :
            speedpelotay *= -1
        if pel_cordX > 780 or pel_cordX < 0 :
            pel_cordX = 360
            pel_cordy = 200
            speedpelotax *= -1
            speedpelotay *= -1
        #--------------------------        
        ## color de pantalla    
        pantalla.fill(BLACK)
        
        ##----Zona de dibujo -------
        jugador1 = pygame.draw.rect(pantalla,WHITE,(j1_cordx,j1_cordy, 10,60))
        jugador2 = pygame.draw.rect(pantalla,WHITE,(j2_cordx,j2_cordy, 10,60))
        pelota = pygame.draw.circle(pantalla,WHITE,(pel_cordX,pel_cordy),13 )


        #----Zona de dibujo -------

        # cuando los jugadores toquen la pelota
        if pelota.colliderect(jugador1):
            speedpelotax *= -1
            speedpelotay *=1
        if pelota.colliderect(jugador2):
            speedpelotax *=-1
            speedpelotay *=1

        ##Actualizar pantalla
        pygame.display.flip()
        fps.tick(60)

juego()
pygame.QUIT()