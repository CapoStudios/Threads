import pygame
pygame.mixer.init()

def box_hit(rect1, rect2):
    # Rect 1
    x1 = rect1.x
    y1 = rect1.y
    w1 = rect1.w
    h1 = rect1.h
    # Rect 2
    x2 = rect2.x
    y2 = rect2.y
    w2 = rect2.w
    h2 = rect2.h

    xs = w1/2 + w2/2
    ys = h1/2 + h2/2
    xd = abs((x1 + w1/2) - (x2 + w2/2))
    yd = abs((y1 + h1/2) - (y2 + h2/2))
    
    hit = (xd < xs and yd < ys)
    return hit


# Player Class
class Player:  
    def __init__(self, x, y, w, h, opposite):  
        self.x = x  
        self.y = y 
        self.w = w 
        self.h = h  
        self.onFloor  = False
        self.opposite = opposite
        self.flip = False

        self.velX = 2
        self.velY = 0
        self.acc  = 0.1

        self.getStar = False
        self.blocks  = 0
        self.moveCursorTutorial = False
        self.alreadyPrint = False
        self.endCircleRadius = 500

        self.level   = 1
        self.restart = False

        self.jumpSound  = pygame.mixer.Sound('../assets/jump.wav')
        self.starSound  = pygame.mixer.Sound('../assets/star.wav')
        self.deadSound  = pygame.mixer.Sound('../assets/dead.wav')
        self.clickSound = pygame.mixer.Sound('../assets/click.wav')
        self.leverSound = pygame.mixer.Sound('../assets/leverSound.wav')

    # reset only the velocity vars of the player
    def resetVel(self):
        self.velX = 2
        self.velY = 0
        self.acc  = 0.1
        self.flip = False

    # reset player variables
    def reset(self, x, y):
        self.x = x
        self.y = y

        self.resetVel()

        self.getStar = False
        self.blocks  = 0
        self.restart = False

    # Getters
    def getX(self): return self.x    
    def getY(self): return self.y

    def getW(self): return self.w
    def getH(self): return self.h 

    # set player position
    def setPos(self, newX, newY):
        self.x = newX
        self.y = newY

    def input(self):
        if not self.getStar:
            keys = pygame.key.get_pressed()
            # A/D - Left/Right
            dir_left  = int(keys[pygame.K_a] or keys[pygame.K_LEFT])
            dir_right = int(keys[pygame.K_d] or keys[pygame.K_RIGHT])

            self.x += self.velX * (dir_right - dir_left)

            if dir_left:    self.flip = True
            if dir_right:   self.flip = False        
            
            # Jump (Space)
            if self.onFloor and (keys[pygame.K_UP] or keys[pygame.K_SPACE]):
                self.jumpSound.play()
                self.velY = -3
                self.onFloor = False
                
    # draw the player
    def draw(self, screen, img, x, y, crop):
        screen.blit(pygame.transform.flip(img, self.flip, self.opposite), (x, y), crop)

    # exerts gravity on the players
    def gravity(self):
        self.y += -self.velY if self.opposite else self.velY
        self.velY += self.acc

    def wallCollide(self, width, height):
        if not self.opposite:
            if self.y >= (height/2) - self.h:
                self.y = (height/2) - self.h
                self.onFloor = True

            if self.y <= 0:
                self.y = 1
        else:
            if self.y <= (height/2):
                self.y = (height/2)
                self.onFloor = True

            if self.y + self.h >= height:
                self.y = height - self.h

        # collisions with the screen
        if self.x >= width - self.w:    self.x = width - self.w
        if self.x <= 0:                 self.x = 0

    def createRect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

    # Collide Functions
    def collideWith(self, rect2):
        if box_hit(pygame.Rect(self.x, self.y, self.w, self.h), rect2):
            if (not self.opposite and self.y-self.h < rect2.y-rect2.h) or (self.opposite and self.y+self.h > rect2.y+rect2.h):
                if (not self.opposite and self.y-self.h < rect2.y-rect2.h):     self.y = rect2.y - self.h 
                if (    self.opposite and self.y+self.h > rect2.y+rect2.h):     self.y = rect2.y + rect2.h
                
                self.velY = 0
                self.acc  = 0.1
                self.onFloor = True
            else:
                self.x += -self.velX if self.x <= rect2.x else self.velX

    def collideWithRect(self, rect2):
        return box_hit(pygame.Rect(self.x, self.y, self.w, self.h), rect2)

    def collideWithStar(self, rect2):
        if box_hit(pygame.Rect(self.x, self.y, self.w, self.h), rect2):
            self.starSound.play()
            self.getStar = True
            self.acc  = 0
            self.velY = 0

    # Update
    def update(self, width, height, elements):
        self.gravity()                  # Gravity
        self.input()                    # Handle Input
        self.wallCollide(width, height) # Wall Collisions

        for element in elements:
            self.collideWith(pygame.Rect(element))

    # Sounds
    def dead(self):     self.deadSound.play()
    def click(self):    self.clickSound.play()
    def lever(self):    self.leverSound.play()