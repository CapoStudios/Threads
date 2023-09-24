import sys, os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

# My File
from player import Player
from util   import drawChessBoard, drawBlackHole

pygame.init()

width, height = 900, 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Threads()")


# SETUP
clock = pygame.time.Clock()
player1 = Player(100, 50,  24, 24, False)

# Font
midFont = pygame.font.Font('../assets/m5x7.ttf', 64)
bigFont = pygame.font.Font('../assets/m5x7.ttf', 86)

# Buttons
btn1 = pygame.Rect(300, 225, 225, 75)
btn2 = pygame.Rect(300, 325, 225, 75)

# Images
midBlockImg = pygame.image.load('../assets/midBlock.png')
blockImg = pygame.image.load('../assets/block.png')
robot1 = pygame.transform.scale2x(pygame.image.load('../assets/robot1single.png'))
robot2 = pygame.transform.scale2x(pygame.image.load('../assets/robot2single.png'))

CELL = 25  # GRID

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#---------------------------------------------------------------------------------------
# DRAW
def drawMenu():
    screen.fill(WHITE)                  # Clear Screen
    drawChessBoard(screen, width, CELL) # ChessBoard

    # Title
    screen.blit(pygame.transform.scale2x(midBlockImg), (200, 50), (0, 0, 225*2, 75*2))
    screen.blit(bigFont.render("THREADS()", True, BLACK), (260, 85))
    screen.blit(bigFont.render("THREADS()", True, WHITE), (265, 85))

    # Robots
    screen.blit(pygame.transform.flip(robot1, True, False), (220,  19), (0, 0, 20, 30))
    screen.blit(pygame.transform.flip(robot2, False, True), (600, 201), (0, 0, 30, 42))

    # Buttons
    screen.blit(midBlockImg, (btn1.x, btn1.y), (0, 0, 225, 75))
    screen.blit(midBlockImg, (btn2.x, btn2.y), (0, 0, 225, 75))
    
    # Texts Borders
    screen.blit(midFont.render("PLAY()",    True, BLACK), (333, 230))
    screen.blit(midFont.render("CREDITS()", True, BLACK), (313, 335))
    
    # Texts
    screen.blit(midFont.render("PLAY()",    True, WHITE), (335, 230))
    screen.blit(midFont.render("CREDITS()", True, WHITE), (315, 335))

    # LEVEL ENDING
    drawBlackHole(screen, player1, width, height)

# UPDATE
def updateMenu():
    clock.tick(60)  # FPS

    # Input Events
    for event in pygame.event.get():
        #Exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard Events (Exit)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Mouse Events
        if event.type == pygame.MOUSEBUTTONDOWN:
            player1.click()
            if event.button == 1:
                mousePosition = pygame.mouse.get_pos()
                if btn1.collidepoint(mousePosition):
                    player1.getStar = True
                
                elif btn2.collidepoint(mousePosition) and not player1.alreadyPrint:
                    player1.alreadyPrint = True
                    # Credit "Scene"
                    print("\nCoding and drugs by CapoStudios™")
                    print("Robots asset from \"26 Animated PixelArt Robots\" by \"Mounir Tohami\"")
                    print("Blocks asset from \"16x16 Industrial Tileset\" by \"0x72\"")
                    print("Font from \"m5x7\" by \"Daniel Linssen\" \n\n")
                    print("(Making a Credits Scene was too difficult)")

    pygame.display.update()
    pygame.time.delay(10)

# Menu Class
class Menu:
	def open():
		player1.level = 0
		while player1.level == 0:
			updateMenu()
			drawMenu()
			