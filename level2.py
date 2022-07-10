import sys, os, math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

#My File
from player import Player
from hammer import Hammer
from lever import Lever
from star import Star

pygame.init()

width, height = 900, 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Threads()")

#----------------------------------------------------------------------

#SETUP
clock = pygame.time.Clock()

#Font
font = pygame.font.Font('assets/m5x7.ttf', 32)

#Player variables
player1 = Player(100, 50,  24, 24, (0, 29, 213), False)
player2 = Player(100, height-50, 25, 25, (255, 115, 4), True)

#Images
robot1 = pygame.transform.scale2x(pygame.image.load('assets/robot1single.png'))
robot2 = pygame.transform.scale2x(pygame.image.load('assets/robot2single.png'))
blockImg = pygame.image.load('assets/block.png')
thronsImg = pygame.image.load('assets/throns.png')
hammerImg = pygame.transform.scale2x(pygame.image.load('assets/hammer.png'))
leverImg = pygame.transform.scale2x(pygame.image.load('assets/lever.png'))

#Hammer
hammer = Hammer(475, 200)

#Lever
lever = Lever(750, 250)

#Star
star = Star(670, 75, 5)
starBorder = Star((star.getX())/5, ((star.getY())/5)-10, 4)

#Elements
elements = [
    #UP
    (250, 200, 25, 25),
    (500, 150, 25, 25),

    #DOWN
    (300, 250, 25, 25),
    (575, 250, 25, 25),
]

def resetElements(defaultElements):
    for e in elements:
        if elements.index(e) > defaultElements:
            elements.remove(e)

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
    resetElements(3)


#DRAW
def drawGame():
    #Clear Screen
    screen.fill((255, 255, 255))

    #(Chess Board)
    #----------------------------------------------------------------------------
    #Size of squares
    size = 75
    #board length, must be even
    boardLength = int(width/CELL)
    cnt = 0
    for i in range(-1,boardLength+1):
        for z in range(-1,boardLength+1):
            #check if current loop value is even
            if cnt % 2 == 0:
                pygame.draw.rect(screen, (191,191,191),[size*z,size*i,size,size])
            else:
                pygame.draw.rect(screen, (254,254,255), [size*z,size*i,size,size])
            cnt +=1
        #since theres an even number of squares go back one value
        cnt-=1
    #----------------------------------------------------------------------------


    #Player 1
    player1.draw(screen, robot1, player1.getX(), player1.getY() - player1.getH()/3.6, (0, 0, 20, 30)) 

    #Thorns
    for t in range(10):
        screen.blit(pygame.transform.flip(thronsImg, False, True), (325+(25*t), 251), (0, 0, 25*2, 25*2))

    #Elements(Blocks)
    for e in elements: 
        b = pygame.Rect(e)
        screen.blit(blockImg, (b.x, b.y), (0, 0, 50, 50))

    #Line
    pygame.draw.line(screen, (0,0,0), (0, height/2), (width, height/2))

    #Player 2
    player2.draw(screen, robot2, player2.getX()-5, player2.getY()+1, (0, 0, 30, 42))

    #Hammer
    hammer.draw(screen, hammerImg)

    #Lever
    lever.draw(screen, leverImg)


    #Star & Border
    starBorder.draw(screen, (0,0,0), starBorder.createStarPoints())
    star.draw(screen, (230, 255, 80), star.createStarPoints())

    #Texts
    screen.blit(font.render("int Level  = " + str(player1.level), True, (0, 0, 0)), (5, 5))
    screen.blit(font.render("int blocks = " + str(player1.blocks), True, (0, 0, 0)), (5, 25))
    screen.blit(font.render("if key.press == 'r':", True, (0, 0, 0)), (5, 45))
    screen.blit(font.render("   restart()", True, (0, 0, 0)), (5, 65))
    

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
    for t in range(10):
        if player2.collideWithRect(pygame.Rect(325+(25*t), 251, 25, 24)):
            player2.dead()
            player2.setPos(100, height-50)
            player2.resetVel()

    #Hammer Collision
    if player1.collideWithRect(pygame.Rect(hammer.createRect())) and hammer.hasCollideWithPlayer == False:
        player1.click()
        hammer.hasCollideWithPlayer = True
        player1.blocks += 1

    #Lever Collision
    if player2.collideWithRect(pygame.Rect(lever.createRect())) and lever.hasCollideWithPlayer == False:
        player1.lever()
        lever.hasCollideWithPlayer = True
        elements.append((350, 150, 25, 25))

    #Star Collision
    starRect = pygame.Rect(star.createRect())
    player1.collideWithStar(pygame.Rect(starRect.x, starRect.y, starRect.w/2, starRect.h/2))

    pygame.display.update()
    pygame.time.delay(10)

#----------------------------------------------------------------------

#MAIN
class Level2():
    def start():
        player1.level = 2
        while player1.level == 2:
            updateGame()
            drawGame()
