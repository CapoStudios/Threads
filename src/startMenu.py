import sys, os, math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

#My File
from player import Player

pygame.init()

width, height = 900, 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Threads()")

#----------------------------------------------------------------------

#SETUP
clock = pygame.time.Clock()
player1 = Player(100, 50,  24, 24, (0, 29, 213), False)

#Font
midFont = pygame.font.Font('../assets/m5x7.ttf', 64)
bigFont = pygame.font.Font('../assets/m5x7.ttf', 86)

#Buttons
btn1 = pygame.Rect(300, 225, 225, 75)
btn2 = pygame.Rect(300, 325, 225, 75)
#btn3 = pygame.Rect(15, 10, 225, 75)

#Images
midBlockImg = pygame.image.load('../assets/midBlock.png')
blockImg = pygame.image.load('../assets/block.png')
robot1 = pygame.transform.scale2x(pygame.image.load('../assets/robot1single.png'))
robot2 = pygame.transform.scale2x(pygame.image.load('../assets/robot2single.png'))

#Menu
#---------------------------------------------------------------------------------------
#DRAW
def drawMenu():
    #Clear Screen
    screen.fill((255, 255, 255))

    #(Chess Board)
    #----------------------------------------------------------------------------
    #Size of squares
    size = 75
    #board length, must be even
    boardLength = int(width/25)
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

    #Title
    screen.blit(pygame.transform.scale2x(midBlockImg), (200, 50), (0, 0, 225*2, 75*2))
    screen.blit(bigFont.render("THREADS()", True, (0, 0, 0)), (260, 85))
    screen.blit(bigFont.render("THREADS()", True, (255, 255, 255)), (265, 85))

    #Robots
    screen.blit(pygame.transform.flip(robot1, True, False), (220, 19), (0, 0, 20, 30))
    screen.blit(pygame.transform.flip(robot2, False, True), (600, 201), (0, 0, 30, 42))

    #Buttons
    screen.blit(midBlockImg, (btn1.x, btn1.y), (0, 0, 225, 75))
    screen.blit(midBlockImg, (btn2.x, btn2.y), (0, 0, 225, 75))
    #Texts(black)
    screen.blit(midFont.render("PLAY()", True, (0, 0, 0)), (333, 230))
    screen.blit(midFont.render("CREDITS()", True, (0, 0, 0)), (313, 335))
    #Texts(white)
    screen.blit(midFont.render("PLAY()", True, (255, 255, 255)), (335, 230))
    screen.blit(midFont.render("CREDITS()", True, (255, 255, 255)), (315, 335))

    if player1.alreadyPrint == True:
        player1.alreadyPrint = True
    else:
        player1.alreadyPrint = False

    #END
    if player1.getStar == True:
        if player1.endCircleRadius > 250:
            pygame.draw.circle(screen, (0, 0, 0), (width/2, height/2), int(player1.endCircleRadius*2.1), height)
            player1.endCircleRadius -= 5
        else:
            screen.fill((0, 0, 0))
            player1.level += 1

#UPDATE
def updateMenu():
    #FPS
    clock.tick(60)

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

        #Mouse Events
        if event.type == pygame.MOUSEBUTTONDOWN:
            player1.click()
            if event.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()
                if btn1.collidepoint((mouseX, mouseY)):
                	player1.level += 1
                elif btn2.collidepoint((mouseX, mouseY)) and player1.alreadyPrint == False:
                    player1.alreadyPrint = True
                    print("A new game from CapoStudios")
                    print("Robots asset from \"26 Animated PixelArt Robots\" by \"Mounir Tohami\"")
                    print("Blocks asset from \"16x16 Industrial Tileset\" by \"0x72\"")
                    print("Font from \"m5x7\" by \"Daniel Linssen\" \n\n")
                    print("(Making a Credits Scene was too difficult)")

    pygame.display.update()
    pygame.time.delay(10)

#MAIN
class Menu:
	def open():
		player1.level = 0
		while player1.level == 0:
			updateMenu()
			drawMenu()
			