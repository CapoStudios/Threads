import pygame

# My File
from player import Player
from hammer import Hammer
from lever  import Lever
from star   import Star
from util   import drawChessBoard, arrow, drawInfoTexts, drawBottomGrid, drawBlackHole
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
blockImg    = pygame.image.load('../assets/block.png')
bigBlockImg = pygame.image.load('../assets/bigBlock.png')
hammerImg = pygame.transform.scale2x(pygame.image.load('../assets/hammer.png'))
leverImg  = pygame.transform.scale2x(pygame.image.load('../assets/lever.png'))

# Hammer & Lever
hammer = Hammer(475, 200)
lever  = Lever(392, 350)

# Star
star = Star(750, 150, 5)
starBorder = Star((star.getX())/5, ((star.getY())/5)-10, 4)

# Elements
def getElements():
    return [
        # UP
        (250, 225, 25, 25),
        (300, 200, 25, 25),
        (325, 225, 25, 25),

        # DOWN
        (300, 250, 25, 25),
        (375, 325, 25, 25),
        (400, 325, 25, 25),
        (425, 325, 25, 25),

        # UP
        (625, 0, 25, height/2)
    ]

CELL = 25   # GRID

# Colors
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
GRAY   = (128, 128, 128)
YELLOW = (230, 255, 80)

# restart ALL
def resetAll():
    player1.reset(x=100, y=50)
    player2.reset(x=100, y=height-50)

    hammer.reset()
    lever.reset()

# DRAW FUCTION
def drawGame(elements):
    screen.fill(WHITE)                  # Clear Screen
    drawChessBoard(screen, width, CELL) # ChessBoard

    # Elements(Blocks)
    for element in elements: 
        block = pygame.Rect(element)
        if block == pygame.Rect(625, 0, 25, height/2):
            screen.blit(bigBlockImg, (block.x, block.y), (0, 0, 50, int(height/2)))

        elif block == pygame.Rect(625, 0, 25, (height/2)-25):
            screen.blit(bigBlockImg, (block.x, block.y-25), (0, 0, 50, int(height/2)))

        else:
            screen.blit(blockImg, (block.x, block.y), (0, 0, 50, 50))

    # Player 1 & Player 2
    player1.draw(screen, robot1, player1.getX(), player1.getY() - player1.getH()/3.6, (0, 0, 20, 30)) 
    player2.draw(screen, robot2, player2.getX()-5, player2.getY()+1, (0, 0, 30, 42))
    
    # Line
    pygame.draw.line(screen, BLACK, (0, height/2), (width, height/2))

    # Draw Hammer & Lever
    hammer.draw(screen, hammerImg)
    lever.draw(screen,  leverImg)

    # Tutorial with Arrows
    if not hammer.hasCollideWithPlayer:
        screen.blit(font.render("Take this", True, BLACK), (403, 100))
        arrow(screen, BLACK, BLACK, (433, 124), (469, 191), 12, 4)

    elif not player1.moveCursorTutorial and player1.blocks == 1:
        screen.blit(font.render("Move the cursor here", True, BLACK), (372, 180))
        arrow(screen, BLACK, BLACK, (402, 209), (351, 275), 12, 4)

    elif player1.moveCursorTutorial and player1.blocks == 1:
        screen.blit(font.render("Try clicking here", True, BLACK), (307, 389))
        arrow(screen, BLACK, BLACK, (337, 399), (337, 316), 12, 4)

    elif len(elements) > 8 and not lever.hasCollideWithPlayer:
        screen.blit(font.render("Come here", True, BLACK), (464, 420))
        arrow(screen, BLACK, BLACK, (474, 426), (440, 387), 12, 4)

    elif lever.hasCollideWithPlayer:
        screen.blit(font.render("Well, I think you are ready", True, BLACK), (333, 80))
        arrow(screen, BLACK, BLACK, (506, 103), (585, 183), 12, 4)

    # Draw Star with Border
    starBorder.draw(screen, BLACK, starBorder.createStarPoints())
    star.draw(screen, YELLOW, star.createStarPoints())

    # Draw the Texts, the Grid & the Black Hole
    drawInfoTexts(screen, font, player1.level, player1.blocks)
    drawBottomGrid(screen, height, width, player1.blocks, pygame.mouse.get_pos(), CELL, blockImg)
    drawBlackHole(screen, player1, width, height)


# UPDATE FUNCTION
def updateGame(elements):
    clock.tick(60) # FPS

    # Handle inputs events
    handleInputEvents(player1, elements, height, CELL)

    # Movement, Walls Collision & Rects Collision
    players = [player1, player2]
    for i, player in enumerate(players):
        player.update(width, height+(i*3), elements)
        
    # Hammer Collision
    if player1.collideWithRect(pygame.Rect(hammer.createRect())) and not hammer.hasCollideWithPlayer:
        player1.click()
        hammer.hasCollideWithPlayer = True
        player1.blocks += 1

    # Lever Collision
    if player2.collideWithRect(pygame.Rect(lever.createRect())) and not lever.hasCollideWithPlayer:
        player1.lever()
        lever.hasCollideWithPlayer = True

        # Open the Door
        elements.remove((625, 0, 25, height/2))
        elements.append((625, 0, 25, (height/2)-25))

    # Star Collision
    starRect = pygame.Rect(star.createRect())
    player1.collideWithStar(pygame.Rect(starRect.x, starRect.y, starRect.w/2, starRect.h/2))

    pygame.display.update()


# Level 1 Class
class Level1():
    def __init__(self):
        self.elements = getElements()
        self.restart  = False
    
    def start(self):
        while player1.level == 1 and not self.restart:
            updateGame(self.elements)
            drawGame(self.elements)
            self.restart = player1.restart
        
        resetAll()
        self.elements = getElements()

        if self.restart:
            self.restart = False
            self.start()
