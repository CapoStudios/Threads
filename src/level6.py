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
blockImg = pygame.image.load('../assets/block.png')
bigBlockImg = pygame.image.load('../assets/bigBlock.png')
enemyImg  = pygame.image.load('../assets/enemy.png')
thronsImg = pygame.image.load('../assets/throns.png')
hammerImg = pygame.transform.scale2x(pygame.image.load('../assets/hammer.png'))
leverImg  = pygame.transform.scale2x(pygame.image.load('../assets/lever.png'))

# Hammer & Lever
hammer  = Hammer(510, 175)
hammer2 = Hammer(165, 0)

lever = Lever(770, 275)

# Enemies
enemies = [ Enemy(425, 225, False, 0.01) ]

# Star
star = Star(775, 50, 5)
starBorder = Star((star.getX())/5, ((star.getY())/5)-10, 4)

# Elements
def getElements():
    return [
        # UP
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

        # DOWN
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

    hammer.reset()
    hammer2.reset()
    lever.reset()


# DRAW FUNCTION
def drawGame(elements):
    screen.fill(WHITE)                  # Clear Screen
    drawChessBoard(screen, width, CELL) # ChessBoard

    # Player 1
    player1.draw(screen, robot1, player1.getX(), player1.getY() - player1.getH()/3.6, (0, 0, 20, 30)) 

    # Thorns
    for s in throns:
            sp = pygame.Rect(s)
            screen.blit(pygame.transform.flip(thronsImg, False, False), (sp.x, sp.y), (0, 0, 25*2, 25*2))
    for t in range(36):
        screen.blit(pygame.transform.flip(thronsImg, False, True), (25*t, 251), (0, 0, 25*2, 25*2))

    # Elements(Blocks)
    for e in elements: 
        b = pygame.Rect(e)
        if pygame.Rect(e) == pygame.Rect(675, 0, 25, height/2):
            screen.blit(bigBlockImg, (b.x, b.y), (0, 0, 50, int(height/2)))
        elif pygame.Rect(e) == pygame.Rect(675, 0, 25, (height/2)-25):
            screen.blit(bigBlockImg, (b.x, b.y-25), (0, 0, 50, int(height/2)))
        else:
            screen.blit(blockImg, (b.x, b.y), (0, 0, 50, 50))

    # Line
    pygame.draw.line(screen, BLACK, (0, height/2), (width, height/2))

    # Player 2
    player2.draw(screen, robot2, player2.getX()-5, player2.getY()+1, (0, 0, 30, 42))

    # Enemies
    for n in enemies:
        n.draw(screen, enemyImg)

    # Draw Hammers & Lever
    hammer.draw(screen,  hammerImg)
    hammer2.draw(screen, hammerImg)

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
    for s in throns:
        if player1.collideWithRect(pygame.Rect(s)):
            player1.dead()
            player1.setPos(100, 50)
            player1.resetVel()

    for t in range(36):
        if player2.collideWithRect(pygame.Rect(25*t, 251, 25, 24)):
            player1.dead()
            player2.setPos(100, height-50)
            player2.resetVel()

    # Enemy Collision
    for n in enemies:
        for b in elements: 
            n.update(pygame.Rect(b))
        if player1.collideWithRect(pygame.Rect(n.createRect())):
            player1.dead()
            player1.setPos(100, 50)
            player1.resetVel()

    # Hammer Collision
    if player1.collideWithRect(pygame.Rect(hammer.createRect())) and not hammer.hasCollideWithPlayer:
        player1.click()
        hammer.hasCollideWithPlayer = True
        player1.blocks += 1

    if player1.collideWithRect(pygame.Rect(hammer2.createRect())) and not hammer2.hasCollideWithPlayer:
        player1.click()
        hammer2.hasCollideWithPlayer = True
        player1.blocks += 1

    # Lever Collision
    if player2.collideWithRect(pygame.Rect(lever.createRect())) and lever.hasCollideWithPlayer == False:
        player1.lever()
        lever.hasCollideWithPlayer = True
        elements.pop(43)
        elements.append((675, 0, 25, (height/2)-25))

    # Star Collision
    starRect = pygame.Rect(star.createRect())
    player1.collideWithStar(pygame.Rect(starRect.x, starRect.y, starRect.w/2, starRect.h/2))

    pygame.display.update()
    pygame.time.delay(10)


# Level6 Class
class Level6():
    def __init__(self):
        self.elements = getElements()
        self.restart  = False
        
    def start(self):
        player1.level = 6
        while player1.level == 6 and not self.restart:
            updateGame(self.elements)
            drawGame(self.elements)
            self.restart = player1.restart
        
        resetAll()
        self.elements = getElements()

        if self.restart:
            self.restart = False
            self.start()
