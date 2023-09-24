import pygame
from tkinter import *
from tkinter import messagebox

# My File
from player import Player
from enemy  import Enemy
from hammer import Hammer
from lever  import Lever
from star   import Star
from util   import drawChessBoard, drawInfoTexts, drawBottomGrid, drawBlackHole
from events import handleInputEvents

pygame.init()

width, height = 900, 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Threads()")


clock = pygame.time.Clock()                          # FPS CLOCK
font  = pygame.font.Font('../assets/m5x7.ttf', 32)   # FONT

# Player variables
player1 = Player(100, 50,  24, 24, False)
player2 = Player(100, height-50, 25, 25, True)

# Images
robot1 = pygame.transform.scale2x(pygame.image.load('../assets/robot1single.png'))
robot2 = pygame.transform.scale2x(pygame.image.load('../assets/robot2single.png'))
blockImg  = pygame.image.load('../assets/block.png')
thronsImg = pygame.image.load('../assets/throns.png')
leverImg  = pygame.transform.scale2x(pygame.image.load('../assets/lever.png'))

# Star & Lever
star = Star(775, 50, 5)
starBorder = Star((star.getX())/5, ((star.getY())/5)-10, 4)

lever = Lever(825, 475)

# Elements
def getElements():
    return [
        # UP
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

        # DOWN
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

# Throns
throns = [
    (300, 75,  25, 25),
    (375, 225, 25, 25),
    (450, 225, 25, 25),
    (375, 75,  25, 25),
    (450, 75,  25, 25),
]

# GRID
CELL = 25

# Colors
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
GRAY   = (128, 128, 128)
YELLOW = (230, 255, 80)

# Reset ALL
def resetAll():
    player1.reset(x=100, y=50)
    player2.reset(x=100, y=height-50)

    lever.reset()


# DRAW FUNCTION
def drawGame(elements):
    screen.fill(WHITE)                  # Clear Screen
    drawChessBoard(screen, width, CELL) # ChessBoard

    # Player 1
    player1.draw(screen, robot1, player1.getX(), player1.getY() - player1.getH()/3.6, (0, 0, 20, 30)) 

    # Throns
    for t in range(36):
        screen.blit(pygame.transform.flip(thronsImg, False, True), (25*t, 251), (0, 0, 25*2, 25*2))
        screen.blit(pygame.transform.flip(thronsImg, False, False),(25*t, 225), (0, 0, 25*2, 25*2))

    # Elements(Blocks)
    for e in visible: 
        b = pygame.Rect(e)
        screen.blit(blockImg, (b.x, b.y), (0, 0, 50, int(height/2)))

    # Line
    pygame.draw.line(screen, BLACK, (0, height/2), (width, height/2))

    # Player 2
    player2.draw(screen, robot2, player2.getX()-5, player2.getY()+1, (0, 0, 30, 42))

    # Lever
    lever.draw(screen, leverImg)

    # Draw Star with Border
    starBorder.draw(screen, BLACK, starBorder.createStarPoints())
    star.draw(screen, YELLOW, star.createStarPoints())

    # Draw the Texts, the Grid & the Black Hole
    drawInfoTexts(screen, font, player1.level, player1.blocks)
    drawBottomGrid(screen, height, width, player1.blocks, pygame.mouse.get_pos(), CELL, blockImg)
    drawBlackHole(screen, player1, width, height)


# UPDATE FUNCTION
def updateGame(elements):
    clock.tick(60)  # FPS

    # Handle inputs events
    handleInputEvents(player1, elements, height, CELL)

    # Movement, Walls Collision & Rects Collision
    players = [player1, player2]
    for i, player in enumerate(players):
        player.update(width, height+(i*3), elements)

    # Throns Collision
    for t in range(36):
        if player1.collideWithRect(pygame.Rect(25*t, 225, 25, 24)):
            player1.dead()
            player1.setPos(100, 50)
            player1.resetVel()

        if player2.collideWithRect(pygame.Rect(25*t, 251, 25, 24)):
            player1.dead()
            player2.setPos(100, height-50)
            player2.resetVel()

    # Lever Collision
    if player2.collideWithRect(pygame.Rect(lever.createRect())) and not lever.hasCollideWithPlayer:
        player1.lever()
        lever.hasCollideWithPlayer = True
        for i in range(2):
            elements.pop(59)
            visible.pop(47)

    # Star Collision
    starRect = pygame.Rect(star.createRect())
    if player1.collideWithRect(pygame.Rect(starRect.x, starRect.y, starRect.w/2, starRect.h/2)):      
        Tk().wm_withdraw() # Hide the tkinter window
        messagebox.showerror('Fatal Error', "The programmer's imagination is over")
        
        pygame.quit()
        print("\nThank you for playing.\n")
        sys.exit()

    pygame.display.update()


# Level 7 Class
class Level7():
    def __init__(self):
        self.elements = getElements()
        self.restart  = False
        
    def start(self):
        player1.level = 7
        while player1.level == 7 and not self.restart:
            updateGame(self.elements)
            drawGame(self.elements)
            self.restart = player1.restart
        
        resetAll()
        self.elements = getElements()

        if self.restart:
            self.restart = False
            self.start()
