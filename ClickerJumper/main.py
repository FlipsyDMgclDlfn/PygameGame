import pygame
import time
import random
import math

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
class Level:
    def __init__(self,l,p,pinc,pps,g,h1,h2,h3,h4,h5,h6,h7):
        
        gameExit = False
        ticks = 1
        level = l
        
        power = p
        powerInc = pinc
        powerPS = pps
        
        gold = g

        enemies = []
        spawnRate = 122 - (2 * level)
        kills = 0
        player = Player()
        
        helper = h1
        helperC = 10 + h1*5

        helper2 = h2
        helper2C = 100 + h2*50

        helper3 = h3
        helper3C = 1000 + h3*500   

        helper4 = h4
        helper4C = 10000 + h4*5000

        helper5 = h5
        helper5C = 100000 + h5*50000

        helper6 = h6
        helper6C = 1000000 + h6*500000

        helper7 = h7
        helper7C = 10000000 + h7*5000000
        
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
                        if not player.inAir:
                            player.maxH = 100
                            player.inAir = True
                            player.playerH = 0
                            player.rise = True
                            
                    if event.key == pygame.K_a:
                        player.dx = -4
                        player.walkingL = 1
                        
                    if event.key == pygame.K_d:
                        player.dx = 4
                        player.walkingR = 1
                        
                elif event.type == pygame.KEYUP:
                    player.dx = 0
                    if event.key == pygame.K_a:
                        player.playerS = playerImgL
                        player.walking = False
                        player.walkingL = 0
                    if event.key == pygame.K_d:
                        player.playerS = playerImgR
                        player.walking = False
                        player.walkingR = 0
                        
            if player.playerX < 2 and pygame.key.get_pressed()[pygame.K_a]:
                player.playerX = 0
            elif player.playerX > display_width - 34 and pygame.key.get_pressed()[pygame.K_d]:
                player.playerX = display_width - 32
            else:
                player.playerX += player.dx
            if player.walkingR < 2 and player.walkingR >= 1:
                player.playerS = playerImgWR1
                player.walkingR+=.2
            elif player.walkingR < 3 and player.walkingR >= 1:
                player.playerS = playerImgWR2
                player.walkingR+=.2
            elif player.walkingR < 4 and player.walkingR >= 1:
                player.playerS = playerImgWR3
                player.walkingR+=.2
            elif player.walkingR < 5 and player.walkingR >= 1:
                player.playerS = playerImgWR4
                player.walkingR+=.2
            elif player.walkingR < 6 and player.walkingR >= 1:
                player.playerS = playerImgWR5
                player.walkingR+=.2 
            elif player.walkingR < 7 and player.walkingR >= 1:
                player.walkingR = 1
                player.playerS = playerImgWR6
                
            if player.walkingL < 2 and player.walkingL >= 1:
                player.playerS = playerImgWL1
                player.walkingL+=.2
            elif player.walkingL < 3 and player.walkingL >= 1:
                player.playerS = playerImgWL2
                player.walkingL+=.2
            elif player.walkingL < 4 and player.walkingL >= 1:
                player.playerS = playerImgWL3
                player.walkingL+=.2
            elif player.walkingL < 5 and player.walkingL >= 1:
                player.playerS = playerImgWL4
                player.walkingL+=.2
            elif player.walkingL < 6 and player.walkingL >= 1:
                player.playerS = playerImgWL5
                player.walkingL+=.2
            elif player.walkingL < 7 and player.walkingL >= 1:
                player.walkingL = 1
                player.playerS = playerImgWL6
                
            if player.playerH < player.maxH and player.rise == True:
                player.playerY -= 2
                player.playerH += 2
            elif player.playerH == player.maxH:
                player.rise = False
                player.playerY += 2
                player.playerH -= 2
            elif player.playerH > 0:
                player.playerY += 2
                player.playerH -= 2
            else:
                player.inAir = False
                
            player.draw()
                
            ##other screen stuff
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
        ##Stat Row
            pygame.draw.rect(gameDisplay, brown,(0,400,800,100))
            
            ##Health Bar
            pygame.draw.rect(gameDisplay, black,(25,430,204,40))
            pygame.draw.rect(gameDisplay, bright_red, (27,432,200*(player.health/player.maxHealth),36))
            smallText = pygame.font.Font("freesansbold.ttf",15)
            textSurf, textRect = text_objects("Health", smallText,black)
            textRect.center = (50,417)
            gameDisplay.blit(textSurf, textRect)
            smallText = pygame.font.Font("freesansbold.ttf",15)
            textSurf, textRect = text_objects((suf(player.health,0) + "/" + suf(player.maxHealth,0)), smallText,white)
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

            #Kill Counter
            smallText = pygame.font.Font("freesansbold.ttf",15)
            textSurf, textRect = text_objects((str(10-kills)+" kills until level "+str(level+1)),smallText,black)
            textRect.center = (display_width/2,20)
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
                
            if (ticks+spawnRate)%(spawnRate*2) == 0:
                enemies += [Enemy(level,0)]
            if ticks%(spawnRate*2) == 0:
                enemies += [Enemy(level,1)]
            for enemy in enemies:
                enemy.draw(player)
            for enemy in enemies:
                if enemy.testForDead():
                    kills += 1
                    enemies.remove(enemy)
            for enemy in enemies:
                if enemy.testForHit(player) == True:
                    player.health -= 10 * level
                    
            if kills == 10:
                print("next level! " + str(level + 1))
                newLevel = Level(level + 1, power, powerInc, powerPS, gold, helper, helper2, helper3, helper4, helper5, helper6, helper7)

            player.health += 100 * (1 + math.log10(power)) - player.maxHealth
            player.maxHealth = 100 * (1 + math.log10(power))

            ticks += 1    
            pygame.display.update()
            clock.tick(60)

class Player:
    def __init__(self):
        self.playerX = 100
        self.playerY = 368
        self.playerS = playerImgR
        self.dx = 0
        self.inAir = False
        self.rise = False
        self.playerH = 0
        self.maxH = 0
        self.maxHealth = 100
        self.health = self.maxHealth
        self.walking = False
        self.walkingL = 0
        self.walkingR = 0
        
    def draw(self):
        gameDisplay.blit(self.playerS,(self.playerX,self.playerY))
    
        
class Enemy:
    def __init__(self,l,s):
        self.side = s
        self.move = 2
        if s == 0:
            self.image = pygame.image.load('pc_fr.png')
        else:
            self.image = pygame.image.load('pc_fl.png')
        self.health = 10 * l
        self.x = s*display_width
    def draw(self,player):
        if self.x > player.playerX:
            self.x -= self.move
        elif self.x < player.playerX:
            self.x += self.move
        gameDisplay.blit(self.image,(self.x-8,368))

    def testForHit(self, player):
        if self.x > player.playerX - 16 and self.x < player.playerX + 16 and player.playerY + 32 > 368:
            self.health = 0
            return True
        else: return False
            
    def testForDead(self):
        if self.health > 0: return False
        else: return True


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


start = Level(1,1,1,0,100000,0,0,0,0,0,0,0)
