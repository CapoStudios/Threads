import sys, pygame, math

# Colors
BLACK = (0, 0, 0)
GRAY  = (191, 191, 191)
GRAYG = (128, 128, 128)
WHITE = (254, 254, 255)

# Draw Chessboard
def drawChessBoard(screen, width, CELL):
    size = 75   # Size of squares
    boardLength = int(width/CELL)
    cnt = 0
    for i in range(-1, boardLength+1):
        for z in range(-1, boardLength+1):
            rectangle = [size*z, size*i, size, size]
            color = WHITE if cnt % 2 else GRAY
        
            pygame.draw.rect(screen, color, rectangle)
            cnt += 1
        cnt -= 1

# Draw An Arrow
def arrow(screen, lcolor, tricolor, start, end, trirad, thickness=2):
    rad = math.pi / 180
    pygame.draw.line(screen, lcolor, start, end, thickness)
    
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi / 2
    pygame.draw.polygon(screen, tricolor, ((end[0] + trirad * math.sin(rotation),
                                        end[1] + trirad * math.cos(rotation)),
                                       (end[0] + trirad * math.sin(rotation - 120 * rad),
                                        end[1] + trirad * math.cos(rotation - 120 * rad)),
                                       (end[0] + trirad * math.sin(rotation + 120 * rad),
                                        end[1] + trirad * math.cos(rotation + 120 * rad))))

# Draw Info on Screen
def drawInfoTexts(screen, font, level, blocks):
    texts = ["int level  = " + str(level), "int blocks = " + str(blocks), "if key.press == 'r':", "   restart()"]
    for i, text in enumerate(texts):
        screen.blit(font.render(text,  True, BLACK), (5, 5 + (20 * i)))


# Draw the Grid in the bottom of the screen
def drawBottomGrid(screen, height, width, blocks, mousePosition, CELL, blockImg):
    mouseX, mouseY = mousePosition
    if mouseY > height/2:
        # Draw Grid
        for i in range(int(width/(CELL))):
            color = BLACK if i == 0 else GRAYG
            pygame.draw.line(screen, color, (i*CELL, height/2), (i*CELL, height))
            pygame.draw.line(screen, color, (0, (i*CELL)+height/2), (width, (i*CELL) + height/2))

        if blocks > 0:  # Draw Cell
            screen.blit(blockImg, (CELL*(int(mouseX/CELL)), CELL*(int(mouseY/CELL))), (0, 0, 50, 50))


# Draw Black Hole at the end of a Level
def drawBlackHole(screen, player, width, height):
    if player.getStar:
        if player.endCircleRadius > 250:
            pygame.draw.circle(screen, BLACK, (width/2, height/2), int(player.endCircleRadius*2.1), height)
            player.endCircleRadius -= 5
        else:
            screen.fill(BLACK)
            player.level += 1
