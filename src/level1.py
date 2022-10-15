import sys, os, math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

#My File
from player import Player
from hammer import Hammer
from lever import Lever
from star import Star
from util import drawChessBoard, arrow, resetElements, drawInfoTexts

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
bigBlockImg = pygame.image.load('../assets/bigBlock.png')
hammerImg = pygame.transform.scale2x(pygame.image.load('../assets/hammer.png'))
leverImg = pygame.transform.scale2x(pygame.image.load('../assets/lever.png'))

#Hammer
hammer = Hammer(475, 200)

#Lever
lever = Lever(392, 350)

#Star
star = Star(750, 150, 5)
starBorder = Star((star.getX())/5, ((star.getY())/5)-10, 4)

#Elements
elements = [
    #UP
    (250, 225, 25, 25),
    (300, 200, 25, 25),
    (325, 225, 25, 25),

    #DOWN
    (300, 250, 25, 25),
    (375, 325, 25, 25),
    (400, 325, 25, 25),
    (425, 325, 25, 25),

    #UP
    (625, 0, 25, height/2),
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
    resetElements(7)

#DRAW
def drawGame():
    #Clear Screen
    screen.fill((255, 255, 255))

    #ChessBoard
    drawChessBoard(screen, width, CELL)

    #Player 1
    player1.draw(screen, robot1, player1.getX(), player1.getY() - player1.getH()/3.6, (0, 0, 20, 30)) 

    #Line
    pygame.draw.line(screen, (0,0,0), (0, height/2), (width, height/2))

    #Elements(Blocks)
    for e in elements: 
        b = pygame.Rect(e)
        if pygame.Rect(e) == pygame.Rect(625, 0, 25, height/2):
            screen.blit(bigBlockImg, (b.x, b.y), (0, 0, 50, int(height/2)))
        elif pygame.Rect(e) == pygame.Rect(625, 0, 25, (height/2)-25):
            screen.blit(bigBlockImg, (b.x, b.y-25), (0, 0, 50, int(height/2)))
        else:
            screen.blit(blockImg, (b.x, b.y), (0, 0, 50, 50))

    #Player 2
    player2.draw(screen, robot2, player2.getX()-5, player2.getY()+1, (0, 0, 30, 42))

    #Hammer
    hammer.draw(screen, hammerImg)

    #Lever
    lever.draw(screen, leverImg)

    #Tutorial
    if hammer.hasCollideWithPlayer == False:
        screen.blit(font.render("Take this", True, (0, 0, 0)), (403, 100))
        arrow(screen, (0,0,0), (0,0,0), (433, 124), (469, 191), 12, 4)
    elif player1.moveCursorTutorial == False and player1.blocks  == 1:
        screen.blit(font.render("Move the cursor here", True, (0, 0, 0)), (372, 180))
        arrow(screen, (0,0,0), (0,0,0), (402, 209), (351, 275), 12, 4)
    elif player1.moveCursorTutorial == True and player1.blocks  == 1:
        screen.blit(font.render("Try clicking here", True, (0, 0, 0)), (307, 389))
        arrow(screen, (0,0,0), (0,0,0), (337, 399), (337, 316), 12, 4)
    elif len(elements) > 8 and lever.hasCollideWithPlayer == False:
        screen.blit(font.render("Come here", True, (0, 0, 0)), (464, 420))
        arrow(screen, (0,0,0), (0,0,0), (474, 426), (440, 387), 12, 4)
    elif lever.hasCollideWithPlayer == True:
        screen.blit(font.render("Well, I think you are ready", True, (0, 0, 0)), (333, 80))
        arrow(screen, (0,0,0), (0,0,0), (506, 103), (585, 183), 12, 4)
        #open the Door
        for e in elements:
            elements.pop(7)
            elements.append((625, 0, 25, (height/2)-25))


    #Star & Border
    starBorder.draw(screen, (0,0,0), starBorder.createStarPoints())
    star.draw(screen, (230, 255, 80), star.createStarPoints())

    #Texts
    drawInfoTexts(screen, font, player1.level, player1.blocks)
    

    #Grid
    mouseX, mouseY = pygame.mouse.get_pos()
    if mouseY > height/2:
        #Move Cursor Part Tutorial
        player1.moveCursorTutorial = True
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
    else:
        player1.moveCursorTutorial = False


    #END
    if player1.getStar == True:
        if player1.endCircleRadius > 250:
            pygame.draw.circle(screen, (0, 0, 0), (width/2, height/2), int(player1.endCircleRadius*2.1), height)
            player1.endCircleRadius -= 5
        else:
            screen.fill((0, 0, 0))
            player1.level = 2



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

    #Hammer Collision
    if player1.collideWithRect(pygame.Rect(hammer.createRect())) and hammer.hasCollideWithPlayer == False:
        player1.click()
        hammer.hasCollideWithPlayer = True
        player1.blocks += 1

    #Lever Collision
    if player2.collideWithRect(pygame.Rect(lever.createRect())) and lever.hasCollideWithPlayer == False:
        player1.lever()
        lever.hasCollideWithPlayer = True

    #Star Collision
    starRect = pygame.Rect(star.createRect())
    player1.collideWithStar(pygame.Rect(starRect.x, starRect.y, starRect.w/2, starRect.h/2))

    pygame.display.update()
    pygame.time.delay(10)

#----------------------------------------------------------------------

#MAIN
class Level1():
    def start():
        while player1.level == 1:
            updateGame()
            drawGame()
