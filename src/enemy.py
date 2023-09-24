import pygame

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
    
    xs = w1/2 + w2/2
    ys = h1/2 + h2/2
    xd = abs((x1 + w1/2) - (x2 + w2/2))
    yd = abs((y1 + h1/2) - (y2 + h2/2))
    
    return (xd < xs and yd < ys)

class Enemy:
	def __init__(self, x, y, opposite, velX):
		self.x = x
		self.y = y
		self.w = 12
		self.h = 12
		self.opposite = opposite

		self.velX = velX
		self.hasCollideWithPlayer = False

	def draw(self, screen, img):
		flip = (self.velX < 0)
		sprite_enemy = pygame.transform.flip(img, flip, self.opposite)
		screen.blit(sprite_enemy, (self.x, self.y), (0, 0, 20, 20))

	def createRect(self):	return (self.x, self.y, self.w, self.h)

	def update(self, rect2):
		enemy_rect = pygame.Rect(self.x, self.y, self.w, self.h)
		if box_hit(enemy_rect, rect2):
			self.velX *= -1 if self.x < rect2.x + rect2.h else 1
		self.x += self.velX
