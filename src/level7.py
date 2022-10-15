import sys, os, math
from tkinter import *
from tkinter import messagebox

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
leverImg = pygame.transform.scale2x(pygame.image.load('../assets/lever.png'))

#Lever
lever = Lever(825, 475)

#Star
star = Star(775, 50, 5)
starBorder = Star((star.getX())/5, ((star.getY())/5)-10, 4)

#Elements
elements = [
    #UP
    (100, 200, 25, 25),
    (100, 175, 25, 25),
    (100, 75, 25, 25),
    (100, 25, 25, 25),
    (100, 0, 25, 25),
    (100, 100, 25, 25),
    (100, 125, 25, 25),
    (100, 150, 25, 25),
    (175, 275, 25, 25),
    (150, 275, 25, 25),
    (125, 275, 25, 25),
    (200, 200, 25, 25),
    (200, 175, 25, 25),
    (200, 100, 25, 25),
    (200, 50, 25, 25),
    (200, 75, 25, 25),
    (200, 25, 25, 25),
    (200, 0, 25, 25),
    (200, 275, 25, 25),
    (300, 150, 25, 25),
    (300, 325, 25, 25),
    (300, 50, 25, 25),
    (300, 75, 25, 25),
    (300, 25, 25, 25),
    (300, 0, 25, 25),
    (300, 175, 25, 25),
    (300, 200, 25, 25),
    (425, 150, 25, 25),
    (425, 350, 25, 25),
    (425, 175, 25, 25),
    (425, 200, 25, 25),
    (425, 75, 25, 25),
    (425, 50, 25, 25),
    (425, 25, 25, 25),
    (425, 0, 25, 25),
    (525, 200, 25, 25),
    (525, 275, 25, 25),
    (525, 125, 25, 25),
    (525, 100, 25, 25),
    (525, 75, 25, 25),
    (525, 50, 25, 25),
    (525, 25, 25, 25),
    (525, 0, 25, 25),
    (550, 200, 25, 25),
    (550, 175, 25, 25),
    (550, 125, 25, 25),
    (550, 325, 25, 25),
    (575, 175, 25, 25),
    (600, 175, 25, 25),
    (600, 150, 25, 25),
    (575, 325, 25, 25),
    (550, 100, 25, 25),
    (600, 375, 25, 25),
    (550, 400, 25, 25),
    (550, 425, 25, 25),
    (625, 75, 25, 25),
    (650, 75, 25, 25),
    (675, 75, 25, 25),
    (700, 75, 25, 25),
    (700, 50, 25, 25),
    (700, 25, 25, 25),
    (700, 0, 25, 25),
    (600, 450, 25, 25),
    (625, 450, 25, 25),
    (650, 450, 25, 25),
    (675, 450, 25, 25),
    (700, 450, 25, 25),
    (725, 450, 25, 25),
    (750, 450, 25, 25),
    (775, 450, 25, 25),
    (800, 450, 25, 25),
    (825, 450, 25, 25),
    (825, 450, 25, 25),
    (850, 450, 25, 25),
    (875, 450, 25, 25),
    (875, 475, 25, 25),

    #DOWN
    (100, 275, 25, 25),
]

visible = [
    (100, 200, 25, 25),
    (100, 175, 25, 25),
    (100, 150, 25, 25),
    (100, 125, 25, 25),
    (100, 100, 25, 25),
    (100, 75, 25, 25),
    (100, 25, 25, 25),
    (100, 0, 25, 25),
    (200, 200, 25, 25),
    (200, 175, 25, 25),
    (200, 100, 25, 25),
    (200, 75, 25, 25),
    (200, 50, 25, 25),
    (200, 25, 25, 25),
    (200, 0, 25, 25),
    (300, 200, 25, 25),
    (300, 175, 25, 25),
    (300, 150, 25, 25),
    (300, 75, 25, 25),
    (300, 50, 25, 25),
    (300, 25, 25, 25),
    (300, 0, 25, 25),
    (425, 200, 25, 25),
    (425, 175, 25, 25),
    (425, 150, 25, 25),
    (425, 75, 25, 25),
    (425, 50, 25, 25),
    (425, 25, 25, 25),
    (425, 0, 25, 25),
    (525, 200, 25, 25),
    (550, 200, 25, 25),
    (550, 175, 25, 25),
    (575, 175, 25, 25),
    (600, 175, 25, 25),
    (600, 150, 25, 25),
    (550, 125, 25, 25),
    (550, 100, 25, 25),
    (525, 100, 25, 25),
    (525, 125, 25, 25),
    (525, 75, 25, 25),
    (525, 50, 25, 25),
    (525, 25, 25, 25),
    (525, 0, 25, 25),
    (625, 75, 25, 25),
    (650, 75, 25, 25),
    (675, 75, 25, 25),
    (700, 75, 25, 25),
    (700, 50, 25, 25),
    (700, 25, 25, 25),
    (700, 0, 25, 25),
]

#Throns
throns = [
    (300, 75,  25, 25),
    (375, 225, 25, 25),
    (450, 225, 25, 25),
    (375, 75,  25, 25),
    (450, 75,  25, 25),
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


#DRAW
def drawGame():
    #Clear Screen
    screen.fill((255, 255, 255))

    #ChessBoard
    drawChessBoard(screen, width, CELL)


    #Player 1
    player1.draw(screen, robot1, player1.getX(), player1.getY() - player1.getH()/3.6, (0, 0, 20, 30)) 

    #Throns
    for t in range(36):
        screen.blit(pygame.transform.flip(thronsImg, False, True), (0+(25*t), 251), (0, 0, 25*2, 25*2))
        screen.blit(pygame.transform.flip(thronsImg, False, False),(0+(25*t), 225), (0, 0, 25*2, 25*2))

    #Elements(Blocks)
    for e in visible: 
        b = pygame.Rect(e)
        screen.blit(blockImg, (b.x, b.y), (0, 0, 50, int(height/2)))


    #Line
    pygame.draw.line(screen, (0,0,0), (0, height/2), (width, height/2))

    #Player 2
    player2.draw(screen, robot2, player2.getX()-5, player2.getY()+1, (0, 0, 30, 42))


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
    for s in range(36):
        if player1.collideWithRect(pygame.Rect(0+(25*s), 225, 25, 24)):
            player1.dead()
            player1.setPos(100, 50)
            player1.resetVel()

    for t in range(36):
        if player2.collideWithRect(pygame.Rect(0+(25*t), 251, 25, 24)):
            player1.dead()
            player2.setPos(100, height-50)
            player2.resetVel()


    #Lever Collision
    if player2.collideWithRect(pygame.Rect(lever.createRect())) and lever.hasCollideWithPlayer == False:
        player1.lever()
        lever.hasCollideWithPlayer = True
        elements.pop(59)
        elements.pop(59)
        visible.pop(47)
        visible.pop(47)

    #Star Collision
    starRect = pygame.Rect(star.createRect())
    if player1.collideWithRect(pygame.Rect(starRect.x, starRect.y, starRect.w/2, starRect.h/2)):      
        Tk().wm_withdraw() #Hide the tkinter window
        messagebox.showerror('Fatal Error',"The programmer's imagination is over")
        pygame.quit()
        print("\nThank you for playing\n")
        sys.exit()


    pygame.display.update()
    pygame.time.delay(10)

#----------------------------------------------------------------------

#MAIN
class Level7():
    def start():
        player1.level = 7
        while player1.level == 7:
            updateGame()
            drawGame()
