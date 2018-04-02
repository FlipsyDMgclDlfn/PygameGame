import pygame
import time
import random
import math

pygame.init()

display_width = 800
display_height = 600

##Colors
black = (0,0,0)
white = (255,255,255,1)
red = (200,0,0)
green = (0,200,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
brown = (204,153,51)

##Game Constants
GRAVITY = 10
MAX_SPEED = 4
SLIDE_DISTANCE = .5

##Images (Not All Currently Used)
playerImgL = pygame.image.load('pc_fl.png')
playerImgR = pygame.image.load('pc_fr.png')
playerImgWL = [pygame.image.load('pc_wl1.png'),pygame.image.load('pc_wl2.png'),pygame.image.load('pc_wl3.png'),pygame.image.load('pc_wl4.png'),pygame.image.load('pc_wl5.png'),pygame.image.load('pc_wl6.png')]
playerImgWR = [pygame.image.load('pc_wr1.png'),pygame.image.load('pc_wr2.png'),pygame.image.load('pc_wr3.png'),pygame.image.load('pc_wr4.png'),pygame.image.load('pc_wr5.png'),pygame.image.load('pc_wr6.png')]
playerImgAPR = pygame.image.load('pc_mpr6.png')
playerImgAPL = pygame.image.load('pc_mpl6.png')
playerImgASR = pygame.image.load('pc_msnl6.png')
playerImgASL = pygame.image.load('pc_msnr6.png')
playerImgSR = pygame.image.load('pc_snr5.png')
playerImgSL = pygame.image.load('pc_snl5.png')
playerImgPR = pygame.image.load('pc_pr12.png')
playerImgPL = pygame.image.load('pc_pl12.png')
enr = pygame.image.load('en_r.png')
enl = pygame.image.load('en_l.png')

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

class Level:
    ##Level Num, Power, Power Per Click, Power PS, Gold, Num Of Each Helper
    def __init__(self,l,p,pinc,pps,g,h1,h2,h3,h4,h5,h6,h7):
        
        gameExit = False
        ticks = 1
        level = l
        
        power = p
        powerInc = pinc
        powerPS = pps
        gold = g

        bullets = [] ## Keeps track of each bullet
        enemies = [] ## Keeps track of each enemy
        spawnRate = 122 - (2 * level) ##Subject to change
        kills = 0
        
        ##Allows control customization and some tweaks would allow multiplayer
        player = Player(pygame.K_SPACE, pygame.K_a, pygame.K_d, pygame.K_LSHIFT)
        
        #Helper Stats (Costs subject to change)
        helper1 = h1
        helper1C = 10 + h1*5

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
        
        helpers = [Helper("Helper", helper1C, helper1, .1, 5, 100),Helper("Helper2", helper2C, helper2, 1, 50, 200),Helper("Helper3", helper3C, helper3, 10, 500, 300),Helper("Helper4", helper4C, helper4, 100, 5000, 400),Helper("Helper5", helper5C, helper5, 1000, 50000, 500),Helper("Helper6", helper6C, helper6, 10000, 500000, 600),Helper("Helper7", helper7C, helper7, 100000, 5000000, 700)]
        
        down = False
        
        ##Game Loop
        while not gameExit:
            pygame.event.pump()
            gameDisplay.fill(white)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    
                    if event.key == player.jump:
                        if not player.inAir:
                            player.dy = 5
                            player.inAir = True
                            
                    if event.key == player.left:
                        player.movingL = True
                        player.face = "Left"
                        player.walkingL = 1
                        
                    elif event.key == player.right:
                        player.movingR = True
                        player.face = "Right"
                        player.walkingR = 1
                        
                elif event.type == pygame.KEYUP:
                    
                    if event.key == player.left:
                        player.movingL = False
                        player.playerS = playerImgL
                        player.face = "Left"
                        player.walking = False
                        player.walkingL = 0
                        
                    if event.key == player.right:
                        player.movingR = False
                        player.playerS = playerImgR
                        player.face = "Right"
                        player.walking = False
                        player.walkingR = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == player.shoot:
                        bullets += [Bullet(player)]
                        
            ##Boarder Testing and Moving
            if player.movingR:
                if player.dx < MAX_SPEED:
                    player.dx += SLIDE_DISTANCE
            if player.movingL:
                if player.dx > (-1) * MAX_SPEED:
                    player.dx -= SLIDE_DISTANCE
            if not player.movingR and not player.movingL:
                if player.dx > 0:
                    player.dx -= SLIDE_DISTANCE
                elif player.dx < 0:
                    player.dx += SLIDE_DISTANCE
                    
            if player.playerX < 2 and pygame.key.get_pressed()[pygame.K_a]:
                player.playerX = 0
            elif player.playerX > display_width - 34 and pygame.key.get_pressed()[pygame.K_d]:
                player.playerX = display_width - 32
            else:
                player.playerX += player.dx
                
            ##Walk Right Cycle     
            if player.movingR:
                player.walkingR += .2
                if player.walkingR >= 7:
                    player.walkingR = 1
                player.playerS = playerImgWR[math.floor(player.walkingR)-1]
                
            ##Walk Left Cycle    
            if player.movingL:
                player.walkingL += .2
                if player.walkingL >= 7:
                    player.walkingL = 1
                player.playerS = playerImgWL[math.floor(player.walkingL)-1]
                
            ##Jump Cycle    
            player.playerY -= player.dy
            if player.playerY < 368:
                player.dy -= GRAVITY/60 ##Accelaration due to gravity per frame(change to affect gravity)
            if player.playerY > 368:
                player.playerY = 368
            if player.playerY == 368:
                player.inAir = False
                player.dy = 0
            
            player.draw()

            ##Getting Mouse Info
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

            ##Draws and does helper stuff
            for helper in helpers:
                if gold >= helper.helperC:
                    pygame.draw.rect(gameDisplay, green,(helper.x,500,100,100))
                else:
                    pygame.draw.rect(gameDisplay, red,(helper.x,500,100,100))
                if helper.x + 100 > mouse[0] > helper.x and 500+100 > mouse[1] > 500:
                    if gold >= helper.helperC:
                        pygame.draw.rect(gameDisplay, bright_green,(helper.x,500,100,100))
                        if click[0] == 1 and not down:
                            gold -= helper.helperC
                            powerPS += helper.pInc
                            helper.clicked()
                            down = True
                    else:
                        pygame.draw.rect(gameDisplay, red,(helper.x,500,100,100))
                button(helper.name,helper.x,helper.helper,helper.helperC)

            if click[0] == 0:
                down = False
            if click[0] == 1:
                down = True
                
            ##Adds PowerPS to Power every second
            if ticks%60 == 0:
                power += powerPS
                
        ##Bullet Stuff
                
            ##Draws Bullets
            for bullet in bullets:
                bullet.draw()

            ##Tests For Bullets Off Screen        
            for bullet in bullets:
                if bullet.testForOff == True:
                    bullets.remove(bullet)
                    
                
        ##Enemy stuff
                
            ##Spwans Enemies
            if (ticks+spawnRate)%(spawnRate*2) == 0:
                enemies += [Enemy(level,0)]
            if ticks%(spawnRate*2) == 0:
                enemies += [Enemy(level,1)]
                
            #Draws Enemies
            for enemy in enemies:
                enemy.draw(player)            
                    
            ##What Happens if Enemy Collides With Player
            for enemy in enemies:
                if enemy.testForHit(player) == True:
                    player.health -= 10 * level

            ##Tests For Dead Enemies
            for enemy in enemies:
                if enemy.testForDead():
                    kills += 1
                    gold += 10 * l
                    enemies.remove(enemy)

            ##What Happensif Enemy Collides With a Bullet
                for enemy in enemies:
                    for bullet in bullets:
                        if enemy.testForHitBullet(bullet,player) == True:
                            bullets.remove(bullet)
                    
            ##End Game Conditions
            if player.health <= 0:
                print("Try again!")
                newLevel = Level(level, power, powerInc, powerPS, gold, helpers[0].helper, helpers[1].helper, helpers[2].helper, helpers[3].helper, helpers[4].helper, helpers[5].helper, helpers[6].helper)
                
            ##Health Scales with Power (Numbers might change)
            player.health += 100 * (1 + math.log10(power)) - player.maxHealth
            player.maxHealth = 100 * (1 + math.log10(power))

            ##Level Up
            if kills >= 10:
                print("Next level! " + str(level + 1))
                newLevel = Level(level+1, power, powerInc, powerPS, gold, helpers[0].helper, helpers[1].helper, helpers[2].helper, helpers[3].helper, helpers[4].helper, helpers[5].helper, helpers[6].helper)
            
            
            ticks += 1    
            pygame.display.update()
            clock.tick(60)

##Classes

##Helper class
class Helper:
    ##Sets initail values
    def __init__(self, name, cost, count, pInc, cInc, x):
        self.name = name    ##Name
        self.helper = count ##Num of helpers
        self.helperC = cost ##Cost
        self.pInc = pInc    ##Power PS gained per helper
        self.cInc = cInc    ##Cost increase per helper
        self.x = x          ##X cord on screen
    ##If helper is clicked (Subject to change to expenential growth instread of linear)    
    def clicked(self):
        self.helper += 1
        self.helperC += self.cInc
        
            
##Player Class
class Player:
    def __init__(self, jump, left, right, shoot):
        self.jump = jump                ##Key to press to jump
        self.left = left                ##Key to press to move left
        self.right = right              ##Key to press to move right
        self.shoot = shoot              ##Key to press to shoot
        self.playerX = 100              ##X cord of player 
        self.playerY = 368              ##Y Cord of player
        self.width = 16                 ##Width of player
        self.height = 32                ##Height of player
        self.playerS = playerImgR       ##Sprite for the player
        self.dx = 0                     ##Change in X Cord for the player
        self.dy = 0                     ##Change in Y Cord for player
        self.inAir = False              ##Indicates in player is in the air or not
        self.maxHealth = 100            ##Max Health for the player
        self.health = self.maxHealth    ##Current Health for the player
        self.movingL = False            ##Indicates if the player is moving left
        self.movingR = False            ##Indicates if the player is moving right
        self.walking = False            ##Indicates if the player is walking or not
        self.walkingL = 0               ##Frame number for walking left
        self.walkingR = 0               ##Frame number for walking right
        self.face = "Right"             ##Direction facing

    ##Draws Player    
    def draw(self):
        gameDisplay.blit(self.playerS,(self.playerX,self.playerY))
    
##Enemy Class        
class Enemy:
    def __init__(self,l,s):
        self.side = s               ##Intitail side for player (-1 or 1)
        self.move = 2               ##Speed of enemy

        if s == 0:
            self.img = enr          ##Sprite for the enemy
        else:
            self.img = enl
            
        self.health = 10 * l        ##Health of the enemy
        self.x = s*display_width    ##X Cord of enemy
        self.y = 368                ##Y cord of enemy
        self.width = 16             ##Width of enemy

    #Draws Enemy and figures which way to move
    def draw(self,player):
        if self.x > player.playerX:
            self.x -= self.move
            self.img = enl
        elif self.x < player.playerX:
            self.x += self.move
            self.img = enr
        gameDisplay.blit(self.img,(self.x-8,self.y))
        
    ##Tests for Collision with Player
    def testForHit(self, player):
        if self.x > player.playerX - player.width and self.x < player.playerX + player.width and player.playerY + player.height > self.y:
            self.health = 0
            return True
        else: return False
        
    ##Tests for Collision with a Bullet
    def testForHitBullet(self, bullet, player):
        if self.x + self.width > bullet.x and self.x - self.width < bullet.x and bullet.y + 2 > self.y:
            self.health -= player.maxHealth/10
            return True
        else: return False
        
    ##Tests if this Enemy is dead        
    def testForDead(self):
        if self.health > 0: return False
        else: return True

##Bullet Class        
class Bullet:
    ##Initializes Bullet properties
    def __init__(self,player):
        self.d = player.face                            ##Direction of bullet
        self.y = player.playerY + 8                     ##Y Cord of bullet
        if self.d == "Right":
            self.x = player.playerX + player.width + 2  ##X Cord of bullet
            self.m = 8                                  ##Speed of bullet
        else:
            self.x = player.playerX - 2 -2
            self.m = - 8
    ##Draws the bullet
    def draw(self):
       pygame.draw.rect(gameDisplay, black,(self.x,self.y,2,2))
       self.x += self.m
    ##Tests for bullet off screen
    def testForOff(self):
        if self.x - 2 < 0 or self.x > display_width:
            return True
        return False
       
##Static Methods
       
##For Making Text
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Shortens Numbers (Can impliment more)
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

##Clicker Bar Buttons
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

##l = int(input("What Level Would You Like To Start At?"))
start = Level(1,1,1,0,0,0,0,0,0,0,0,0)
