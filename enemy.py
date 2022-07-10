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

    hit = False
    
    xs = w1*0.5 + w2*0.5
    ys = h1*0.5 + h2*0.5
    xd = abs((x1 + (w1/2)) - (x2+(w2/2)))
    yd = abs((y1 + (h1/2)) - (y2+(h2/2)))
    
    if xd < xs and yd < ys:
        hit = True
    
    return hit

class Enemy:
	def __init__(self, x, y, opposite, velX):
		self.x = x
		self.y = y
		self.w = 12
		self.h = 12
		self.flip  = False
		self.flipX = False
		self.opposite = opposite

		self.velX = velX
		self.hasCollideWithPlayer = False

	def draw(self, screen, img):
		if self.velX > 0:
			self.flip = False
		else:
			self.flip = True
		screen.blit(pygame.transform.flip(img, self.flip, self.opposite), (self.x, self.y), (0, 0, 20, 20))

	def createRect(self):
		return (self.x, self.y, self.w, self.h)

	def update(self, rect2):
		if box_hit(pygame.Rect(self.x, self.y, self.w, self.h), rect2):
			if self.x < rect2.x + rect2.h:
				self.velX = -self.velX
			else:
				self.velX = +self.velX
		self.x += self.velX