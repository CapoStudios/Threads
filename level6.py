import sys, os, math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

#My File
from player import Player
from enemy import Enemy
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
bigBlockImg = pygame.image.load('assets/bigBlock.png')
enemyImg = pygame.image.load('assets/enemy.png')
thronsImg = pygame.image.load('assets/throns.png')
hammerImg = pygame.transform.scale2x(pygame.image.load('assets/hammer.png'))
leverImg = pygame.transform.scale2x(pygame.image.load('assets/lever.png'))

#Hammer
hammer  = Hammer(510, 175)
hammer2 = Hammer(165, 0)

#Enemies
enemies = [
    Enemy(425, 225, False, 0.01)
]

#Lever
lever = Lever(770, 275)

#Star
star = Star(775, 50, 5)
starBorder = Star((star.getX())/5, ((star.getY())/5)-10, 4)

#Elements
elements = [
    #UP
    (150, 200, 25, 25),
    (150, 175, 25, 25),
    (175, 175, 25, 25),
    (250, 125, 25, 25),
    (150, 150, 25, 25),
    (150, 125, 25, 25),
    (150, 100, 25, 25),
    (150, 75, 25, 25),
    (150, 50, 25, 25),
    (150, 25, 25, 25),
    (150, 0, 25, 25),
    (275, 225, 25, 25),
    (300, 225, 25, 25),
    (300, 200, 25, 25),
    (300, 175, 25, 25),
    (300, 150, 25, 25),
    (300, 100, 25, 25),
    (300, 125, 25, 25),
    (275, 100, 25, 25),
    (525, 125, 25, 25),
    (525, 100, 25, 25),
    (525, 75, 25, 25),
    (525, 50, 25, 25),
    (525, 25, 25, 25),
    (525, 0, 25, 25),
    (525, 225, 25, 25),
    (525, 150, 25, 25),
    (325, 100, 25, 25),
    (350, 100, 25, 25),
    (375, 100, 25, 25),
    (400, 100, 25, 25),
    (425, 100, 25, 25),
    (450, 100, 25, 25),
    (475, 100, 25, 25),
    (500, 150, 25, 25),
    (475, 150, 25, 25),
    (450, 150, 25, 25),
    (425, 150, 25, 25),
    (400, 150, 25, 25),
    (375, 150, 25, 25),
    (375, 150, 25, 25),
    (350, 150, 25, 25),
    (175, 50, 25, 25),
    (675, 0, 25, height/2),
    (825, 125, 25, 25),
    (875, 175, 25, 25),
    (850, 200, 25, 25),

    #DOWN
    (100, 275, 25, 25),
    (225, 350, 25, 25),
    (350, 300, 25, 25),
    (450, 350, 25, 25),
    (575, 425, 25, 25),
    (650, 350, 25, 25),
    (750, 250, 25, 25),
    (775, 250, 25, 25),
    (800, 250, 25, 25),
]

#Throns
throns = [
    (300, 75,  25, 25),
    (375, 225, 25, 25),
    (450, 225, 25, 25),
    (375, 75,  25, 25),
    (450, 75,  25, 25),
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
    hammer2.reset()
    lever.hasCollideWithPlayer = False
    resetElements(55)
    resetElements(55)


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
    for s in throns:
            sp = pygame.Rect(s)
            screen.blit(pygame.transform.flip(thronsImg, False, False), (sp.x, sp.y), (0, 0, 25*2, 25*2))
    for t in range(36):
        screen.blit(pygame.transform.flip(thronsImg, False, True), (0+(25*t), 251), (0, 0, 25*2, 25*2))

    #Elements(Blocks)
    for e in elements: 
        b = pygame.Rect(e)
        if pygame.Rect(e) == pygame.Rect(675, 0, 25, height/2):
            screen.blit(bigBlockImg, (b.x, b.y), (0, 0, 50, int(height/2)))
        elif pygame.Rect(e) == pygame.Rect(675, 0, 25, (height/2)-25):
            screen.blit(bigBlockImg, (b.x, b.y-25), (0, 0, 50, int(height/2)))
        else:
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
    hammer2.draw(screen, hammerImg)

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
                #print("x: " + str(mouseX) + " | y: " + str(mouseY)) 
                if mouseY > height/2 and player1.blocks > 0:
                    for e in elements:
                        if pygame.Rect(e) != pygame.Rect(CELL*(int(mouseX/CELL)), CELL*(int(mouseY/CELL)), 25, 25):
                            elements.append((CELL*(int(mouseX/CELL)), CELL*(int(mouseY/CELL)), 25, 25))
                            #print(str(elements[len(elements)-1]))
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

    for t in range(36):
        if player2.collideWithRect(pygame.Rect(0+(25*t), 251, 25, 24)):
            player1.dead()
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

    if player1.collideWithRect(pygame.Rect(hammer2.createRect())) and hammer2.hasCollideWithPlayer == False:
        player1.click()
        hammer2.hasCollideWithPlayer = True
        player1.blocks += 1

    #Lever Collision
    if player2.collideWithRect(pygame.Rect(lever.createRect())) and lever.hasCollideWithPlayer == False:
        player1.lever()
        lever.hasCollideWithPlayer = True
        elements.pop(43)
        elements.append((675, 0, 25, (height/2)-25))

    #Star Collision
    starRect = pygame.Rect(star.createRect())
    player1.collideWithStar(pygame.Rect(starRect.x, starRect.y, starRect.w/2, starRect.h/2))

    pygame.display.update()
    pygame.time.delay(10)

#----------------------------------------------------------------------

#MAIN
class Level6():
    def start():
        player1.level = 6
        while player1.level == 6:
            updateGame()
            drawGame()
