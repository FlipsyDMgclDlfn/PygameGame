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

playerImgL = pygame.image.load('pc_fl.png')
playerImgR = pygame.image.load('pc_fr.png')
playerImgWL1 = pygame.image.load('pc_wl1.png')
playerImgWL2 = pygame.image.load('pc_wl2.png')
playerImgWL3 = pygame.image.load('pc_wl3.png')
playerImgWL4 = pygame.image.load('pc_wl4.png')
playerImgWL5 = pygame.image.load('pc_wl5.png')
playerImgWL6 = pygame.image.load('pc_wl6.png')
playerImgWR1 = pygame.image.load('pc_wr1.png')
playerImgWR2 = pygame.image.load('pc_wr2.png')
playerImgWR3 = pygame.image.load('pc_wr3.png')
playerImgWR4 = pygame.image.load('pc_wr4.png')
playerImgWR5 = pygame.image.load('pc_wr5.png')
playerImgWR6 = pygame.image.load('pc_wr6.png')

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

class Enemy:
    def __init__(self,l,s):
        self.side = s
        if s == 0:
            self.move = 2
            self.image = pygame.image.load('pc_fr.png')
        else:
            self.move = -2
            self.image = pygame.image.load('pc_fl.png')
        self.health = 10 * l
        self.x = s*display_width
    def draw(self):
        self.x += self.move
        if self.health > 0:
            gameDisplay.blit(self.image,(self.x-8,368))
            
def player(x,y,s):
    gameDisplay.blit(s,(x,y))
    
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def suf(x,d):
    for i in range(0,5):
        if x >= 1000:
            x = x/1000
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
    return(str(round(x,d)) + suf)

def button(name, x, number, cost):
    
    smallText = pygame.font.Font("freesansbold.ttf",15)
    textSurf, textRect = text_objects(name, smallText,black)
    textRect.center = ( (x+(100/2)), (500+(100/4)) )
    gameDisplay.blit(textSurf, textRect)
    smallText = pygame.font.Font("freesansbold.ttf",15)
    textSurf, textRect = text_objects(suf(number,0), smallText,black)
    textRect.center = ( (x+(100/2)), (500+(2*100/4)) )
    gameDisplay.blit(textSurf, textRect)
    smallText = pygame.font.Font("freesansbold.ttf",10)
    textSurf, textRect = text_objects(("cost: "+suf(cost,1)), smallText,black)
    textRect.center = ( (x+(100/2)), (500+(3*100/4)) )
    gameDisplay.blit(textSurf, textRect)

def game_loop():

    gameExit = False
    ticks = 0
    level = 1
    
    playerX = 100
    playerY = 368
    playerS = playerImgR
    dx = 0
    inAir = False
    rise = False
    playerH = 0
    maxH = 0
    
    walking = False
    walkingL = 0
    walkingR = 0
    
    power = 0
    powerInc = 1
    powerPS = 0
    health = 75
    maxHealth = 100
    gold = 100000

    enemies = []
    
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
        pygame.event.pump()
        gameDisplay.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not inAir:
                        maxH = 100
                        inAir = True
                        playerH = 0
                        rise = True
                        
                if event.key == pygame.K_a:
                    dx = -2
                    walkingL = 1
                    
                if event.key == pygame.K_d:
                    dx = 2
                    walkingR = 1
                    
            elif event.type == pygame.KEYUP:
                dx = 0
                if event.key == pygame.K_a:
                    playerS = playerImgL
                    walking = False
                    walkingL = 0
                if event.key == pygame.K_d:
                    playerS = playerImgR
                    walking = False
                    walkingR = 0
        if playerX < 2 and pygame.key.get_pressed()[pygame.K_a]:
            playerX = 0
        elif playerX > display_width - 34 and pygame.key.get_pressed()[pygame.K_d]:
            playerX = display_width - 32
        else:
            playerX += dx
        if walkingR < 2 and walkingR >= 1:
            playerS = playerImgWR1
            walkingR+=.2
        elif walkingR < 3 and walkingR >= 1:
            playerS = playerImgWR2
            walkingR+=.2
        elif walkingR < 4 and walkingR >= 1:
            playerS = playerImgWR3
            walkingR+=.2
        elif walkingR < 5 and walkingR >= 1:
            playerS = playerImgWR4
            walkingR+=.2
        elif walkingR < 6 and walkingR >= 1:
            playerS = playerImgWR5
            walkingR+=.2 
        elif walkingR < 7 and walkingR >= 1:
            walkingR = 1
            playerS = playerImgWR6   
        if walkingL < 2 and walkingL >= 1:
            playerS = playerImgWL1
            walkingL+=.2
        elif walkingL < 3 and walkingL >= 1:
            playerS = playerImgWL2
            walkingL+=.2
        elif walkingL < 4 and walkingL >= 1:
            playerS = playerImgWL3
            walkingL+=.2
        elif walkingL < 5 and walkingL >= 1:
            playerS = playerImgWL4
            walkingL+=.2
        elif walkingL < 6 and walkingL >= 1:
            playerS = playerImgWL5
            walkingL+=.2
        elif walkingL < 7 and walkingL >= 1:
            walkingL = 1
            playerS = playerImgWL6
            
        if playerH < maxH and rise == True:
            playerY -= 2
            playerH += 2
        elif playerH == maxH:
            rise = False
            playerY += 2
            playerH -= 2
        elif playerH > 0:
            playerY += 2
            playerH -= 2
        else:
            inAir = False
            
        player(playerX,playerY,playerS)
            
        ##other screen stuff
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
    ##Stat Row
        pygame.draw.rect(gameDisplay, brown,(0,400,800,100))
        
        ##Health Bar
        pygame.draw.rect(gameDisplay, black,(25,430,204,40))
        pygame.draw.rect(gameDisplay, bright_red, (27,432,200*(health/maxHealth),36))
        smallText = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects("Health", smallText,black)
        textRect.center = (50,417)
        gameDisplay.blit(textSurf, textRect)
        smallText = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects((suf(health,0) + "/" + suf(maxHealth,0)), smallText,white)
        textRect.center = (129,450)
        gameDisplay.blit(textSurf, textRect)
        
        ##Power Counter
        smallText = pygame.font.Font("freesansbold.ttf",15)
        if power > 1000:
            c = 1
        else:
            c = 0
        textSurf, textRect = text_objects("Power: " + suf(power,c), smallText,black)
        textRect = (250,422)
        gameDisplay.blit(textSurf, textRect)
        
        ##PowerPS
        smallText = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects("Power Ps: " + suf(powerPS,1), smallText,black)
        textRect = (250,444)
        gameDisplay.blit(textSurf, textRect)
        
        ##Gold
        smallText = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects("Gold: " + str(gold), smallText,black)
        textRect = (250,466)
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
        textSurf, textRect = text_objects("+ " + suf(powerInc,0), smallText,black)
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
                    powerPS += 1
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
            if gold >= helper3C:
                pygame.draw.rect(gameDisplay, bright_green,(300,500,100,100))
                if click[0] == 1 and not down:
                    powerPS += 5
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
            if gold >= helper4C:
                pygame.draw.rect(gameDisplay, bright_green,(400,500,100,100))
                if click[0] == 1 and not down:
                    powerPS += 20
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
                    powerPS += 50
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
                    powerPS += 75
                    helper6 += 1
                    gold -= helper6C
                    helper6C +=500000
                    down = True
            else:
                pygame.draw.rect(gameDisplay, red,(600,500,100,100))
        button("Helper6",600,helper6,helper6C)

        ##Helper7
        if gold >= helper7C:
            pygame.draw.rect(gameDisplay, green,(700,500,100,100))
        else:
            pygame.draw.rect(gameDisplay, red,(700,500,100,100))
        if 700 + 100 > mouse[0] > 700 and 500+100 > mouse[1] > 500:
            if gold >= helper7C:
                pygame.draw.rect(gameDisplay, bright_green,(700,500,100,100))
                if click[0] == 1 and not down:
                    powerPS += 150
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

        if ticks%60 == 0:
            power += powerPS
        if (ticks+240)%480 == 0:
            enemies += [Enemy(1,0)]
        if ticks%480 == 0:
            enemies += [Enemy(1,1)]
        for enemy in enemies:
            enemy.draw()
        ticks += 1    
        pygame.display.update()
        clock.tick(60)

game_loop()
