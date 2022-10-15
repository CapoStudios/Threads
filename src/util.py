import sys, os, math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

#Draw Chessboard
def drawChessBoard(screen, width, CELL):
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

#Draw An Arrow
def arrow(screen, lcolor, tricolor, start, end, trirad, thickness=2):
    rad = math.pi/180
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    pygame.draw.polygon(screen, tricolor, ((end[0] + trirad * math.sin(rotation),
                                        end[1] + trirad * math.cos(rotation)),
                                       (end[0] + trirad * math.sin(rotation - 120*rad),
                                        end[1] + trirad * math.cos(rotation - 120*rad)),
                                       (end[0] + trirad * math.sin(rotation + 120*rad),
                                        end[1] + trirad * math.cos(rotation + 120*rad))))

#Reset Elements
def resetElements(defaultElements, elements):
    for e in elements:
        if elements.index(e) > defaultElements:
            elements.remove(e)

#Draw Info on Screen
def drawInfoTexts(screen, font, level, blocks):
    screen.blit(font.render("int Level  = " + str(level), True, (0, 0, 0)), (5, 5))
    screen.blit(font.render("int blocks = " + str(blocks), True, (0, 0, 0)), (5, 25))
    screen.blit(font.render("if key.press == 'r':", True, (0, 0, 0)), (5, 45))
    screen.blit(font.render("   restart()", True, (0, 0, 0)), (5, 65))