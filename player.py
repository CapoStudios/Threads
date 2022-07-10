import pygame
pygame.mixer.init()

def box_hit(rect1, rect2):
    #-----------
    x1 = rect1.x
    y1 = rect1.y
    w1 = rect1.w
    h1 = rect1.h
    #-----------
    x2 = rect2.x
    y2 = rect2.y
    w2 = rect2.w
    h2 = rect2.h
    #-----------

    hit = False
    
    xs = w1*0.5 + w2*0.5
    ys = h1*0.5 + h2*0.5
    xd = abs((x1 + (w1/2)) - (x2+(w2/2)))
    yd = abs((y1 + (h1/2)) - (y2+(h2/2)))
    
    if xd < xs and yd < ys:
        hit = True
    
    return hit

#---------------------------------------------------
#Player Constructor
class Player:  
    def __init__(self, x, y, w, h, color, opposite):  
        self.x = x  
        self.y = y 
        self.w = w 
        self.h = h  
        self.onFloor  = False
        self.opposite = opposite
        self.flip = False

        self.color = color

        self.velX = 2
        self.velY = 0
        self.acc  = 0.1

        self.getStar = False
        self.blocks  = 0
        self.moveCursorTutorial = False
        self.alreadyPrint = False
        self.endCircleRadius = 500

        self.level = 1

        self.jumpSound  = pygame.mixer.Sound('assets/jump.wav')
        self.starSound  = pygame.mixer.Sound('assets/star.wav')
        self.deadSound  = pygame.mixer.Sound('assets/dead.wav')
        self.clickSound = pygame.mixer.Sound('assets/click.wav')
        self.leverSound = pygame.mixer.Sound('assets/leverSound.wav')


    def resetStar(self):
        self.getStar = False
        self.blocks  = 0


    #Getters
    #-------------------
    def getX(self):
        return self.x    

    def getY(self):
        return self.y

    def getW(self):
        return self.w
   
    def getH(self):
        return self.h 
    #-------------------


    def setPos(self, newX, newY):
        self.x = newX
        self.y = newY

    def resetVel(self):
        self.velX = 2
        self.velY = 0
        self.acc  = 0.1
        self.flip = False

    def input(self):
        if self.getStar == False:
            keys = pygame.key.get_pressed()
            #A/D - Left/Right
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.x -= self.velX
                self.flip = True

            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.x += self.velX
                self.flip = False        
            
            #Jump(Space)
            if self.onFloor == True:
                if keys[pygame.K_UP] or keys[pygame.K_SPACE]: 
                    self.jumpSound.play()
                    self.velY = -3
                    self.onFloor = False
                

    def draw(self, screen, img, x, y, crop):
        screen.blit(pygame.transform.flip(img, self.flip, self.opposite), (x, y), crop)

    def gravity(self):
        if self.opposite == False:
            self.y += self.velY
            self.velY += self.acc
        else:
            self.y -= self.velY
            self.velY += self.acc

    def wallCollide(self, width, height):
        if self.opposite == False:
            if self.y >= (height/2) - self.h:
                self.y = (height/2) - self.h
                self.onFloor = True

            if self.y <= 0:
                self.y = 1

            if self.x >= width - self.w:
                self.x = width - self.w

            if self.x <= 0:
                self.x = 0
        else:
            if self.y <= (height/2):
                self.y = (height/2)
                self.onFloor = True

            if self.y + self.h >= height:
                self.y = height - self.h

            if self.x >= width - self.w:
                self.x = width - self.w

            if self.x <= 0:
                self.x = 0


    def createRect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


    def collideWith(self, rect2):
        if box_hit(pygame.Rect(self.x, self.y, self.w, self.h), rect2):
            if self.opposite == False:
                if self.y-self.h < rect2.y-rect2.h:
                    self.y = rect2.y - self.h
                    self.velY = 0
                    self.acc  = 0.1
                    self.onFloor = True
                else:
                    self.y = self.y 
                    if self.x <= rect2.x:
                        self.x -= self.velX
                    else:
                        self.x += self.velX
            else:
                if self.y+self.h > rect2.y+rect2.h:
                    self.y = rect2.y + rect2.h
                    self.velY = 0
                    self.acc  = 0.1
                    self.onFloor = True
                else:
                    self.y = self.y 
                    if self.x <= rect2.x:
                        self.x -= self.velX
                    else:
                        self.x += self.velX

    def collideWithRect(self, rect2):
        if box_hit(pygame.Rect(self.x, self.y, self.w, self.h), rect2):
            return True

    def collideWithStar(self, rect2):
        if box_hit(pygame.Rect(self.x, self.y, self.w, self.h), rect2):
            self.starSound.play()
            self.getStar = True
            self.acc = 0
            self.velY = 0
            self.x = self.x 
            self.y = self.y 

    def dead(self):
        self.deadSound.play()

    def click(self):
        self.clickSound.play()

    def lever(self):
        self.leverSound.play()