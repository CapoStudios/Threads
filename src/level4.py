import pygame

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
enemyImg  = pygame.image.load('../assets/enemy.png')
thronsImg = pygame.image.load('../assets/throns.png')
hammerImg = pygame.transform.scale2x(pygame.image.load('../assets/hammer.png'))
leverImg  = pygame.transform.scale2x(pygame.image.load('../assets/lever.png'))

# Hammer & Lever
hammer = Hammer(825, 200)
lever  = Lever(790, 450)

# Enemies
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

# Star
star = Star(775, 50, 5)
starBorder = Star((star.getX())/5, ((star.getY())/5)-10, 4)

# Elements
def getElements():
    return [
        # UP
        (-25, 225, 25, 25),
        (900, 225, 25, 25),
        (100, 125, 25, 25),
        (75, 125,  25, 25),
        (125, 125, 25, 25),

        # DOWN
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


CELL = 25  # GRID

# Colors
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
GRAY   = (128, 128, 128)
YELLOW = (230, 255, 80)

# Reset ALL
def resetAll():
    player1.reset(x=100, y=50)
    player2.reset(x=100, y=height-50)

    hammer.reset()
    lever.reset()


# DRAW FUNCTION
def drawGame(elements):
    screen.fill(WHITE)                  # Clear Screen
    drawChessBoard(screen, width, CELL) # ChessBoard

    # Player 1
    player1.draw(screen, robot1, player1.getX(), player1.getY() - player1.getH()/3.6, (0, 0, 20, 30)) 

    # Thorns
    for t in range(36):
        screen.blit(pygame.transform.flip(thronsImg, False, True), (25*t, 251), (0, 0, 25*2, 25*2))

    # Elements(Blocks)
    for element in elements: 
        block = pygame.Rect(element)
        screen.blit(blockImg, (block.x, block.y), (0, 0, 50, 50))

    # Line
    pygame.draw.line(screen, BLACK, (0, height/2), (width, height/2))

    # Player 2
    player2.draw(screen, robot2, player2.getX()-5, player2.getY()+1, (0, 0, 30, 42))

    # Enemies
    for enemy in enemies:
        enemy.draw(screen, enemyImg)

    # Draw Hammer & Lever
    hammer.draw(screen, hammerImg)
    lever.draw(screen, leverImg)


    # Draw Star & Border
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
        if player2.collideWithRect(pygame.Rect(25*t, 251, 25, 24)):
            player2.dead()
            player2.setPos(100, height-50)
            player2.resetVel()

    # Enemy Collision
    for enemy in enemies:
        for b in elements:
            enemy.update(pygame.Rect(b))
        
        if player1.collideWithRect(pygame.Rect(enemy.createRect())):
            player1.dead()
            player1.setPos(100, 50)
            player1.resetVel()

    # Hammer Collision
    if player1.collideWithRect(pygame.Rect(hammer.createRect())) and not hammer.hasCollideWithPlayer:
        player1.click()
        hammer.hasCollideWithPlayer = True
        player1.blocks += 1

    # Lever Collision
    if player2.collideWithRect(pygame.Rect(lever.createRect())) and not lever.hasCollideWithPlayer:
        player1.lever()
        lever.hasCollideWithPlayer = True
        for x in [225, 375, 400, 550, 575]:
            elements.append((x, 75, 25, 25))

    # Star Collision
    starRect = pygame.Rect(star.createRect())
    player1.collideWithStar(pygame.Rect(starRect.x, starRect.y, starRect.w/2, starRect.h/2))

    pygame.display.update()


# Level 4 Class
class Level4():
    def __init__(self):
        self.elements = getElements()
        self.restart  = False
        
    def start(self):
        player1.level = 4
        while player1.level == 4 and not self.restart:
            updateGame(self.elements)
            drawGame(self.elements)
            self.restart = player1.restart
        
        resetAll()
        self.elements = getElements()

        if self.restart:
            self.restart = False
            self.start()
