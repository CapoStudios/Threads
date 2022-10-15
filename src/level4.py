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
enemyImg = pygame.image.load('../assets/enemy.png')
thronsImg = pygame.image.load('../assets/throns.png')
hammerImg = pygame.transform.scale2x(pygame.image.load('../assets/hammer.png'))
leverImg = pygame.transform.scale2x(pygame.image.load('../assets/lever.png'))

#Hammer
hammer = Hammer(825, 200)

#Enemies
enemies = [
    Enemy(0, 225, False,  0.15),
    Enemy(25, 225, False, 0.15),
    Enemy(50, 225, False, 0.15),
    Enemy(75, 225, False, 0.15),

    Enemy(200, 225, False, 0.15),
    Enemy(225, 225, False, 0.15),
    Enemy(250, 225, False, 0.15),
    Enemy(275, 225, False, 0.15),

    Enemy(400, 225, False, 0.15),
    Enemy(425, 225, False, 0.15),
    Enemy(450, 225, False, 0.15),
    Enemy(475, 225, False, 0.15),

    Enemy(600, 225, False, 0.15),
    Enemy(625, 225, False, 0.15),
    Enemy(650, 225, False, 0.15),
    Enemy(675, 225, False, 0.15),

    Enemy(800, 225, False, 0.15),
    Enemy(825, 225, False, 0.15),
    Enemy(850, 225, False, 0.15),
    Enemy(875, 225, False, 0.15),
]

#Lever
lever = Lever(790, 450)

#Star
star = Star(775, 50, 5)
starBorder = Star((star.getX())/5, ((star.getY())/5)-10, 4)

#Elements
elements = [
    #UP
    (-25, 225, 25, 25),
    (900, 225, 25, 25),
    (100, 125, 25, 25),
    (75, 125,  25, 25),
    (125, 125, 25, 25),

    #DOWN
    (100, 375, 25, 25),
    (75, 375, 25,  25),
    (125, 375, 25, 25),
    (775, 425, 25, 25),
    (800, 425, 25, 25),
    (825, 425, 25, 25),

    (675, 300, 25, 25),
    (800, 325, 25, 25),
    (725, 375, 25, 25),
    (375, 425, 25, 25),
    (500, 425, 25, 25),
    (550, 300, 25, 25),
    (725, 275, 25, 25),
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
    hammer.reset()
    lever.hasCollideWithPlayer = False
    resetElements(17)
    resetElements(17)
    resetElements(17)


#DRAW
def drawGame():
    #Clear Screen
    screen.fill((255, 255, 255))

    #ChessBoard
    drawChessBoard(screen, width, CELL)


    #Player 1
    player1.draw(screen, robot1, player1.getX(), player1.getY() - player1.getH()/3.6, (0, 0, 20, 30)) 

    #Thorns
    for t in range(36):
        screen.blit(pygame.transform.flip(thronsImg, False, True), (0+(25*t), 251), (0, 0, 25*2, 25*2))

    #Elements(Blocks)
    for e in elements: 
        b = pygame.Rect(e)
        screen.blit(blockImg, (b.x, b.y), (0, 0, 50, 50))

    #Line
    pygame.draw.line(screen, (0,0,0), (0, height/2), (width, height/2))

    #Player 2
    player2.draw(screen, robot2, player2.getX()-5, player2.getY()+1, (0, 0, 30, 42))

    #Enemies
    for n in enemies:
        n.draw(screen, enemyImg)

    #Hammer
    hammer.draw(screen, hammerImg)

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
    for t in range(36):
        if player2.collideWithRect(pygame.Rect(0+(25*t), 251, 25, 24)):
            player2.dead()
            player2.setPos(100, height-50)
            player2.resetVel()

    #Enemy Collision
    for n in enemies:
        for b in elements: 
            n.update(pygame.Rect(b))
        if player1.collideWithRect(pygame.Rect(n.createRect())):
            player1.dead()
            player1.setPos(100, 50)
            player1.resetVel()

    #Hammer Collision
    if player1.collideWithRect(pygame.Rect(hammer.createRect())) and hammer.hasCollideWithPlayer == False:
        player1.click()
        hammer.hasCollideWithPlayer = True
        player1.blocks += 1

    #Lever Collision
    if player2.collideWithRect(pygame.Rect(lever.createRect())) and lever.hasCollideWithPlayer == False:
        player1.lever()
        lever.hasCollideWithPlayer = True
        elements.append((225, 75, 25, 25))
        elements.append((400, 75, 25, 25))
        elements.append((375, 75, 25, 25))
        elements.append((575, 75, 25, 25))
        elements.append((550, 75, 25, 25))

    #Star Collision
    starRect = pygame.Rect(star.createRect())
    player1.collideWithStar(pygame.Rect(starRect.x, starRect.y, starRect.w/2, starRect.h/2))

    pygame.display.update()
    pygame.time.delay(10)

#----------------------------------------------------------------------

#MAIN
class Level4():
    def start():
        player1.level = 4
        while player1.level == 4:
            updateGame()
            drawGame()
