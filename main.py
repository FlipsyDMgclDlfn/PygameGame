import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255,1)
red = (200,0,0)
green = (0,200,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
brown = (204,153,51)

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(name, x, number, cost):
    for i in range(0,5):
        if cost >= 1000:
            cost = cost/1000
        else:
            break
    if i == 0:
        suf = ""
    elif i == 1:
        suf = " thousand"
    elif i == 2:
        suf = " million"
    elif i == 3:
        suf = " billion"
    elif i == 4:
        suf = " trillion"
    elif i == 5:
        suf = " quadrillion"
    else:
        cost = "NaN"
        suf = ""
    smallText = pygame.font.Font("freesansbold.ttf",15)
    textSurf, textRect = text_objects(name, smallText,black)
    textRect.center = ( (x+(100/2)), (500+(100/4)) )
    gameDisplay.blit(textSurf, textRect)
    smallText = pygame.font.Font("freesansbold.ttf",15)
    textSurf, textRect = text_objects(str(number), smallText,black)
    textRect.center = ( (x+(100/2)), (500+(2*100/4)) )
    gameDisplay.blit(textSurf, textRect)
    smallText = pygame.font.Font("freesansbold.ttf",10)
    textSurf, textRect = text_objects(("cost: "+str(cost)+suf), smallText,black)
    textRect.center = ( (x+(100/2)), (500+(3*100/4)) )
    gameDisplay.blit(textSurf, textRect)

def game_loop():

    gameExit = False
    ticks = 0
    
    power = 0
    powerInc = 1
    powerPS = 0
    health = 75
    maxHealth = 100
    gold = 100000

    helper = 0
    helperC = 10

    helper2 = 0
    helper2C = 100

    helper3 = 0
    helper3C = 1000    

    helper4 = 0
    helper4C = 10000

    helper5 = 0
    helper5C = 100000

    helper6 = 0
    helper6C = 1000000

    helper7 = 0
    helper7C = 10000000
    
    down = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        ##other screen stuff
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
    ##Stat Row
        pygame.draw.rect(gameDisplay, brown,(0,400,800,100))
        #Health Bar
        pygame.draw.rect(gameDisplay, black,(25,430,204,40))
        pygame.draw.rect(gameDisplay, bright_red, (27,432,200*(health/maxHealth),36))
        smallText = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects("Health", smallText,black)
        textRect.center = (50,417)
        gameDisplay.blit(textSurf, textRect)
        smallText = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects((str(health) + "/" + str(maxHealth)), smallText,white)
        textRect.center = (129,450)
        gameDisplay.blit(textSurf, textRect)        
    ##Bottom Row
        ##Clicker
        if 100 > mouse[0] > 0 and 500+100 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green,(0,500,100,100))
            if click[0] == 1 and not down:
                power += powerInc
                down = True
        else:
            pygame.draw.rect(gameDisplay, green,(0,500,100,100))
        smallText = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects(str(round(power)), smallText,black)
        textRect.center = ( (100/2), (500+(100/2)) )
        gameDisplay.blit(textSurf, textRect)

        ##Helper
        if gold >= helperC:
            pygame.draw.rect(gameDisplay, green,(100,500,100,100))
        else:
            pygame.draw.rect(gameDisplay, red,(100,500,100,100))
        if 100 + 100 > mouse[0] > 100 and 500+100 > mouse[1] > 500:
            if gold >= helperC:
                pygame.draw.rect(gameDisplay, bright_green,(100,500,100,100))
                if click[0] == 1 and not down:
                    powerPS += .1
                    helper += 1
                    gold -= helperC
                    helperC +=5
                    down = True
            else:
                pygame.draw.rect(gameDisplay, red,(100,500,100,100))
        button("Helper",100,helper,helperC)

        ##Helper2
        if gold >= helper2C:
            pygame.draw.rect(gameDisplay, green,(200,500,100,100))
        else:
            pygame.draw.rect(gameDisplay, red,(200,500,100,100))
        if 200 + 100 > mouse[0] > 200 and 500+100 > mouse[1] > 500:
            if gold >= helper2C:
                pygame.draw.rect(gameDisplay, bright_green,(200,500,100,100))
                if click[0] == 1 and not down:
                    powerPS += 5
                    helper2 += 1
                    gold -= helper2C
                    helper2C +=50
                    down = True
            else:
                pygame.draw.rect(gameDisplay, red,(200,500,100,100))
        button("Helper2",200,helper2,helper2C)

        ##Helper3
        if gold >= helper3C:
            pygame.draw.rect(gameDisplay, green,(300,500,100,100))
        else:
            pygame.draw.rect(gameDisplay, red,(300,500,100,100))
        if 300 + 100 > mouse[0] > 300 and 500+100 > mouse[1] > 500:
            if gold >= helper2C:
                pygame.draw.rect(gameDisplay, bright_green,(300,500,100,100))
                if click[0] == 1 and not down:
                    powerPS += 50
                    helper3 += 1
                    gold -= helper3C
                    helper3C +=500
                    down = True
            else:
                pygame.draw.rect(gameDisplay, red,(300,500,100,100))
        button("Helper3",300,helper3,helper3C)

        ##Helper4
        if gold >= helper4C:
            pygame.draw.rect(gameDisplay, green,(400,500,100,100))
        else:
            pygame.draw.rect(gameDisplay, red,(400,500,100,100))
        if 400 + 100 > mouse[0] > 400 and 500+100 > mouse[1] > 500:
            if gold >= helper2C:
                pygame.draw.rect(gameDisplay, bright_green,(400,500,100,100))
                if click[0] == 1 and not down:
                    powerPS += 500
                    helper4 += 1
                    gold -= helper4C
                    helper4C +=5000
                    down = True
            else:
                pygame.draw.rect(gameDisplay, red,(400,500,100,100))
        button("Helper4",400,helper4,helper4C)

        ##Helper5
        if gold >= helper5C:
            pygame.draw.rect(gameDisplay, green,(500,500,100,100))
        else:
            pygame.draw.rect(gameDisplay, red,(500,500,100,100))
        if 500 + 100 > mouse[0] > 500 and 500+100 > mouse[1] > 500:
            if gold >= helper5C:
                pygame.draw.rect(gameDisplay, bright_green,(500,500,100,100))
                if click[0] == 1 and not down:
                    powerPS += 5000
                    helper5 += 1
                    gold -= helper5C
                    helper5C +=50000
                    down = True
            else:
                pygame.draw.rect(gameDisplay, red,(500,500,100,100))
        button("Helper5",500,helper5,helper5C)

        ##Helper6
        if gold >= helper6C:
            pygame.draw.rect(gameDisplay, green,(600,500,100,100))
        else:
            pygame.draw.rect(gameDisplay, red,(600,500,100,100))
        if 600 + 100 > mouse[0] > 600 and 500+100 > mouse[1] > 500:
            if gold >= helper6C:
                pygame.draw.rect(gameDisplay, bright_green,(600,500,100,100))
                if click[0] == 1 and not down:
                    powerPS += 50000
                    helper6 += 1
                    gold -= helper6C
                    helper6C +=500000
                    down = True
            else:
                pygame.draw.rect(gameDisplay, red,(600,500,100,100))
        button("Helper6",600,helper6,helper6C)

        ##Helper67
        if gold >= helper7C:
            pygame.draw.rect(gameDisplay, green,(700,500,100,100))
        else:
            pygame.draw.rect(gameDisplay, red,(700,500,100,100))
        if 700 + 100 > mouse[0] > 700 and 500+100 > mouse[1] > 500:
            if gold >= helper7C:
                pygame.draw.rect(gameDisplay, bright_green,(700,500,100,100))
                if click[0] == 1 and not down:
                    powerPS += 500000
                    helper7 += 1
                    gold -= helper7C
                    helper7C +=5000000
                    down = True
            else:
                pygame.draw.rect(gameDisplay, red,(700,500,100,100))
        button("Helper7",700,helper7,helper7C)


        
        if click[0] == 0:
            down = False
        if click[0] == 1:
            down = True

        ticks += 1
        if ticks%60 == 0:
            power += powerPS
            
        pygame.display.update()
        clock.tick(60)

game_loop()
