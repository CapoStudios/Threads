import sys, os, math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

#My File
from player import Player
from enemy import Enemy
from hammer import Hammer
from lever import Lever
from star import Star
from util import drawChessBoard, resetElements, drawInfoTexts

pygame.init()

width, height = 900, 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Threads()")

#----------------------------------------------------------------------

#SETUP
clock = pygame.time.Clock()

#Font
font = pygame.font.Font('../assets/m5x7.ttf', 32)

#Player variables
player1 = Player(100, 50,  24, 24, (0, 29, 213), False)
player2 = Player(100, height-50, 25, 25, (255, 115, 4), True)

#Images
robot1 = pygame.transform.scale2x(pygame.image.load('../assets/robot1single.png'))
robot2 = pygame.transform.scale2x(pygame.image.load('../assets/robot2single.png'))
blockImg = pygame.image.load('../assets/block.png')
thronsImg = pygame.image.load('../assets/throns.png')
enemyImg = pygame.image.load('../assets/enemy.png')
leverImg = pygame.transform.scale2x(pygame.image.load('../assets/lever.png'))

#Lever
lever = Lever(0, 250)

#Star
star = Star(750, 150, 5)
starBorder = Star((star.getX())/5, ((star.getY())/5)-10, 4)

#Enemies
enemies = [
    Enemy(325, 400, True, 0.04),
    Enemy(475, 400, True, 0.04),
    Enemy(625, 400, True, 0.04),
    Enemy(775, 400, True, 0.04),
    Enemy(700, 300, True, 0.04),
    Enemy(550, 300, True, 0.04),
    Enemy(400, 300, True, 0.04),
    Enemy(250, 300, True, 0.04),
    Enemy(100, 300, True, 0.04),
]

#Elements
elements = [
    #UP
    (150, 225, 25, 25),
    (175, 200, 25, 25),
    (200, 175, 25, 25),
    (225, 150, 25, 25),
    (250, 125, 25, 25),
    (275, 100, 25, 25),
    (300, 75, 25, 25),
    (325, 50, 25, 25),
    (325, 0, 25, 25),
    (275, 0, 25, 25),
    (300, 0, 25, 25),
    (300, 225, 25, 25),
    (300, 200, 25, 25),
    (300, 175, 25, 25),
    (325, 150, 25, 25),
    (350, 125, 25, 25),
    (375, 75, 25, 25),
    (400, 50, 25, 25),
    (425, 25, 25, 25),
    (425, 0, 25, 25),
    (350, 0, 25, 25),
    (375, 0, 25, 25),
    (400, 0, 25, 25),
    (450, 225, 25, 25),
    (475, 200, 25, 25),
    (500, 175, 25, 25),
    (525, 150, 25, 25),
    (550, 125, 25, 25),
    (575, 100, 25, 25),
    (600, 75, 25, 25),
    (625, 50, 25, 25),
    (625, 0, 25, 25),
    (650, 0, 25, 25),
    (675, 0, 25, 25),
    (725, 0, 25, 25),
    (700, 0, 25, 25),
    (600, 0, 25, 25),
    (575, 0, 25, 25),
    (550, 0, 25, 25),
    (525, 0, 25, 25),
    (450, 0, 25, 25),
    (475, 0, 25, 25),
    (500, 0, 25, 25),

    #DOWN
    (-25, 400, 25, 25),
    (900, 300, 25, 25),
    (50,  375, 25, 25),
    (25,  375, 25, 25),
    (0,   375, 25, 25),
    (150, 375, 25, 25),
    (175, 375, 25, 25),
    (200, 375, 25, 25),
    (225, 375, 25, 25),
    (250, 375, 25, 25),
    (275, 375, 25, 25),
    (300, 375, 25, 25),
    (325, 375, 25, 25),
    (350, 375, 25, 25),
    (375, 375, 25, 25),
    (400, 375, 25, 25),
    (425, 375, 25, 25),
    (450, 375, 25, 25),
    (475, 375, 25, 25),
    (500, 375, 25, 25),
    (525, 375, 25, 25),
    (550, 375, 25, 25),
    (100, 375, 25, 25),
    (75,  375, 25,  25),
    (125, 375, 25, 25),
    (850, 400, 25, 25),
    (850, 375, 25, 25),
    (825, 375, 25, 25),
    (800, 375, 25, 25),
    (775, 375, 25, 25),
    (750, 375, 25, 25),
    (700, 375, 25, 25),
    (725, 375, 25, 25),
    (675, 375, 25, 25),
    (650, 375, 25, 25),
    (625, 375, 25, 25),
    (600, 375, 25, 25),
    (575, 375, 25, 25),
    (875, 275, 25, 25),
    (850, 275, 25, 25),
    (825, 275, 25, 25),
    (800, 275, 25, 25),
    (775, 275, 25, 25),
    (750, 275, 25, 25),
    (725, 275, 25, 25),
    (700, 275, 25, 25),
    (675, 275, 25, 25),
    (650, 275, 25, 25),
    (625, 275, 25, 25),
    (600, 275, 25, 25),
    (575, 275, 25, 25),
    (550, 275, 25, 25),
    (525, 275, 25, 25),
    (500, 275, 25, 25),
    (475, 275, 25, 25),
    (450, 275, 25, 25),
    (425, 275, 25, 25),
    (400, 275, 25, 25),
    (25,  275, 25, 25),
    (50,  275, 25, 25),
    (75,  275, 25, 25),
    (100, 275, 25, 25),
    (125, 275, 25, 25),
    (150, 275, 25, 25),
    (175, 275, 25, 25),
    (200, 275, 25, 25),
    (225, 275, 25, 25),
    (250, 275, 25, 25),
    (275, 275, 25, 25),
    (300, 275, 25, 25),
    (325, 275, 25, 25),
    (350, 275, 25, 25),
    (375, 275, 25, 25),
    (25,  300, 25, 25),
]

#Throns
throns = [
    (400,  25, 25, 25),
    (325, 125, 25, 25),
    (500, 175, 25, 25),
    (575, 100, 25, 25),
]

#GRID
CELL = 25

#Reset ALL
def resetAll():
    player1.setPos(100, 50)
    player2.setPos(100, height-50)
    player1.resetStar()
    #------------------------------
    player1.resetVel()
    player2.resetVel()
    #------------------------------
    lever.hasCollideWithPlayer = False
    resetElements(116)


#DRAW
def drawGame():
    #Clear Screen
    screen.fill((255, 255, 255))

    #ChessBoard
    drawChessBoard(screen, width, CELL)
    

    #Player 1
    player1.draw(screen, robot1, player1.getX(), player1.getY() - player1.getH()/3.6, (0, 0, 20, 30)) 

    #Thorns
    if lever.hasCollideWithPlayer == True:
        for s in throns:
            sp = pygame.Rect(s)
            screen.blit(pygame.transform.flip(thronsImg, False, False), (sp.x, sp.y), (0, 0, 25*2, 25*2))
        for t in range(30):
            if t == 9 or t==8:
                pass
            else:
                screen.blit(pygame.transform.flip(thronsImg, False, False), (175+(25*t), 225), (0, 0, 25*2, 25*2))

    #Elements(Blocks)
    for e in elements: 
        b = pygame.Rect(e)
        if lever.hasCollideWithPlayer == False:
            if elements.index(e) > 43:
                screen.blit(blockImg, (b.x, b.y), (0, 0, 50, 50))
        else:
            screen.blit(blockImg, (b.x, b.y), (0, 0, 50, 50))

    #Line
    pygame.draw.line(screen, (0,0,0), (0, height/2), (width, height/2))

    #Player 2
    player2.draw(screen, robot2, player2.getX()-5, player2.getY()+1, (0, 0, 30, 42))

    #Enemies
    for n in enemies:
        n.draw(screen, enemyImg)

    #Lever
    lever.draw(screen, leverImg)


    #Star & Border
    starBorder.draw(screen, (0,0,0), starBorder.createStarPoints())
    star.draw(screen, (230, 255, 80), star.createStarPoints())

    #Texts
    drawInfoTexts(screen, font, player1.level, player1.blocks)
    

    #Grid
    mouseX, mouseY = pygame.mouse.get_pos()
    if mouseY > height/2:
        #Draw Grid
        for i in range(int(width/(CELL))):
            if i==0: 
                color = (0,0,0) 
            else: 
                color = (128,128,128)

            pygame.draw.line(screen, color, (i*CELL, height/2), (i*CELL, height))
            pygame.draw.line(screen, color, (0, (i*CELL)+height/2), (width, (i*CELL)+height/2))

        #Draw Cell
        if player1.blocks > 0:
            screen.blit(blockImg, (CELL*(int(mouseX/CELL)), CELL*(int(mouseY/CELL))), (0, 0, 50, 50))


    #END
    if player1.getStar == True:
        if player1.endCircleRadius > 250:
            pygame.draw.circle(screen, (0, 0, 0), (width/2, height/2), int(player1.endCircleRadius*2.1), height)
            player1.endCircleRadius -= 5
        else:
            screen.fill((0, 0, 0))
            player1.level += 1



#UPDATE
def updateGame():
    #FPS
    clock.tick(60)

    #Gravity
    player1.gravity()
    player2.gravity()

    #Input Events
    for event in pygame.event.get():
        #Exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Keyboard Events
        if event.type == pygame.KEYDOWN:
            #Exit
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            #Reset
            if event.key == pygame.K_r:
                resetAll()

        #Mouse Events
        if event.type == pygame.MOUSEBUTTONDOWN:
            player1.click()
            if event.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()
                #mouseY > height/2 and
                if mouseY > height/2 and player1.blocks > 0:
                    for e in elements:
                        if pygame.Rect(e) != pygame.Rect(CELL*(int(mouseX/CELL)), CELL*(int(mouseY/CELL)), 25, 25):
                            elements.append((CELL*(int(mouseX/CELL)), CELL*(int(mouseY/CELL)), 25, 25))
                            player1.blocks -= 1
                            break

            elif event.button == 3:
                mouseX, mouseY = pygame.mouse.get_pos()
                for e in elements:
                    if elements.index(e) > 7:
                        if pygame.Rect(e) == pygame.Rect(CELL*(int(mouseX/CELL)), CELL*(int(mouseY/CELL)), 25, 25):
                            elements.remove(e)
                            player1.blocks += 1
                            break


    #Movement
    player1.input()
    player2.input()

    #Walls Collision
    player1.wallCollide(width, height)
    player2.wallCollide(width, height+3)

    #Rects Collision
    for e in elements: 
        player1.collideWith(pygame.Rect(e))
        player2.collideWith(pygame.Rect(e))

    #Throns Collision
    for s in throns:
        if player1.collideWithRect(pygame.Rect(s)):
            player1.dead()
            player1.setPos(100, 50)
            player1.resetVel()

    for tr in range(30):
        if tr == 9 or tr == 8:
            continue
        else:
            if player1.collideWithRect(pygame.Rect(175+(25*tr), 225, 25, 24)):
                player1.dead()
                player1.setPos(100, 50)
                player1.resetVel()

    #Enemy Collision
    for n in enemies:
        for b in elements: 
            n.update(pygame.Rect(b))
        if player2.collideWithRect(pygame.Rect(n.createRect())):
            player2.dead()
            player2.setPos(100, height-50)
            player2.resetVel()

    #Lever Collision
    if player2.collideWithRect(pygame.Rect(lever.createRect())) and lever.hasCollideWithPlayer == False:
        lever.hasCollideWithPlayer = True
        player1.lever()

    #Star Collision
    starRect = pygame.Rect(star.createRect())
    player1.collideWithStar(pygame.Rect(starRect.x, starRect.y, starRect.w/2, starRect.h/2))

    pygame.display.update()
    pygame.time.delay(10)

#----------------------------------------------------------------------

#MAIN
class Level5():
    def start():
        player1.level = 5
        while player1.level == 5:
            updateGame()
            drawGame()
